from __future__ import absolute_import, print_function, unicode_literals
import tweepy
import sys
import os
import jsonpickle


consumer_token = <TOKEN_KEY>
consumer_secret = <SECRET_KEY>

auth = tweepy.AppAuthHandler(consumer_token,consumer_secret) #Add ur keys
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
   print("problem connection to API")

api.rate_limit_status()['resources']['search']
searchQuery = 'place:08b2d74428e2ca88 "دب" OR " دبة" OR "مرتد " OR " مرتده" OR " مريض نفسي" OR " مجنون" OR " سربوت" OR “سامج” OR " العبد” OR “الخال " OR " معوق” OR " شاذ” OR " أهبل” OR “متخلف” OR “ديوث ” OR " خكري” OR “همجي " OR " لحجي” OR " غبي” OR " قبيح” OR “شين” OR “نشاز ”' 'OR " اعور” OR “همجي " OR " قبيحة” OR " لحجيه” OR " شينه” OR “مغرورة” OR “مستشرف ” OR " دبشه” OR “ساذج” '

maxTweets = 100000 #1000000
tweetsPerQry = 500 #100


tweetCount = 0
with open('saudiData.json', 'w') as f:
    for tweet in tweepy.Cursor(api.search,q=searchQuery, lang= 'ar').items(maxTweets):
        if tweet.place is not None:
            p =  jsonpickle.encode(tweet._json, unpicklable=False)
            xp = p.encode('utf-8')
            f.write(xp + '\n')
            tweetCount += 1
print("Downloaded {0} tweets".format(tweetCount))

