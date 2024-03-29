# -*- coding: utf-8 -*-
"""
    sphinx.websupport.storage.sqlalchemystorage
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    An SQLAlchemy storage backend.

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from datetime import datetime

import sqlalchemy
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func

if sqlalchemy.__version__[:3] < '0.5':
    raise ImportError('SQLAlchemy version 0.5 or greater is required for this '
        'storage backend; you have version %s' % sqlalchemy.__version__)

from sphinx.websupport.errors import CommentNotAllowedError, \
     UserNotAuthorizedError
from sphinx.websupport.storage import StorageBackend
from sphinx.websupport.storage.sqlalchemy_db import Base, Node, \
     Comment, CommentVote, Session
from sphinx.websupport.storage.differ import CombinedHtmlDiff


class SQLAlchemyStorage(StorageBackend):
    """
    A :class:`.StorageBackend` using SQLAlchemy.
    """

    def __init__(self, uri):
        self.engine = sqlalchemy.create_engine(uri)
        Base.metadata.bind = self.engine
        Base.metadata.create_all()
        Session.configure(bind=self.engine)

    def pre_build(self):
        self.build_session = Session()

    def has_node(self, id):
        session = Session()
        node = session.query(Node).filter(Node.id == id).first()
        session.close()
        return True if node else False

    def add_node(self, id, document, source):
        node = Node(id, document, source)
        self.build_session.add(node)
        self.build_session.flush()

    def post_build(self):
        self.build_session.commit()
        self.build_session.close()

    def add_comment(self, text, displayed, username, time,
                    proposal, node_id, parent_id, moderator):
        session = Session()
        proposal_diff = None

        if node_id and proposal:
            node = session.query(Node).filter(Node.id == node_id).one()
            differ = CombinedHtmlDiff()
            proposal_diff = differ.make_html(node.source, proposal)
        elif parent_id:
            parent = session.query(Comment.displayed).\
                filter(Comment.id == parent_id).one()
            if not parent.displayed:
                raise CommentNotAllowedError(
                    "Can't add child to a parent that is not displayed")

        comment = Comment(text, displayed, username, 0,
                          time or datetime.now(), proposal, proposal_diff)
        session.add(comment)
        session.flush()
        # We have to flush the session before setting the path so the
        # Comment has an id.
        comment.set_path(node_id, parent_id)
        session.commit()
        d = comment.serializable()
        session.close()
        return d

    def delete_comment(self, comment_id, username, moderator):
        session = Session()
        comment = session.query(Comment).\
            filter(Comment.id == comment_id).one()
        if moderator or comment.username == username:
            comment.username = '[deleted]'
            comment.text = '[deleted]'
            comment.proposal = ''
            session.commit()
            session.close()
        else:
            session.close()
            raise UserNotAuthorizedError()

    def get_metadata(self, docname, moderator):
        session = Session()
        subquery = session.query(
            Comment.id, Comment.node_id,
            func.count('*').label('comment_count')).group_by(
            Comment.node_id).subquery()
        nodes = session.query(Node.id, subquery.c.comment_count).outerjoin(
            (subquery, Node.id==subquery.c.node_id)).filter(
            Node.document==docname)
        session.close()
        session.commit()
        return dict([(k, v or 0) for k, v in nodes])

    def get_data(self, node_id, username, moderator):
        session = Session()
        node = session.query(Node).filter(Node.id == node_id).one()
        session.close()
        comments = node.nested_comments(username, moderator)
        return {'source': node.source,
                'comments': comments}

    def process_vote(self, comment_id, username, value):
        session = Session()

        subquery = session.query(CommentVote).filter(
            CommentVote.username == username).subquery()
        vote_alias = aliased(CommentVote, subquery)
        q = session.query(Comment, vote_alias).outerjoin(vote_alias).filter(
            Comment.id == comment_id)
        comment, vote = q.one()

        if vote is None:
            vote = CommentVote(comment_id, username, value)
            comment.rating += value
        else:
            comment.rating += value - vote.value
            vote.value = value

        session.add(vote)
        session.commit()
        session.close()

    def update_username(self, old_username, new_username):
        session = Session()

        session.query(Comment).filter(Comment.username == old_username).\
            update({Comment.username: new_username})
        session.query(CommentVote).\
            filter(CommentVote.username == old_username).\
            update({CommentVote.username: new_username})

        session.commit()
        session.close()

    def accept_comment(self, comment_id):
        session = Session()

        # XXX assignment to "comment" needed?
        comment = session.query(Comment).filter(
            Comment.id == comment_id).update(
            {Comment.displayed: True})

        session.commit()
        session.close()

    def reject_comment(self, comment_id):
        session = Session()

        comment = session.query(Comment).\
            filter(Comment.id == comment_id).one()
        session.delete(comment)

        session.commit()
        session.close()
