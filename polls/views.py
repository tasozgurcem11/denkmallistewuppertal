from django.http import HttpResponse, HttpResponseRedirect, request # noqa: 401
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Data
import os
import requests
from bs4 import BeautifulSoup
import csv
import urllib.request, json
from urllib.parse import quote        
import ssl
import logging

def entrance(request):
    return render(request, "polls/entrance.html")

def impressum(request):
    return render(request, "polls/impressum.html")

def datenschutz(request):
    return render(request, "polls/datenschutz.html")
    
def home(request):
    context = {} 
    if request.method == 'POST':
        
        address = str(request.POST.get("address"))

        o_ref = Data(address = address)
        o_ref.save() 

    return render(request, "polls/home.html", context)

def test(request):
    return render(request, "polls/test.html")



def faq(request):
    return render(request, "polls/faq.html")

def form(request):
    context = {} 
    if request.method == 'POST':
    
        address1 = str(request.POST.get("address"))
        address2 = str(request.POST.get("address2"))

        if address1 != "":
            address = address1
        
        else:
            address = address2

        print(address)

        o_ref = Data(address = address)
        o_ref.save() 
        context1 = ssl._create_unverified_context()

        location_api = "https://maps.googleapis.com/maps/api/geocode/json?address=" + quote(address) + "&key=AIzaSyCQDUvwiU-YRg38P7J1UGfoE-yN-y1bi9c"
        with urllib.request.urlopen(location_api, context=context1) as url:
                                print(location_api)
                                data_raw = json.loads(url.read().decode())
                                print(data_raw["status"])
                                if "ZERO" in data_raw["status"]:
                                    print(data_raw["status"])
                                else:
                                    house_number = data_raw["results"][0]["address_components"][0]["long_name"]
                                    street_address = data_raw["results"][0]["address_components"][1]["long_name"]
                                    
            
                                    street_address = str(street_address) + " " +str(house_number)

                                    print(street_address)

                                    monument_list = ["", "", "", "", "", "", ""]
                                    monument_list = monumentFunction2(street_address)
                                    print(monument_list)
                                    if "♠" in monument_list[5]:
                                        temp = monument_list[5].split("♠",2)
                                        monument_list[5] = temp[1]
                                    
                                    context["foto"] = "https:/" + monument_list[6] 
                                    context["lage"] = monument_list[0]
                                    context["bauzeit"] = monument_list[2]
                                    context["bezeichnung"] = monument_list[3]
                                    context["eingetragenseit"] = monument_list[5]
                                    context["nummer"] = monument_list[4]

        

       

        





    return render(request, "polls/home.html", context)

# 1)Deweerthstr. 19 
# 2)Deweerthstrasse 19 
# 3) Deweerthstraße 19 
# 4) Deweerthstr 19 
# 5)Deweerthstr . 19
            

def monumentFunction2(address):
    address = address.lower()
    print("cem address before: " + address)
    splited_address = address.split(" ")
    for item in splited_address:
                    item = item.lower()
                    if "str." in item:
                        item = item.replace("str.", "straße")
                    elif "str ." in item:
                        item = item.replace("str .", "straße")
                    elif "str" in item:
                        item = item.replace("str", "straße")

    print("cem address after: " + address)


    # if "str" in address and "straße" not in address :
    #     address = address.replace("str", "straße")
    #     print
    # elif "str." in address and "straße" not in address:
    #     address = address.replace("str.", "straße")
    # elif "strasse" in address and "straße" not in address:
    #     address = address.replace("strasse", "straße")
    # elif "str ." in address and "straße" not in address:
    #     address = address.replace("str .", "straße")
    


    
    monument_data = ["", "", "", "", "", "", ""]
    with open('data3.csv', 'r', newline='') as g:

        thereader = csv.reader(g)

        for line in thereader:


            
            if line[0].lower() == address.lower() and line[0] != "" :
                
                monument_data[0] = line[0]
                monument_data[1] = line[0]
                monument_data[2] = line[1]
                monument_data[3] = line[2]
                monument_data[4] = line[3]
                monument_data[5] = line[6]
                monument_data[6] = line[4]
                
                
                break
            else:
                monument_data[0] = "kein Ergebnis"
                monument_data[1] = ""
                monument_data[2] = ""
                monument_data[3] = ""
                monument_data[4] = ""
                monument_data[5] = ""

    return monument_data

        
             



