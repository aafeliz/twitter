import re
import urllib

def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+',' ',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub('rt', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end


#Read the tweets one by one and process it
fp = open('President_Project/Kasich_SortedFiltered.json', 'r')
line = fp.readline()
pos_count = neg_count = neutral_count = 0

while line:
    processedTweet = processTweet(line)
    #print processedTweet
    data = urllib.urlencode({"text": processTweet(line)})
    u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
    the_page = u.read()
    #print(str(the_page))
    if "\"label\": \"pos\"" in the_page:
        pos_count += 1
    elif "\"label\": \"neg\"" in the_page:
        neg_count += 1
    elif "\"label\": \"neutral\"" in the_page:
        neutral_count += 1
    line = fp.readline()

#end loop
fp.close()

print "posititve: ", pos_count
print "negative: ", neg_count
print "netural: ", neutral_count


