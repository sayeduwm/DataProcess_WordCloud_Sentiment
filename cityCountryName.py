'''
Created on Aug 7, 2021

@author: 12563
'''

from pandas import read_csv,DataFrame
import geonamescache
from sklearn.feature_extraction.text import CountVectorizer
gc = geonamescache.GeonamesCache()
states=list(gc.get_us_states_by_names().keys())
#country
countryList=[(gc.get_countries().get(i).get('name')) for i in gc.get_countries().keys()]

#major cities    
cityDt=read_csv('US50MajorCitiesByPop.csv')

def findCityCountry(inputcsvfile, searchField,outputCsv):
    print("Using US50MajorCitiesByPop.csv  file to look for city name. It should have a field called 'CITY'")    
    DataFrame(columns=["WORD","CITY","STATE","COUNTRY"]).to_csv(outputCsv,header=None,index=None)
    targetDt=read_csv(inputcsvfile,usecols=[searchField])
    targetDt.dropna(subset=[searchField],inplace=True)
    vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 1),lowercase=True,stop_words='english')
    x=vectorizer.fit_transform( targetDt[searchField].values)
    unigramList=[i for i in vectorizer.get_feature_names() ]
    
    for word in unigramList:
    
        for i in cityDt['CITY'].values:    
            
            if  i.lower()== word.lower():            
                DataFrame(data=[[word,i,'','']]).to_csv(outputCsv,header=None,index=None,mode='a')
                
        for j in states:            
            if  j.lower()== word.lower():            
                DataFrame(data=[[word,'',j,'']]).to_csv(outputCsv,header=None,index=None,mode='a')
                
        for l in countryList:        
            if l[1].lower()==word.lower() :
                
                DataFrame(data=[[word,'','',l[1]]]).to_csv(outputCsv,header=None,index=None,mode='a')
    
    
def findCityCountryTweet(inputcsvfile, indexField,geoField,searchField,outputCsv):
    import string
    from nltk.corpus import stopwords
    
    print("\n\nUsing US50MajorCitiesByPop.csv  file to look for city name. It should have a field called 'CITY'\n   ...Running......")
    targetDt=read_csv(inputcsvfile,usecols=[indexField,geoField,searchField])
    targetDt.dropna(subset=[searchField],inplace=True) 
    DataFrame(columns=[indexField,geoField,"WORD","CITY","STATE","COUNTRY"]).to_csv(outputCsv,index=None)   
    for ind,geo,twt in zip(targetDt[indexField].values,targetDt[geoField].values,targetDt[searchField].values):
        doc=twt.lower()
        tokens=doc.split()
        table=str.maketrans('','',string.punctuation)
        tokens=[w.translate(table) for w in tokens]
        stop_words=set(stopwords.words('english'))
        tokens2=[w for w in tokens if not w in stop_words]
        city=[]
        state=[]
        country=[]
        wordlist=[]
        for word in tokens2:           
 
    
            for i in cityDt['CITY'].values:    
                
                if  i.lower()== word.lower(): 
                    city.append(i),wordlist.append(word)          
                   
            for j in states:           
                if  j.lower()== word.lower(): 
                    state.append(j),wordlist.append(word)            
     
            for l in countryList:                        
                if l.lower()==word.lower() :
                    
                    country.append(l) ,wordlist.append(word)
        DataFrame(data=[[ind,geo,wordlist,city,state,country]]).to_csv(outputCsv,header=None,index=None,mode='a')
                
#findCityCountryTweet('final_Delta_Varient_simplyfy_news_merge_titile_and_newsText.csv','index','news_Title','mergeField','final_Delta_Varient_simplyfy_news_merge_titile_and_newsText_with_city_cstate_country_listed.csv')


def simplifyFindCityCountryTweet(inputcsv,outputcsv):
    from pandas import read_csv,DataFrame
    simplyfydf=read_csv(inputcsv)
    simplyfydfnew=simplyfydf[['index','news_Title','news_Text']]
    simplyfydfnew=simplyfydfnew[simplyfydfnew.news_Title !='0']
    simplyfydfnew.dropna(axis=0, subset=['news_Title'], inplace=True)   
    simplyfydfnew.to_csv(outputcsv,index=None)
    
#simplifyFindCityCountryTweet('final_Delta_Varient.csv','ffinal_Delta_Varient_simplyfy_news.csv')    

        
    