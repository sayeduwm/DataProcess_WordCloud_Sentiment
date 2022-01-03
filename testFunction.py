'''
Created on Aug 19, 2021

@author: 12563'''


import pandas as pd
import re
import nltk
import re
import numpy as np
import pandas as pd
from pprint import pprint
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import spacy
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
nlp = spacy.load('en', disable=['parser', 'ner'])


def listtorow(index,rlist,outputfileName):
    k=[]
    for ind,i in zip(index,rlist): 
        ilist=[] 
        
        for j in i.split(','):
            x=re.sub(r'[^\w]', '', j)
            if x not in ilist and x!='Washington':                                 
                ilist.append(x)
        [k.append([ind,i]) for i in ilist]
    
    df2=pd.DataFrame(columns=['index','country'],data=k)   
    
    return df2.to_csv('news_country_xF.csv',index=None) 
#df=pd.read_csv('news_country_x.csv')       
#listtorow(df.Index,df.COUNTRY_News,outputfileName)      



def importantWord(text,bigram,unigram): 
    textl=text.split()  
    output='<p>'
    for t in textl:
        if t in unigram.keys():
            output=output+' ' +'<span style="background-color: rgb(0,200,100,'+str(unigram[t])+')">'+t+'</span>'
        else:
            output+=' '+t
             
    return output+'</p>'
            
          
#print(importantWord(texts,bigrams,unigrams))
#print('md sayed'.split())

def importantWordhybrid(text,bigram,unigram): 
    textl=texts.split(' ') 
    print(textl) 
    textl=[textl[i]+' '+textl[i+1] for i in range(0,len(textl)-1)]
    
    output='<p>'
    for tbigram in textl:
        tb=re.sub(r'[^\w]', " ", tbigram)
        for i in bigram.keys():
            
            if i==tb:
                print(tb)      
        if tb in bigram.keys():
            print(tb,bigram.keys())
            
            
            #btext='<span style="background-color: rgb(0,200,100,'+str(bigram[tb])+')">'+tb+'</span>'
            tu=tb.split()
            utext=' '
            for t in tu:
                #print(t)                
                if t in unigram.keys() and unigram[t]>bigram[tb]:
                    utext=utext+' ' +'<span style="background-color: rgb(0,200,100,'+str(unigram[t])+')">'+t+'</span>'
                else:
                    utext=utext+' ' +'<span style="background-color: rgb(0,200,100,'+str(bigram[tb])+')">'+tbigram+'</span>'
           
            #print(tb)
            #output=output+' ' +'<span style="background-color: rgb(0,200,100,'+str(bigram[tb])+')">'+tb+'</span>'
            output=output+utext
            #print(output)
        else:
            output=output+' ' +tbigram

    output=output+'</p>'         
    return output
import string
import nltk
from collections import Counter            
B_list={'am not':0.30,"am say":0.5,'say full':.25,'full name':0.1}
unigrams={'am':0.95,'sayed':0.98}
texts='i am say. i am say. full name md abu sayed 80. what is your name am not'          
#print(importantWordhybrid(texts,bigrams,unigrams))
text1='i am say.  i am say. full name md abu sayed 80. what is your name am not happy.i am say. full name md abu sayed 80. what is your name am not happy' 
textl=texts.split(' ') 
exclude = set(string.punctuation)

textB={''.join(ch for ch in textl[i] if ch not in exclude)+' '+''.join(ch for ch in textl[i+1] if ch not in exclude):textl[i]+' '+textl[i+1] for i in range(0,len(textl)-1)}
#print(textB)
for tbigram in textl:
    tb=re.sub(r'[^\w]', " ", tbigram)
    #print(tb) 
    for i in B_list.keys():
            
        if i==tb:
            print(tb)      
    #if tb in bigrams.keys():
        #print(tb,bigrams.keys())
B_list={'am not':0.30,"am say":0.5,'say full':.25,'full name':0.1,'say i':0.99}
print(list(B_list)[-1])
unigrams={'am':0.95,'sayed':0.98}
texts='i am say.  i am say. full name md abu sayed 80. what is your name am not happy.i am say. WHAT IS HAPPENING. what is your name am not happy'  
text_string = texts.lower()
exclude = set(string.punctuation)
text_string = ''.join(ch for ch in text_string if ch not in exclude)
bigrams = []
bigms = list(nltk.bigrams(text_string .split()))
bigmC = Counter(bigms)
for key in bigmC.keys():
    text_string_b = str(key)
    text_string_b = ''.join(ch for ch in text_string_b if ch not in exclude)
    bigrams.append(text_string_b)

bposition=0
textl=texts.split() 
exclude = set(string.punctuation)
textB={''.join(ch for ch in textl[i] if ch not in exclude)+' '+''.join(ch for ch in textl[i+1] if ch not in exclude):textl[i]+' '+textl[i+1] for i in range(0,len(textl)-1)}
print(textB)
new_Text=''
for bigram in textB.keys():    
    if bigram in B_list.keys():     
        bposition+=1
        if bposition<2:
            print(B_list[bigram])
            imp=' '+'<span style="background-color: rgb(0,200,100,'+str( B_list[bigram])+')">'+textB[bigram]+'</span>'
            texts=texts.replace(bigram,imp)
            new_Text=new_Text+' '+imp          
             
        else:                        
            bigram_last_word=textB[bigram].split()
            print(bigram_last_word[1])
            imp='<span style="background-color: rgb(0,200,100,'+str( B_list[bigram])+')">'+' '+bigram_last_word[1]+'</span>'
            new_Text=new_Text+imp
            texts=texts.replace('</span>'+bigram_last_word[1],imp) 

    else:
        if  bposition>=1:
            bposition=0
        else:
            new_Text=new_Text+' '+textB[bigram].split()[0]
last_bigram=list(textB)[-1]        
if last_bigram not in  B_list.keys():
    new_Text=new_Text+' '+last_bigram.split()[1]

                          
print(new_Text)
b=['a']
st='i am sayed'
print(''.join(i for i in st if i not in b))