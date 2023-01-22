# Desktop notifier app based on
# https://towardsdatascience.com/create-desktop-notifier-application-using-python-fb3b7b2c3cf3

import datetime
import time
import requests






# url of news rss feed
RSS_FEED_URL = "http://rss.cnn.com/rss/cnn_topstories.rss"

def print_hi(name):
    print(f'Hi, {name}')

def news():
    news = None
    try:
        news = requests.get(RSS_FEED_URL)
    except:
        # if the data is not fetched due to lack of internet
        print("Please! Check your internet connection")

    # if we fetched data
    if (news != None):
        # converting data into JSON format
        data = news.json()['Success']

        # repeating the loop for multiple times
        while (True):
            notification.notify(
                # title of the notification,
                title="CNN".format(datetime.date.today()),
                # the body of the notification
                message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                    totalcases=data['cases'],
                    todaycases=data['todayCases'],
                    todaydeaths=data['todayDeaths'],
                    active=data["active"]),
                # creating icon for the notification
                # we need to download a icon of ico file format
                app_icon="Paomedia-Small-N-Flat-Bell.ico",
                # the notification stays for 50sec
                timeout=50
            )
            # sleep for 4 hrs => 60*60*4 sec
            # notification repeats after every 4hrs
            time.sleep(60 * 60 * 4)




if __name__ == '__main__':
    print_hi('PyCharm')




