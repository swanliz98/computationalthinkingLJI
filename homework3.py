# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:39:08 2019

@author: jtse
"""

#1

import time
from bs4 import BeautifulSoup
import requests


pullman = 'https://www.yelp.com/biz/pullman-bar-and-diner-iowa-city'
laregia = 'https://www.yelp.com/biz/la-regia-taqueria-iowa-city'
def getreviews(giveurl):
    all_reviews = ''
    url = ''
    numreviews = 80
    for num in range(0,numreviews,20):
        url = f'{giveurl}?start={num}'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        plist = soup.find_all('p', class_ = 'lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_')
        for p in plist:
            all_reviews = all_reviews + ' ' + p.text
        time.sleep(2)
    return all_reviews

#Lecture 6 functions to clean up the reviews
def doc_to_frequencies(doc):
    myDict = {}
    stop_words = ['iowa','city','food','good','great','a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
    for word in doc:
        if word in stop_words:
            continue
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def remove_punc(words):
    for i in range(len(words)):
        words[i] = words[i].replace(',','')
        words[i] = words[i].replace('.','')
        words[i] = words[i].replace(';','')
        words[i] = words[i].replace(':','')
        words[i] = words[i].replace('(','')
        words[i] = words[i].replace(')','')
        words[i] = words[i].replace('"','')
    return words 

def top_k(freqs, k):
    top = []
    for i in range(k):
        mfreq = 0
        mkey = 0
        for key in freqs:
            if mfreq < freqs[key]:
                mfreq = freqs[key]
                mkey = key
        top.append([mkey, mfreq])
        del(freqs[mkey]) 
    return top

#Running the program
#print(top_k(doc_to_frequencies(remove_punc(getreviews(pullman)))))
print(remove_punc(getreviews(pullman)))