import re
import urllib
import os

def sort_function(name):
    searchfile = open(name + ".json", "r")
    writefile = open(name + "_Sorted.json", "w")
    for line in searchfile:
        #search for Location: something
            m = re.search('location":(.+?)\,"url', line)
            if m:
                found = m.group(1)
                if found == "null":
                    pass
                else:
                    writefile.write(found)
                    writefile.write("\n")
                    column = line.split() # split line into parts
                    if len(column) > 6:   # checks for enough columns
                        n = 5
                        writefile.write(column[n][68:] + " ")
                        if '","source"' in column[n]:
                            p = re.search('(.+?)\","source"', column[n])
                            if p:
                                found2 = p.group(1)
                                writefile.write(found2)
                            writefile.write("\n")
                        else:
                            n = 6
                            while "source" not in column[n]:
                                writefile.write(column[n] + " ")
                                n += 1
                            p = re.search('(.+?)\","source"', column[n])
                            if p:
                                found2 = p.group(1)
                                writefile.write(found2)
                            writefile.write("\n")


    searchfile.close()
    writefile.close()
    searchfile2 = open(name + "_Sorted.json", "r")
    writefile2 = open(name + "_SortedFiltered.json", "w")
    for line in searchfile2:
        ThisTweet = processTweet(line)
        writefile2.write(ThisTweet)
        writefile2.write("\n")
    searchfile2.close()
    writefile2.close()
    os.remove(name + "_Sorted.json")


def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https[^\s]+))','',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub('rt ', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #removing names
    tweet = re.sub('bernie', ' ', tweet)
    tweet = re.sub('sanders', ' ', tweet)
    tweet = re.sub('donald', ' ', tweet)
    tweet = re.sub('trump', ' ', tweet)
    tweet = re.sub('hillary', ' ', tweet)
    tweet = re.sub('rodham', ' ', tweet)
    tweet = re.sub('clinton', ' ', tweet)
    tweet = re.sub('ted', ' ', tweet)
    tweet = re.sub('cruz', ' ', tweet)
    tweet = re.sub('john', ' ', tweet)
    tweet = re.sub('kasich', ' ', tweet)
    tweet = re.sub('santa', ' ', tweet)
    tweet = re.sub('claus', ' ', tweet)

    #trim
    tweet = tweet.strip('\'"')
    return tweet

sort_function("Trump")
print "Trump Complete"

sort_function("Clinton")
print "Clinton Complete"

sort_function("Bernie")
print "Bernie Complete"

sort_function("Cruz")
print "Cruz Complete"

sort_function("Kasich")
print "Kasich Complete"



