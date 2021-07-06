import datetime
from django.db import models
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
import json, urllib.request
import ssl



class Data(models.Model):
    
    address = models.CharField(max_length=200, default="none")
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
         verbose_name = "Data"
 
    



    




    
