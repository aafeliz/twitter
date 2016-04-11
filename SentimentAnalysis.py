
from nltk import tokenize
import nltk.data

'''
- using pip install nltk
- You need to download https://github.com/japerk/nltk-trainer repo
- install it using following command: python setup.py install
- open up python, import nltk, then do nltk.download(), download all files option in the UI
- use link bellow to train classifiers in explainned in section 2.1
    https://media.readthedocs.org/pdf/nltk-trainer/latest/nltk-trainer.pdf
- I trained it with twitter sentence_polarity and moview_reviews using commands bellow:
        python train_classifier.py movie_reviews --classifier sklearn.LinearSVC
        python train_classifier.py sentence_polarity  --classifier sklearn.LinearSVC
'''
'''
def bag_of_words(words):
    return dict([(word, True) for word in words])

feats = bag_of_words(tokenize.word_tokenize("this works"))

classifier = nltk.data.load('classifiers/movie_reviews_sklearn.LinearSVC.pickle')
classed = classifier.classify(feats)
print str(classed)
'''

class analyzer:
    def __init__(self):
        self.classifier = nltk.data.load('classifiers/movie_reviews_sklearn.LinearSVC.pickle')
        self.classified = []
    def classify(self, sentence):
        feats = self.bag_of_words(tokenize.word_tokenize(sentence))
        self.classified.append(self.classifier.classify(feats))

    def getSingleSentiment(self, sentence):
        feats = self.bag_of_words(tokenize.word_tokenize(sentence))
        return self.classifier.classify(feats)

    def getClassified(self):
        return self.classified



    def bag_of_words(self, words):
        return dict([(word, True) for word in words])





