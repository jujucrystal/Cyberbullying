#encoding: utf-8

import pandas as pd
import string
import pyarabic.araby as araby


url = "https\S+|www.\S+"
emoji1 = r'[^\w\s,]'
mention = "@[^\\s]+"
hashtags = "#[^\\s]+"
Arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
Alef = (u'ا', u'آ', u'أ', u'إ', u'ٱ', u'ٰ')
Tehlike = (u'ة',u'ه')
Wawlike = (u'و', u'ؤ')
extraSpace = "  *"
newLine = ("\n" ,"\n\n", "\n\n\n")
repeated_letters = r'(.)\1{3,}'
digits = r'[0-9]+'
arabic_digits = (u'٠',u'١',u'٢',u'٣',u'٤',u'٥',u'٦',u'٧',u'٨',u'٩')
#import your desired data and save it as data frame
df = pd.read_csv('file path .... /saudiData2.csv')
#remove tashkeel
for tashkeel in araby.TASHKEEL:
    df['text'] = df['text'].str.replace(tashkeel,'')
#Normalization
for Alefat in Alef:
    df['text'] = df['text'].str.replace(Alefat, u'ا')
for YEHLIKE  in araby.YEHLIKE:
    df['text'] = df['text'].str.replace(YEHLIKE, u'ي')
for Teh in Tehlike:
    df['text'] = df['text'].str.replace(Teh, u'ه')
for waw in Wawlike:
    df['text'] = df['text'].str.replace(waw, u'و')
#remove url,mention,hashtags,emoji ...
df['text'] = df['text'].str.replace(url, " ", case=False)
df['text'] = df['text'].str.replace(mention," ", case = False)
df['text'] = df['text'].str.replace(hashtags," ", case = False)
df['text'] = df['text'].str.replace(emoji1," ", case = False)
df['text'] = df['text'].replace(newLine," ", regex= True) #remove new lines
df['text'] = df['text'].replace(repeated_letters,r'\1',regex = True)
df['text'] = df['text'].replace(digits,'',regex = True)
df['text'] = df['text'].replace(arabic_digits,'',regex = True)
#remove english and arabic punctuation
for s in string.punctuation:
    df['text'] = df['text'].str.replace(s,' ')
for s in Arabic_punctuations:
    df['text'] = df['text'].str.replace(s,' ')
for s in string.ascii_letters: #remove non-arabic letters
    df['text'] = df['text'].str.replace(s, ' ')
df['text'] = df['text'].replace(extraSpace, " ", regex=True) #remove extra spaces
df['text'] = df['text'].str.replace(r'\b\w\b','').str.replace(r'\s+',' ') #remove single letter

#save cleaned data as csv file
df.to_csv("cleaned_data2.csv", sep='\t', encoding='utf-8', index=False)





