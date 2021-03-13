# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:38:16 2020

@author: intel
"""

import requests
from bs4 import BeautifulSoup as bs
import re
url1 = "https://www.tripadvisor.in/Hotel_Review-g551613-d250426-Reviews"
url2 = "-Hotel_de_France-St_Helier_Jersey_Channel_Islands.html"

reviews=[]
ratings = []
title = []
date = []
for i in range(0,2000,5):
    if i == 0:
        base_url = url1+url2
    else:
        base_url = url1+"-or"+str(i)+url2
    response = requests.get(base_url)
    soup = bs(response.content,"html.parser")
    
    # scrap reviews
    temp = soup.findAll("q",attrs={"class","IRsGHoPm"})
    for j in range(len(temp)):
        reviews.append(str(j)+" "+temp[j].text) 
    
    # scrap ratings
    for a in soup.findAll("div",attrs={"class","nf9vGX55"}):
        for rate in a.findAll("span"):
            ratings.append(rate)
        
    # scrap date of review
    for b in soup.findAll("div",attrs={"class","_2fxQ4TOx"}):
        date.append(b.text)
        
ratings[:4]
int(str(ratings[0])[37:-10])
rate = ratings[:10]

# define functions for mapping to clean data

def get_rate(arr):
    return int(str(arr)[37:-10])

#def get_date(arr):
#    return str(arr)[15:]

def get_review(arr):
    return arr[2:]

rates_in_int = map(get_rate, ratings)
ratings = []
for i in rates_in_int:
    ratings.append(i)

ratings[:10]        
rev = map(get_review, reviews)
reviews = []
for i in rev:
    reviews.append(i)
    reviews[0][2:]
    
reviews[3]
import pandas as pd
rev={"reviews" : reviews}

reviews_hotel=pd.DataFrame(rev)
reviews_hotel.to_csv("reviews_hotel.csv")

data={"reviews" : reviews,
      "ratings": ratings}
final=pd.DataFrame(data)
final.to_csv("reviews_ratings_hotel.csv")
