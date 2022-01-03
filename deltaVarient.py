'''
Created on Aug 7, 2021

@author: 12563
'''

import sys
import dataProcess as dp
from cityCountryName import findCityCountry,findCityCountryTweet
import analysis

if __name__ == '__main__':
    welcome_message=['\n\n******Welcome to Covid- Delta Varient Data Processing and Model Developments******\n'
    'Select An option from the following:\n',
    '1. Do you want to find unique city, state and county name in the corpus? then Input 1',
    '2. Do you want to find unique city, state and county name for each Tweet? then Input 2 ',
    '3. Export selected field from CSV? then input 3',
    '4.Merge two or more text fields of a csv? then input 4',
    '5.Merge two or more csv? then input 5',    
    '6. Sentiment analysis usingTextBold and VADER? input 6',
    '****Data Analysis***',
    ]
    for i in welcome_message:
        print(i)
    
    cityCountryRes= int(input('Input:'))
    if cityCountryRes==1:        
        inputcsvfile=input("Provide Csv file that contains text: ")        
        outputCsv=input("Give a Csv Output File Name: ") 
        searchField=input("Name of Text field name to look for City and Country Name: ")
        findCityCountry(inputcsvfile, searchField,outputCsv)
    elif cityCountryRes==2:
        inputcsvfile=input("Provide Csv file that contains text: ")
        outputCsv=input("Give a Csv Output File Name: ") 
        indexField=input("Name of Index(primary key) field name to look for City and Country Name: ")
        searchField=input("Name of Text field name to look for City and Country Name: ")        
        geoField=input("Give a extra field name that you want to export: ")
        findCityCountryTweet(inputcsvfile,indexField,geoField,searchField,outputCsv)
    elif cityCountryRes==3:
        inputcsvfile=input("Provide Csv file that contains text: ")
        outputCsv=input("Give a Csv Output File Name: ") 
        fieldList=input("List the field names as ['x','y','z'] to be exported : ")
        dp.simplifyFindCityCountryTweet(inputcsvfile,fieldList,outputCsv)        
        
    elif cityCountryRes==4:
        inputcsvfile=input("Provide Csv file: ")
        outputCsv=input("Give a Csv Output File Name: ") 
        mergeFieldList=input("List the field names as ['x','y','z'] to be merged : ")     
        dp.mergeField(inputcsvfile,mergeFieldList,outputCsv)
        
    elif cityCountryRes==5:
        inputcsvfile1=input("Provide Csv file-1(source): ")
        inputcsvfile2=input("Provide Csv file-2(Target): ")
        outputCsv=input("Give a Csv Output file Name: ") 
        key=input("Provide the field name to be used as primary key: ") 
        rule=input("How the join will be performed such as 'inner','outer': ")     
        dp.JoinCSV(inputcsvfile1,inputcsvfile2,key,rule,outputCsv)
    elif cityCountryRes==6:
        print ('***please note: the empty cell will be replaced with "null" word and their sensitivity value will be 0\n')
        inputcsvfile=input("Provide Csv file to calculate analysis: ")        
        outputCsv=input("Give a Csv Output file Name: ") 
        text=input("Provide the field name to be used for sentiment analysis: ")           
        analysis.sentiment(inputcsvfile,outputCsv,text)      
    else:          
        pass