'''
Created on Aug 12, 2021

@author: 12563
'''
#nltk.download('vader_lexicon')
import os
from textblob import TextBlob
from pandas import read_csv
from dataProcess import clean_doc
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def sentiment(inputCsv,outputCsv,text):
    for row in read_csv(inputCsv,chunksize=20000,encoding='utf-8'):    
        #row.drop_duplicates(subset=['index'],inplace=True)        
        #row.dropna(subset=[text],inplace=True)
        row[text].fillna('null',inplace=True)
        #print( row[text])
        row['clean_text_'+text]=row[text].apply(lambda x: clean_doc(x))  
       # print( row['clean_text_'+text])  
        row['TextBlobPolarity_'+text]=row['clean_text_'+text].apply(lambda clean_text: TextBlob(clean_text).sentiment.polarity)
        #print(row['TextBlobPolarity'])
        row['TextBlob_Senti_'+text]=''
        row.loc[row['TextBlobPolarity_'+text]>0.1,'TextBlob_Senti_'+text]='POSITIVE'
        row.loc[row['TextBlobPolarity_'+text]==0 & row['TextBlobPolarity_'+text]<0.1,'TextBlob_Senti_'+text]='NEUTRAL'
        row.loc[row['TextBlobPolarity_'+text]<-0.1,'TextBlob_Senti_'+text]='NEGATIVE'        
        row['VADER_sent_Score_'+text] = row[text].apply(lambda textData: SentimentIntensityAnalyzer().polarity_scores(textData))
        #print(row['VADERscores_'+text])
        row['compound_'+text] = row['VADER_sent_Score_'+text].apply(lambda score_dict: score_dict['compound'])
        row['VADER_senti_'+text]=''
        
        row.loc[row['compound_'+text]>0.1,'VADER_senti_'+text]='POSITIVE'
        row.loc[row['compound_'+text]>-0.1 & row['compound_'+text]<0.1,'VADER_senti_'+text]='NEUTRAL'
        row.loc[row['compound_'+text]<-0.1,'VADER_senti_'+text]='NEGATIVE'
               
        if os.path.isfile(outputCsv):
            row.to_csv(outputCsv,index=None,header=None,mode='a')
        else:
            row.to_csv(outputCsv,index=None)     
  
#sentiment("Final_merge_city_state_country_listed_tweettext_news_tweetplace_senti.csv","Final_merge_city_state_country_listed_tweettext_news_tweetplace_senti_all.csv",'news_Text')

def emotion(text):
    from nrclex import NRCLex   
    print(text[0]) 
    emotion = NRCLex(text[0]).top_emotions
    return emotion
#print(emotion(['i do not hate']))  
#print(emotion(['The Delta Variant May Cause Different COVID-19 Symptoms'])) 

