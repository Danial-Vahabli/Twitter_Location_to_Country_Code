# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 23:37:58 2022

@author: User
"""

from statistics import mode
import pandas as pd
import numpy as np
import json
import time as time
import matplotlib.pyplot as plt
from alphabet_detector import AlphabetDetector

ad = AlphabetDetector()

def make_list(string):
    list =[]
    list1 = string.split(",")
    for i in range(len(list1)):
        list1[i] = list1[i].strip()
   # list2 = string.split()

    list.append(string)
    if len(list1)>1:
        list = list +list1
  #  if len(list2)>1:
  #      list = list +list2 
        

        
    return list

def make_list_space(string):
    list =[]
    list1 = string.split(" ")
    for i in range(len(list1)):
        list1[i] = list1[i].strip()
   # list2 = string.split()

    list.append(string)
    if len(list1)>1:
        list = list +list1
  #  if len(list2)>1:
  #      list = list +list2 
        

        
    return list


def dict_load(path):
    a_file = open("{0}.json".format(path), "r")

    dict_ = json.load(a_file)

    a_file.close()
    return  dict_



            
def search_dict_lower(string,country_dict_l,OG_names_dict_l,alt_name_dict_l,country_codes_l):
    search_results= []

    
    #check if the string has no "alphabetical charachter"
    temp_bol = False
    for i in range (len(string)):
        temp_bol = temp_bol + string[i].isalpha()
        
    if np.logical_not(temp_bol):
        search_results.append("Error")
        return search_results[-1]
            
            
    DICTS = [country_dict_l,OG_names_dict_l,alt_name_dict_l]
    
    string_list =  make_list(string) #separated by ,
    string_list_space =  make_list_space(string) #separated by " "

    for i in range (len(string_list)): #go through the list seperated by ","
        for j in range (len(DICTS)):
            try: 
                temp = DICTS[j]["{0}".format(string_list[i]).lower()]
                search_results.append(temp)
            except:
                continue
     
            
    if len(search_results) ==0:

        
        for i in range (len(string_list_space)): #go through the list seperated by " "
            for j in range (len(DICTS)):
                try: 
                    temp = DICTS[j]["{0}".format(string_list_space[i]).lower()]
                    search_results.append(temp)
                except:
                    continue
                
                
    if len(search_results) ==0:
    
        for i in range (len(string_list)): #Check wether the string contains the alpha 2 code or not
                try: 
                    temp = country_codes_l[string_list[i].upper()]
                    search_results.append(string_list[i].upper())
                    print("test",string_list[i])

                except:
                    continue
           
        for i in range (len(string_list_space)): #Check wether the string contains the alpha 2 code or not
                try: 
                    temp = country_codes_l[string_list_space[i].upper()]
                    search_results.append(string_list_space[i].upper())
                    print("test",string_list_space[i])
                except:
                    continue             
            
            
    if len(search_results) ==0: #see whether it has cyrillic or cjk charachters
        for i in range (len(string_list)):
                if ad.is_cyrillic(u"{0}".format(string_list[i]).lower()):
                    search_results.append("RU")
                if ad.is_cjk(u"{0}".format(string_list[i]).lower()):
                    search_results.append("JP")
    

            
    if len(search_results) ==0: #if didnt find anything else

        search_results.append("Error")
        
            
    return search_results[-1]
                

string = "New York"


#load dictionaries
country_dict =dict_load("Country_Names_dict")

OG_names_dict =dict_load("Original_Names_dict")

alt_name_dict = dict_load("Alternative_Names_exp")


#Case Insensitive
country_dict_l = {k.lower(): v for k, v in country_dict.items()}
OG_names_dict_l = {k.lower(): v for k, v in OG_names_dict.items()}
alt_name_dict_l = {k.lower(): v for k, v in alt_name_dict.items()}

#Alpha-2 code of countries
country_codes_l = {v: k for k, v in country_dict_l.items()}


Country_Code = search_dict_lower(string,country_dict_l,OG_names_dict_l,alt_name_dict_l,country_codes_l)

print(Country_Code)