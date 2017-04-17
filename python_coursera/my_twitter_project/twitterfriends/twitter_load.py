

import urllib
import sqlite3
import json
import time
import ssl
import twurl  #to augment the twitter url


# put twitter api in here
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'




scontext = None
#i have to make it so it replaces the table or something else
conn = sqlite3.connect('twitterfriend7.sqlite')
cur = conn.cursor()


print 'created the database'

cur.execute('''

CREATE TABLE IF NOT EXISTS Friends (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    twitteruser TEXT,
    friendtwitterhandle TEXT UNIQUE,
    friendname  TEXT,
    friendid INTEGER,
    twitterimage TEXT,
    friendfollowerscount INTEGER,
    description TEXT,
    friendscount INTEGER,
    latestTweet TEXT
)
''')

print 'created the table'


#start retrieving from API
while True:
    print ''
    acct = raw_input("Enter Twitter Account: ")
    if (len(acct) < 1 ) : break
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': 5} ) #gives you the five friends of that account
#look more closely at the possible other parameters to be added here, ie for trump tweets etc
    print "Retrieving baby!", url

    connection = urllib.urlopen(url) #getting data
    data = connection.read() #reading the body which is in json...
    headers = connection.info().dict #hold onto the headers, which are a dictionary, for later

    print "Remaining", headers['x-rate-limit-remaining']

#so all below has to be in while statement? do i need that?
    js = json.loads(data) #deserializing the json and turning
#that into a list, an array)
    print json.dumps(js, indent=4) #taking array of objects, js, and prettify json

#get some
    for us in js['users'] :  #go through the list and for each user the screen name and their status
        friendtwitterhandle = us['screen_name']
        friendname = us['name']
        friendid = us['id_str']
        twitterimage = us['profile_image_url_https']
        friendfollowerscount = us['followers_count']
        description = us['description']
        friendscount = us['friends_count']
        latestTweet = us['status']['text']

        if friendtwitterhandle is None:
            continue

        print friendtwitterhandle

        cur.execute('''INSERT OR IGNORE INTO Friends (twitteruser, friendtwitterhandle, friendname, friendid,
        twitterimage, friendfollowerscount, description, friendscount, latestTweet)
                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)''', ( acct, friendtwitterhandle, friendname, friendid, twitterimage, friendfollowerscount, description, friendscount, latestTweet) )

        conn.commit()
        print " "
        print "check the database"
