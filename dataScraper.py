from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import datetime


# Update these variable values for the user and timeline you want to scrape the tweets for
screenName = 'realdonaldtrump'
fromDate = datetime.datetime(2017, 1, 20)  # yyyy, m, d
toDate = datetime.datetime(2018, 8, 1)  # yyyy, m, d

# Update these variables to change the wait time between page loads or the browser to be used
wait = 1  # No. of seconds to wait before reloading a page
webDriver = webdriver.Chrome()  # Options- Chrome() Firefox() Safari()



tweetIdFile = 'tweetIds.json'
days = (toDate - fromDate).days + 1
idSelector = '.time a.tweet-timestamp'
tweetSelector = 'li.js-stream-item'
screenName = screenName.lower()
ids = []

def formatDays(date):
    day = '0' + str(date.day) if len(str(date.day)) == 1 else str(date.day)
    month = '0' + str(date.month) if len(str(date.month)) == 1 else str(date.month)
    year = str(date.year)
    return '-'.join([year, month, day])

def createUrl(fromDay, toDay):
    part1 = 'https://twitter.com/search?f=tweets&vertical=default&q=from%3A'
    part2 =  screenName + '%20from%3A' + fromDay + '%20to%3A' + toDay + 'include%3Aretweets&src=typd'
    return part1 + part2

def incrementDays(date, i):
    return date + datetime.timedelta(days=i)

for day in range(days):
    day1 = formatDays(incrementDays(fromDate, 0))
    day2 = formatDays(incrementDays(fromDate, 1))
    url = createUrl(day1, day2)
    print(url)
    print(day1)
    webDriver.get(url)
    sleep(wait)

    try:
        tweetsFound = webDriver.find_elements_by_css_selector(tweetSelector)
        increment = 10

        while len(tweetsFound) >= increment:
            print('Loading more tweets')
            webDriver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(wait)
            tweetsFound = webDriver.find_elements_by_css_selector(tweetSelector)
            increment += 10

        print('{} tweets have been found, {} in total'.format(len(tweetsFound), len(ids)))

        for tweet in tweetsFound:
            try:
                id = tweet.find_element_by_css_selector(idSelector).get_attribute('href').split('/')[-1]
                ids.append(id)
            except StaleElementReferenceException as e:
                print('Stale element reference', tweet)

    except NoSuchElementException:
        print('No tweets found for this day')

    fromDate = incrementDays(fromDate, 1)


try:
    with open(tweetIdFile) as f:
        tweetIds = ids + json.load(f)
        tweetsToFind = list(set(tweetIds))
        print('Total no. of tweets scraped: ', len(ids))
        print('Total tweets: ', len(tweetsToFind))
except FileNotFoundError:
    with open(tweetIdFile, 'w') as f:
        tweetIds = ids
        tweetsToFind = list(set(tweetIds))
        print('Total no. of tweets scraped: ', len(ids))
        print('Total tweets: ', len(tweetsToFind))

with open(tweetIdFile, 'w') as outfile:
    json.dump(tweetsToFind, outfile)

print('Scraping completed')
webDriver.close()
