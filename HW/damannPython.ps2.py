#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:04:25 2020

@author: taylor
"""

#importing modules
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
#import unicodedata

#the following is eerily similar to Patrick's solution to lab 4:

#creating a csv 
with open('damann.Python.ps2.csv', 'w') as f:
    
    #csv.DictWriter creates an object that operates like a regular reader
    #but maps the information in each row to a dict whose keys are given 
    #by the optional fieldnames parameter.  
  w = csv.DictWriter(f, fieldnames = ("title", "published", "issues", "signatures"))
    
  #writing a row with the fieldnames
  w.writeheader()
    
  #creating empty list of links to petitions
  links = []
   
  #using for loop to grab both page 1 and page 2
  for i in range(1, 3):
        # This line allows me to collect data from page=1 and page=2 using + str(i)
        web_address='https://petitions.whitehouse.gov/?page=' + str(i)
    #saving and loading in the correct web address
    #web_address = 'https://petitions.whitehouse.gov/petitions?page=2'
        web_page = urllib.request.urlopen(web_address)
  
    #reading contents of webpages with .read method
        soup = BeautifulSoup(web_page.read(), features="lxml")
  
    #using find_all to extract from several 'h3' tags
        link = soup.find_all('h3')
  
    #subsetting because the first few tags aren't of interest to us
        link = link[3::]
  
    #populating the links list
        links = links + link
  
    #extracting information from each link
  for i in links[0:len(links)]:
      
      #creating an empty dictionary of petition information
        petition = {}      
      
      #assigning the key "title" to several values that are the titles of the petitions
        petition["title"] = i.text
      
      #visiting each petition's url because it contains the info we need
        try:
            petition_page = urllib.request.urlopen("https://petitions.whitehouse.gov" + str(i.find('a')['href']))
            soup = BeautifulSoup(petition_page.read(), features = 'lxml')
      
      #telling python to rally if there is an error
        except urllib.error.URLError:
            continue
    
      #assigning the key "published" to several values that are the dates the petitions were published
        try:
            petition['published'] = soup.find('h4', class_ = 'petition-attribution').get_text()
            
            #replace the first few words in the date keys with a regex
            #this regex removes all words before "on " and replaces them with nothing
            petition['published'] = re.sub(r"^.+?on ", "", petition['published'])
      
      #telling python to persevere if there is an error  
        except AttributeError:
            petition['published'] = 'NA'
          
      #assigning the key "issues" to several values that are the issue tags     
        try:
            petition["issues"] = soup.find('div', class_ = 'content').find_all('h6')
            ##Ben, I wasn't able to clean up the issues column. I am comfortable with regexs,
            ##but for some reason petition["issues"] isn't saving as a string
            ##How would you go about cleaning this column?
            
      #keep calm and carry on, python  
        except AttributeError: 
            petition['issues'] = 'NA'
       
      #you know what I'm doing at this point 
        try:
            petition['signatures'] = soup.find('span', class_ = 'signatures-number').get_text()
        except AttributeError:
            petition['signatures'] = 'NA'
      
      #FINALLY we tell python to write it up
      #technically we are writing the values in our dictionary petition and fieldname keys to file w
        w.writerow(petition)        