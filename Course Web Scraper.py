# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:23:54 2019

@author: jtse
"""
import time
from bs4 import BeautifulSoup
import requests

link = ''
def getdesc(key, value):
    url = f'https://myui.uiowa.edu/my-ui/courses/dashboard.page?q.sectionNumber=&q.startTime=&q.endTime=&q.courseSubject={key}&q.genEd=&q.sessionId=79&q.courseNumber={value}&q.learningCenter=&q.instructors=&q.keywords=&showResults=1'
    response = requests.get(url)
    html_doc = response.text
    text = BeautifulSoup(html_doc, 'lxml')
    atag = text.find_all('a', class_ = 'text-underline')[0]
    link = atag.get('href')
    newurl = 'https://myui.uiowa.edu' + link
    newresponse = requests.get(newurl)
    newhtml_doc = response.text
    newtext = BeautifulSoup(newhtml_doc, 'lxml')
    hours = newtext.find_all('div', class_ = 'col-md-3')[0]
    description = newtext.find_all('p')[0]
    prereqs = newtext.find_all('div', class_ = 'col-md-10', id_ = 'prerequisites')[0]
    reqs = newtext.find_all('div', class_ = 'col-md-10', id_ = 'requirements')[0]
    restrictions = newtext.find_all('div', class_ = 'col-md-10', id_ = 'requirements')[0]
    return text
dict = {'STAT':2010, 'MATH':1550} 

list = []
for key in dict.keys():
    list.append(getdesc(key, dict.get(key)))

print(list)


    
    