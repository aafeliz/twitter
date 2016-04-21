import tweepy
from tweepy import OAuthHandler
from multiprocessing import Process
# Authentication details. To  obtain these visit dev.twitter.com

consumer_key = 'B0FxsKxDbCa6u2FYORxiEpILH'
consumer_secret = 'SLppwSRdMYGcJZ0A4d2hnw7AVR7IvBd0fVc12VKAHi4VEQl8SM'
access_token = '709884140439658496-vu3Tyk2EEa2Ewy4SrkiOgh5I0caVApg'
access_token_secret = 'LW6nZvUmes91NuA5gvR3Qioma5suGzPLSRzIRREx7mkmh'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener


class PresidentialListener(StreamListener):
    def on_data(self, data):
        try:
            if any(ext in data.lower() for ext in Sanders_words):
                with open('Bernie.json', 'a') as f:
                    f.write(data)
            if any(ext in data.lower() for ext in Trump_words):
                with open('Trump.json', 'a') as f:
                    f.write(data)
            if any(ext in data.lower() for ext in Clinton_words):
                with open('Clinton.json', 'a') as f:
                    f.write(data)
            if any(ext in data.lower() for ext in Cruz_words):
                with open('Cruz.json', 'a') as f:
                    f.write(data)
            if any(ext in data.lower() for ext in Kasich_words):
                with open('Kasich.json', 'a') as f:
                    f.write(data)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
    
Trump_words = ["trump", "thedonald", "The Donald", "makeamericagreat", "make america great" 'makedonalddrumph']
Sanders_words = ["sanders", "feelthebern", "feel the bern", "bernie"]
Clinton_words = ["hilary", "clinton"]
Cruz_words = ["cruz", "trust ted", "trustted", 'lyinted' "lyin ted"]
Kasich_words = ["kasich"]
key_words = Trump_words + Sanders_words + Clinton_words + Cruz_words + Kasich_words

while True:
    try:
        Presidential_stream = Stream(auth, PresidentialListener())
        Presidential_stream.filter(track=key_words)
    except: 
        continue



