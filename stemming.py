
from pandas import DataFrame
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem.isri import ISRIStemmer
import fileinput



def stemming (text):
    st = ISRIStemmer()
    stemmed_words =[]
    words = word_tokenize(text)
    for w in words:
        stemmed_words.append(st.stem(w))
    stemmed_sentence = " ".join(stemmed_words)
    return stemmed_sentence



sentence =[]
for line in fileinput.input(files="cleaned_data2.csv", inplace=True, backup='.bak'):
        Tweets = stemming(line)
        sentence.append(Tweets)
df_sentences = DataFrame(sentence, columns = ["Text"])


df_sentences.to_csv("cleaned+.csv", sep='\t', encoding='utf-8', index=False)
