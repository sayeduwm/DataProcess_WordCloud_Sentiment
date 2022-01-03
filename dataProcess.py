'''
Created on Aug 7, 2021

@author: 12563
'''

def clean_doc(text):
    import string,re
    from nltk.corpus import stopwords
    #list to store the clean data
    
    #read by narratives.Here,  A narrative is a string of multiple sentences.

    try:  
        #print(text)     
        doc=text.lower()
                # create temporary token
        #token=re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", doc).split()
        token=doc.split()
                # remove user name.tagged name
        tokens=[re.sub('[^A-Za-z0-9]+', '', i) for i in token  if '@' not in i and 'https' not in i]    
                # remove all punctuation
        #table=str.maketrans('','',string.punctuation)
        #tokens=[w.translate(table) for w in tokens]
                # remove numeric values
                #tokens1=[word for word in tokens if word.isalpha()]
                # remove stop words
        stop_words=set(stopwords.words('english'))
        tokens=[w for w in tokens if not w in stop_words]
                # remove words which has <= 2 characters
        if tokens: 
  
            tokens=' '.join([word for word in tokens]) 
        else:
            tokens='NA'
            

        #print('text:',"string length:",len(tokens),tokenF)
                # return the clean sentance again '
    
    #in case there is no value in the field
    except:
        tokens='null'
        

    return tokens
#print(clean_doc("@Oil_Can_Boy @CapnCook44 @jeffa_walker @ClayTravis False. https://t.co/W2roahGPOK"))
def simplifyFindCityCountryTweet(inputCsv,fieldList,outputCsv):
    from pandas import read_csv
    simplyfydf=read_csv(inputCsv)
    simplyfydfnew=simplyfydf[fieldList]
    simplyfydfnew=simplyfydfnew[simplyfydfnew.news_Title !='0']
    simplyfydfnew.dropna(axis=0, subset=['news_Title'], inplace=True)   
    simplyfydfnew.to_csv(outputCsv,index=None)
 

def mergeField(inputCsv,mergeFieldList,outputCsv):
    from pandas import read_csv
    simplyfydf=read_csv(inputCsv)
    simplyfydf['mergeField']=''
    for field in mergeFieldList:
        simplyfydf['mergeField']+=(' '+simplyfydf[field])
    simplyfydf.to_csv(outputCsv,index=None)    
#mergeField('final_Delta_Varient_simplyfy_news.csv',['news_Title','news_Text'],'final_Delta_Varient_simplyfy_news_merge.csv')

def JoinCSV(inputCsv1,inputCsv2,key,rule,outputCsv):
    from pandas import read_csv
    Source=read_csv(inputCsv1)
    Target=read_csv(inputCsv2)
    newCsv=Source.merge(Target,how=rule,on=key)
    return newCsv.to_csv(outputCsv,index=None) 
#JoinCSV('Final_merge_city_state_country_listed_tweettext_news_tweetplace.csv','final_Delta_Varient_simplyfy_news.csv','index','left','Final_merge_city_state_country_listed_tweettext_news_tweetplace.csv')
def JoinCSVSelectedField(inputCsv1,inputCsv2,key,rule,outputCsv,fieldlist):
    from pandas import read_csv
    Source=read_csv(inputCsv1)
    Target=read_csv(inputCsv2)
    fieldlist.append(key)
    Target=Target[fieldlist]
    newCsv=Source.merge(Target,how=rule,on=key)
    return newCsv.to_csv(outputCsv,index=None) 
JoinCSVSelectedField('tweet_country_xF.csv','clean_tweet_Text_emotion_senti.csv','index','left','tweet_caountry_xF_emotion_senti.csv',['anger','anticipation','disgust','fear','joy','sadness','surprise','trust','cSentiment'])
def city(text):  
    str=text.split(',')  
    for i in text:
        if len(str)==3:
            return str[0]
    
def state(text):  
    str=text.split(',')  
    for i in text:
        if len(str)==3:
            return str[1]
        
#seperate sity,state from the Place fields        
def findUnique(inputCsv,outputCsv,textField):
    from pandas import read_csv
    Uniquedf=read_csv(inputCsv)
    Uniquedf.dropna(subset=[textField],inplace=True)
    Uniquedf['city_tweet']=Uniquedf[textField].apply(lambda x:city(x))
    Uniquedf['state_tweet']=Uniquedf[textField].apply(lambda x:state(x))
    return Uniquedf.to_csv(outputCsv,index=None)

#findUnique('outputCsv_sentiment.csv','Place_x')        
    
