# this is skelton code for new language support

stopwords = set()

js_stemmer_code = """
/**
 * Dummy Stemmer
 */
var Stemmer = function() {
  this.stemWord = function(w) {
    return w;
  }
}
"""

class Stemmer(object):
    def stem(self, word):
        return word


class Splitter(object):
    def __init__(self, option):
        pass

    def split(self, input):
        return []

