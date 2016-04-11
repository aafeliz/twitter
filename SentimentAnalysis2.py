import re, math
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk import precision
from nltk import recall


class predictor:
    def make_full_dict(self, words):
        return dict([(word, True) for word in words])

    def __init__(self):
        #reading pre-labeled input and splitting into lines
        posSentences = open('negMessages.txt', 'r')
        negSentences = open('posMessages.txt', 'r')
        posSentences = re.split(r'\n', posSentences.read())
        negSentences = re.split(r'\n', negSentences.read())

        posFeatures = []
        negFeatures = []
        #breaks up the sentences into lists of individual words (as selected by the input mechanism) and appends 'pos' or 'neg' after each list
        for i in posSentences:
            posWords = re.findall(r"[\w']+|[.,!?;]", i)
            posWords = [self.make_full_dict(posWords), 'pos']
            posFeatures.append(posWords)
        for i in negSentences:
            negWords = re.findall(r"[\w']+|[.,!?;]", i)
            negWords = [self.make_full_dict(negWords), 'neg']
            negFeatures.append(negWords)

        # selects 3/4 of the features to be used for training and 1/4 to be used for testing
        posCutoff = int(math.floor(len(posFeatures) * 3 / 4))
        negCutoff = int(math.floor(len(negFeatures) * 3 / 4))
        trainFeatures = posFeatures[:posCutoff] + negFeatures[:negCutoff]
        testFeatures = posFeatures[posCutoff:] + negFeatures[negCutoff:]

        self.classifier = NaiveBayesClassifier.train(trainFeatures)

        referenceSets = {'pos':set([]), 'neg':set([])}
        testSets = {'pos':set([]), 'neg':set([])}

        for i, (features, label) in enumerate(testFeatures):
            referenceSets[label].add(i)
            predicted = self.classifier.classify(features)
            testSets[predicted].add(i)
        posPrecision = precision(reference=referenceSets['pos'], test=testSets['pos'])
        print 'train on %d instances, test on %d instances' % (len(trainFeatures), len(testFeatures))
        print 'accuracy:', nltk.classify.util.accuracy(self.classifier, testFeatures)
        print 'pos precision:', precision(referenceSets['pos'], testSets['pos'])
        print 'pos recall:', recall(referenceSets['pos'], testSets['pos'])
        print 'neg precision:', precision(referenceSets['neg'], testSets['neg'])
        print 'neg recall:',recall(referenceSets['neg'], testSets['neg'])
        self.classifier.show_most_informative_features(10)

    def test(self, sentence):
        words = sentence.split()
        true = []
        for i in range(len(words)):
            true.append(True)
        wordsDict = dict(zip(words,true))
        prediction = self.classifier.classify(wordsDict)
        return prediction


print 'using all words as features'
analyser = predictor()
prediction = analyser.test("its really bad")
print str(prediction)
