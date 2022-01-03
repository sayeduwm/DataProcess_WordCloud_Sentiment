'''
Created on Aug 19, 2021

@author: 12563'''

import nltk
import string
from collections import Counter            

B_list={'not paying':0.30,'paying attention':0.5,'attention and':.25,'looked up':0.1,'the lgpd':0.99,'looking down':.45,'vehicles stopped':0.5}
#print(list(B_list)[-1])
U_list={'looked':0.95,'paying':0.98,'stopped': 0.75,'vehicles':0.6,'traveling':0.65,'avoid':0.8}
texts='''ON THE ABOVE DATE AND TIME, I (OFC GREETHAM) WAS ON DUTY FOR THE LGPD IN FULL UNIFORM AND IN M/S 203.  I WAS DISPATCHED TO 1300BLK OF W MAIN ST FOR A 3 CAR ACCIDENT.  VEHICLE'S 1,2, AND 3 WERE ALL TRAVELING EASTBOUND ON W MAIN ST.  VEHICLE 3 STOPPED FOR A CAR TURNING ACROSS TRAFFIC.  THE DRIVER OF VEHICLE 1 WAS NOT PAYING ATTENTION AND COULD NOT STOP IN TIME TO AVOID REAR ENDING VEHICLE 2, WHICH THEN REAR ENDED VEHICLE 3.  DRIVER OF VEHICLE 1 ADMITTED TO LOOKING DOWN FOR A MOMENT AND LOOKED UP TO SEE THE VEHICLES STOPPED IN TRAFFIC.  GREETHAM 350'''  
def textViz(texts,B_list,U_list):
    bposition=0
    textl=texts.lower() 
    textl=textl.split()
    #print(textl)
    exclude = set(string.punctuation)
    textB=[[''.join(ch for ch in textl[i] if ch not in exclude)+' '+''.join(ch for ch in textl[i+1] if ch not in exclude),textl[i]+' '+textl[i+1]] for i in range(0,len(textl)-1)]
    #print(textB)
    new_Text=''
    for bigram in textB:
        if bigram[0] in B_list.keys():     
            bposition+=1
            if bposition<2:
                unigram=bigram[0].split()
                unigramDis=bigram[1].split() 
                bigram_last_word=bigram[1].split()
                #print(unigramDis,bigram_last_word)           
                if unigram[0] in U_list.keys() and  unigram[1] not in U_list.keys():
                    imp=' '+'<span style="background-color: rgb(0,200,100,'+str( B_list[bigram[0]])+')">'+'<span style="background-color: rgb(256,200,100,'+str( U_list[unigram[0]])+')">'+unigramDis[0]+'</span>'+' '+unigramDis[1]+'</span>'           
                    new_Text=new_Text+' '+imp
                    
                elif unigram[0] not in U_list.keys() and  unigram[1]  in U_list.keys():
                    imp=' '+'<span style="background-color: rgb(0,200,100,'+str( B_list[bigram[0]])+')">'+unigramDis[0]+' '+'<span style="background-color: rgb(256,200,100,'+str( U_list[unigram[1]])+')">'+unigramDis[1]+'</span></span>'           
                    new_Text=new_Text+' '+imp
                
                elif unigram[0] in U_list.keys() and  unigram[0]  in U_list.keys():
                    imp=' '+'<span style="background-color: rgb(0,200,100,'+str( B_list[bigram[0]])+')">'+'<span style="background-color: rgb(256,200,100,'+str( U_list[unigram[0]])+')">'+unigramDis[0]+'</span>'+' '+'<span style="background-color: rgb(256,200,100,'+str( U_list[unigram[1]])+')">'+unigramDis[1]+'</span></span>'           
                    new_Text=new_Text+' '+imp                                  
                else:
                    imp=' '+'<span style="background-color: rgb(0,200,100,'+str( B_list[bigram[0]])+')">'+bigram[1]+'</span>'           
                    new_Text=new_Text+' '+imp                       
            else:
                bigram_last_word_keys=bigram[0].split()                        
                bigram_last_word=bigram[1].split()
                #print(bigram_last_word_keys,bigram_last_word)
                if bigram_last_word[1] in U_list.keys():
                    imp='<span style="background-color: rgb(0,200,100,'+str( B_list[bigram[0]])+')">'+' '+'<span style="background-color: rgb(256,200,100,'+str( U_list[bigram_last_word_keys[1]])+')">'+bigram_last_word[1]+'</span></span>'
                    new_Text=new_Text+imp
                else:
                    imp='<span style="background-color: rgb(0,200,100,'+str( B_list[bigram[0]])+')">'+' '+bigram_last_word[1]+'</span>'
                    new_Text=new_Text+imp                
        else:
            if  bposition>=1:
                bposition=0
            else:
                bigram_last_word_keys=bigram[0].split()                        
                bigram_last_word=bigram[1].split()
               
                if bigram_last_word[0] in U_list.keys():
                    imp=' '+'<span style="background-color: rgb(256,200,100,'+str( U_list[bigram_last_word_keys[0]])+')">'+bigram_last_word[0]+'</span>'
                    new_Text=new_Text+imp
                    #print('p ',imp,bigram_last_word[1])
                else:
                    new_Text=new_Text+' '+bigram[1].split()[0]
                    #print('not in ',bigram[1].split()[0])
               
    last_bigram=textB[-1][1]        
    if last_bigram not in  B_list.keys():
        new_Text=new_Text+' '+last_bigram.split()[1]                          
    return new_Text
print(textViz(texts,B_list,U_list))
