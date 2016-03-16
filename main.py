import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'B0FxsKxDbCa6u2FYORxiEpILH'
consumer_secret = 'SLppwSRdMYGcJZ0A4d2hnw7AVR7IvBd0fVc12VKAHi4VEQl8SM'
access_token = '709884140439658496-vu3Tyk2EEa2Ewy4SrkiOgh5I0caVApg'
access_token_secret = 'LW6nZvUmes91NuA5gvR3Qioma5suGzPLSRzIRREx7mkmh'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #programming:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['Trump'])