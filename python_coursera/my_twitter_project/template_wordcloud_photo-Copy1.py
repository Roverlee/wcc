
# coding: utf-8

# In[3]:

#some of these might not be needed 
#wordcloud has stopwords in it, so 
#don't actually need to do that step but i did
#i didn't use stemmer but leaving in for future
import warnings
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
#
from PIL import Image
# suppress warnings
import matplotlib.image as mpimg
warnings.filterwarnings ( 'ignore' )
get_ipython().magic(u'matplotlib inline')
import os 
import nltk
import re
import time
import nltk.tag.stanford as st
from nltk.corpus import stopwords # Import the stop word list
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud










# In[4]:

# load listings data into a pandas df
#skiprows keeps it from having a double header
#im only going to use a few columns
cleanedDF = pd.read_csv ("test322.csv") #trump realDT tweets march 22 download

# display the first two rows
cleanedDF.head ( 2 )


# In[5]:

#copy the sets to not accidentally change them
A = cleanedDF[:]

print(A.head(5))

#get rid of retweets, ie leave in null retweets, then drop that column
newDF = A[A["retweeted_status"].isnull()].dropna(axis=1)



# In[6]:

#then grab the content that column..
newDF['content'].head(5)


# In[7]:


#get rid of text after hashtags
newDF['content'] = newDF['content'].str[0:-1].str.split('#', expand=True)[0]
#get rid of text of http etc 
newDF['content'] = newDF['content'].str[0:-1].str.split('http', expand=True)[0]
#get rid of punctuation ...
# replace all the numbers and non letter characters   with a space 
newDF['content'] = newDF['content'].str.replace("[^a-zA-Z]", " ")
# convert the text into lower
newDF['content'] = newDF['content'].str.lower()

#i didnt worry about stemming here but perhaps i should

newDF['content'].head(10)
#len(newDF['content'])


# In[8]:

#amazing, kind of figured this out myself, is it good to have an array of arrays?

tokens = []
for row in newDF['content']:
    go = word_tokenize(row)
    tokens.append(go)
#(row for row in set(text1) if w.endswith('ableness'))



# In[14]:

#take out stopwords too
#can i filter out stopwords? this doesnt work
from nltk.corpus import stopwords

stoppy = set(stopwords.words('english'))

no_stop = []

for list in tokens:
    for x in list:
        if x not in stoppy:
            no_stop.append(x)

print(no_stop)


# In[15]:

from nltk import FreqDist
#trying to see frequency, amazingly, it works!!!
fdist1 = FreqDist(no_stop)

fdist1.most_common(10) 
most_common = []
for word, frequency in fdist1.most_common(18):
    most_common.append((u'{};{}'.format(word, frequency)))
    
print(most_common)
#if I want to use most frequent, I later have to split that..
new = [i.split(';', 1)[0] for i in most_common]
#make a list for a bigger wordcloud later that has stoppwords
new = [i.split(';', 1)[0] for i in no_stop]
print(new)


# In[16]:

# Genearte Word cloud  -- generating from all words, not most frequent

from scipy.misc import imread
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



#Get the text document and join all the words together

text = " ".join([each for each in no_stop])
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt

# lower max_font_size
wordcloud = WordCloud(max_font_size=100).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()



# In[17]:

#using a mask
text = " ".join([each for each in no_stop])

trump_color = np.array(Image.open("image090.png"))

wc = WordCloud(background_color="white", max_words=2000, mask=trump_color,
               max_font_size=40, random_state=42)
wc.generate(text)
# Show the Word cloud with colors that aren't in photo
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
#if the below isn't there you get a numbery thing that is a mystery to me!
plt.show()


# In[18]:

#using a mask
text = " ".join([each for each in no_stop])

trump_color = np.array(Image.open("image090.png"))

wc = WordCloud(background_color="white", max_words=2000, mask=trump_color,
               max_font_size=40, random_state=42)
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(trump_color)


plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()



# In[19]:

#using a mask
text = " ".join([each for each in no_stop])

trump_color = np.array(Image.open("image090.png"))

wc = WordCloud(background_color="white", max_words=2000, mask=trump_color,
               max_font_size=40, random_state=42)
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(trump_color)

 #the below can be fun if you want to mess with it
    #making it into one channel color -- http://matplotlib.org/users/image_tutorial.html
lum_img = img_mask[:,:,0]
    #get rid of grid on image of trumpy
plt.grid(False)
    #showing the image
plt.imshow(lum_img)
    #luminosity dfault called jet
plt.imshow(lum_img, cmap="hot")
#imgplot = plt.imshow(lum_img)
    #the below is cool!
#imgplot.set_cmap('nipy_spectral')
plt.axis("off")




# In[ ]:

#make a bar chart of most common words


# plot the bar graph for top 20 occuring words  for full,pos ,neg dataset 
fig = plt.figure(figsize=(20,25))

plt.show()

