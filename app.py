# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import streamlit as st
import pandas
import pickle

data = pickle.load(open('data_new.pkl','rb'))
similarities = pickle.load(open('similarity_git.pkl','rb'))



def movies_recommendation(movie_nme):

  print('Hey!! Gyus, Checkout these Amazing Movies')
  print(' ')
  index = data[data['title']== movie_nme].index[0]
  similar_content = sorted(list(enumerate(similarities[index])),reverse = True , key = lambda x: x[-1])

  recommend_hotels =[]
  for i,j in similar_content[1:6]:
    recommend_hotels.append(data['title'][i])
        
  return (recommend_hotels)


def poster_file(movie_name):
    url = "https://streaming-availability.p.rapidapi.com/v2/search/title"
    
    querystring = {"title":movie_name,"country":"us"}
    
    headers = {
    	"X-RapidAPI-Key": "8a00eb7337mshf8a2d52e86cf87cp12435fjsnc093d6aa0f8f",
    	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    
    output= response.json()
    
    poster = output['result'][0]['posterURLs']['original']
    #for i in (output['result']):
      #if i['title']== movie_name :
        #poster.append(i['posterURLs']['original'])
        #break
    return poster


st.title('Netflix Movies Recommendation System')
option = st.selectbox(
        'Movie List',
        data['title'].unique())
    
    
if st.button('Recommend'):
        recommendation = movies_recommendation(option)
        for i in recommendation :
            st.write(i)
            #image = Image.open(poster_file(i))
            st.image(poster_file(i))

