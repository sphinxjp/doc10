# this is skelton code for new language support


import re


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
    """
    This class implements stemming algorythm.
    
    This class is dummy class. You should implement if that 
    language has any stemming rules.
    
    """
    def stem(self, word):
        """
        stemming method implementations
        
        :param word: input word
        :type  word: string
        :return: stemmed word
        :rtype:  string
        """
        return word


class Splitter(object):
    """Basic word splitter class
    
    This class can split almost all language which uses white space 
    between words.
    
    If your language is in CJK, you should implement this class for it.
    """
    word_re = re.compile(r'\w+(?u)')
    def __init__(self, option):
        pass

    def split(self, input):
        """
        word split method.
        
        :param word: input word
        :type  word: string
        :return: splitted words
        :rtype:  [string]
        """
        return self.word_re.findall(input)


def should_not_register(stemmed_word):
    return (len(stemmed_word) < 3 
             or stemmed_word in stopwords 
             or stemmed_word.isdigit())

