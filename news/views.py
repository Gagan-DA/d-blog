from django.shortcuts import render
import requests;

def getNews(request,cat):
    apiKey="d5beca6eb7944b4aa1c4bc0233907e03";
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+apiKey+"&category="+cat;
    try:
        data=requests.get(url)
        result=data.json()
        articles=result['articles']
    except Exception as e:
        print("Error in code"+e)
    return render(request,'news.html',{'articles':articles,'n':None})

