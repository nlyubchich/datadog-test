from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def solr(request):
    return HttpResponse(
        requests.get(
            'http://localhost:8983/solr/techproducts/select?q=inStock:false&wt=json&fl=id,name'
        ).text
    )
