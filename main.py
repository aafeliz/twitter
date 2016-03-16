import tweepy
from tweepy import OAuthHandler
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
names = {"Trump","Hilary",""}
class Trump(StreamListener):

    def on_data(self, data):
        try:

            with open('Trump.json'), 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
class Hilary(StreamListener):

    def on_data(self, data):
        try:

            with open('Hilary.json'), 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
class Bernie(StreamListener):

    def on_data(self, data):
        try:

            with open('Bernie.json'), 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

class Cruz(StreamListener):

    def on_data(self, data):
        try:

            with open('Cruz.json'), 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
twitter_stream = Stream(auth, Trump())
twitter_stream.filter(track=['#Trump', ])