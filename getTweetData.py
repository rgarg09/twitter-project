import tweepy
import json
import math
import glob
import csv
import zipfile
import zlib
from tweepy import TweepError
from time import sleep

# Update this variable with the user you want to extract tweets for
screenName = 'realdonaldtrump'

with open('api_keys.json') as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)
screenName = screenName.lower()
outputFile = '{}.json'.format(screenName)
outputFileShort = '{}_short.json'.format(screenName)
compression = zipfile.ZIP_DEFLATED

with open('tweetIds.json') as f:
    ids = json.load(f)

print('Total ids found: {}'.format(len(ids)))

allData = []
start = 0
end = 100
limit = len(ids)
i = math.ceil(limit / 100)

for go in range(i):
    print('currently getting {} - {}'.format(start, end))
    sleep(6)  # Sleep time needed to prevent reaching the API extraction rate
    id_batch = ids[start:end]
    start += 100
    end += 100
    tweets = api.statuses_lookup(id_batch)
    for tweet in tweets:
        allData.append(dict(tweet._json))

print('Tweet data gathering completed')
print('Creating master output json file')
with open(outputFile, 'w') as outfile:
    json.dump(allData, outfile)

print('Creating master json in a zipped file')
jsonZipped = zipfile.ZipFile('{}.zip'.format(screenName), mode='w')
jsonZipped.write(outputFile, compress_type=compression)
jsonZipped.close()

results = []

def isRetweet(entry):
    return 'retweeted_status' in entry.keys()

def getSource(entry):
    if '<' in entry["source"]:
        return entry["source"].split('>')[1].split('<')[0]
    else:
        return entry["source"]

with open(outputFile) as json_data:
    data = json.load(json_data)
    for entry in data:
        t = {
            "created_at": entry["created_at"],
            "text": entry["text"],
            "in_reply_to_screen_name": entry["in_reply_to_screen_name"],
            "retweet_count": entry["retweet_count"],
            "favorite_count": entry["favorite_count"],
            "source": getSource(entry),
            "id_str": entry["id_str"],
            "is_retweet": isRetweet(entry)
        }
        results.append(t)

print('Creating a short master json file')
with open(outputFileShort, 'w') as outfile:
    json.dump(results, outfile)

with open(outputFileShort) as masterFile:
    data = json.load(masterFile)
    fields = ["favorite_count", "source", "text", "in_reply_to_screen_name", "is_retweet", "created_at", "retweet_count", "id_str"]
    print('creating CSV version of minimized json master file')
    f = csv.writer(open('{}.csv'.format(screenName), 'w'))
    f.writerow(fields)
    for x in data:
        f.writerow([x["favorite_count"], x["source"], x["text"].encode("utf-8"), x["in_reply_to_screen_name"], x["is_retweet"], x["created_at"], x["retweet_count"], x["id_str"]])
