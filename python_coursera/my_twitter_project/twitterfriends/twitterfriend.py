#so i produce the json that should match with bostocks miserables.json example,
# and his js example but have to figure out how to render that?

import sqlite3
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn = sqlite3.connect('twitterfriend.sqlite')
cur = conn.cursor()


print "Creating JSON output on twitter.js..."
howmany = int(raw_input("How many nodes? "))
#retrieve all the rows
cur.execute('SELECT * FROM Friends')
#create where.js
fhand = open('twitter.json','w')
nodes = list()
maxrank = None
minrank = None


for row in cur :

    nodes.append(row)

    #need to append martha here as one node

     #ranking by friendsfollwers count, row 6
#    if maxrank < rank or maxrank is None : maxrank = rank
#    if minrank > rank or minrank is None : minrank = rank
    if len(nodes) > howmany : break
    print row
print nodes
#if maxrank == minrank or maxrank is None or minrank is None:
#    print "Error page rank"
#    quit()


fhand.write('{"nodes":[\n')
fhand.write('{"id": "Martha", "group": 1},\n')
count = 0
map = dict()
for row in nodes :
    #get name of central person, in this case Martha
    #mainname = row[x]
    name = row[3]
    print name
    if count > 0 : fhand.write(',\n')
    fhand.write('{"id": ' + '"' + name + '"' + ', "group": 2}')
    count = count + 1
    #to make the above work I had to add sys.setdefaultencoding('utf-8') and
fhand.write('],\n')

fhand.write('\n')

fhand.write('"links":[\n')
count = 0
map = dict()
for row in nodes :
    name = row[3]
    print name
    if count > 0 : fhand.write(',\n')
    fhand.write('{"source": ' + '"' + name +'"' + ', "target":' + ' "Martha", ' + ' "value" : 1 }')
    #to make the above work I had to add sys.setdefaultencoding('utf-8') and
    count = count + 1
fhand.write(']\n')
fhand.write('};\n')
