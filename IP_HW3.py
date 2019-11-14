# -*- coding: utf-8 -*-
"""
HW3
@author: Isaac Perrilles
"""
from bs4 import BeautifulSoup
import requests
import time

def Yelp_Pages(page):
    
    if(page==0):
        page = ""
    elif(page==1):
        page = "?start=20"
            
    Pullman = f'https://www.yelp.com/biz/pullman-bar-and-diner-iowa-city{page}'
    
    Presponse = requests.get(Pullman)
    
    Pullman_doc = Presponse.text
    
    P_soup = BeautifulSoup(Pullman_doc, "lxml")
        
    P_tag = P_soup.find_all('p', class_='lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_')[0]

    time.sleep(2)
    
    return P_tag.text

    Taqueria = f'https://www.yelp.com/biz/la-regia-taqueria-iowa-city{page}'
    
    Tresponse = requests.get(Taqueria)
    Tanqueria_doc = Tresponse.text
    T_soup = BeautifulSoup(Tanqueria_doc, "lxml")
    T_tag = T_soup.find_all('p', class_='lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_')[0]
    time.sleep(2)
    return T_tag.text

one = Yelp_Pages(0)
print(one)
