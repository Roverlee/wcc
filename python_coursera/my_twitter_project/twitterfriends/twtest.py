import urllib
#his augment fxn from his twurl.py
from twurl import augment

print "calling Twitter! Amazing!...You're welcome!"

url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {"screen_name": 'heatherwalsh100', 'count': '5'})

print url


connection = urllib.urlopen(url)
data = connection.read()  #this will be json data, this is the body

print data

headers = connection.info().dict  #asking info about the headers now, this is a dictionary of the headers
print headers
