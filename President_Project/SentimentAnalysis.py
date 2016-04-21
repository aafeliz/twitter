
from nltk import tokenize
import nltk.data

#nltk.download()

# READ ME
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
    def __init__(self, trainer = "classifiers/movie_reviews_sklearn.LinearSVC.pickle"):
        self.classifier = nltk.data.load(trainer)#movie_reviews classifiers/movie_reviews_sklearn.DecisionTreeClassifier.pickle
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

if __name__ == '__main__':
    ''' The following is an example of how the class works and can be utilized'''
    textAI = analyzer()
    # test whether it can reply to on sentence at a time
    print str(textAI.getSingleSentiment("this will return on result well"))
    # test whether it can collect many results into a list then spit them out to user
    textAI.classify("donald trump sucks")
    textAI.classify("all candicates plan to break the internet")
    textAI.classify("who will serve the people ?")
    textAI.classify("we live in a great country")
    textAI.classify("although some dont believe we do")
    textAI.classify("")
    textAI.classify("in foley square!! nyc come march with us")

    print (textAI.getClassified())

