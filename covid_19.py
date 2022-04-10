# Mashal Buhamad 2020
# Covid-19 Kuwait statistics 2020
# Based on offical numbers by Ministry Of Health Kuwait
# This was coded during Kuwait lockdown due to covid-19
# I hope others find it helpful.

from time import *
from urllib.request import urlopen
import time 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import pandas as pd
import datetime
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def kuwait():
    str1='data-to='                             #String to look for
    link = "https://corona.e.gov.kw"            #Kuwait Covid-19 offical site
    f = urlopen(link)
    myfile = f.read()
    site=(str(myfile))
    index = site.find(str1)                     #search
    terminate = site.find('\"',index+9)
    number = site[index+9:terminate]
    index2=site.find(str1,index+13)
    terminate = site.find('\"',index2+9)
    treatment=site[index2+9:terminate]
    index3=site.find(str1,index2+13)
    terminate = site.find('\"',index3+9)
    critial=site[index3+9:terminate]
    index4=site.find(str1,index3+11)
    terminate = site.find('\"',index4+9)
    death=site[index4+9:terminate]
    list = [number,treatment,critial,death]
#    r = open("covid_19_data.txt","r")
#    dt=str(datetime.datetime.now())[0:10]

    for x in f:
       if x[0:10] == df:
          f = open("covid_19_data.txt","a")
          f.write(str(datetime.datetime.now()))
          f.write("\n")
          f.write('New cases:' + number +'-' 'At Hospital:'+treatment+'-'+'critical:'+critial + '-' + 'Death:'+death+'\n')
          f.close()
    return (list)

def graph():
    list=kuwait()
    number = [int(list[0]), int(list[1]), int(list[0])-(int(list[1])+int(list[3])), int(list[2]), int(list[3])]
    s = pd.Series([int(list[0]), int(list[1]), int(list[0])-(int(list[1])+int(list[3])), int(list[2]), int(list[3])], 
    index = ['Case', 'At Hospital', 'Cured', 'Critical', 'Death'])
    ax = plt.gca()
    ax.tick_params(axis='x', colors='blue')
    ax.tick_params(axis='y', colors='blue')

    plt.title('Covid-19 Kuwait, By: Mashal Buhamad')
    plt.bar([0,1,2,3,4],number, color='rbgrr',width=.3)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.xticks([0,1,2,3,4], ('Case', 'At Hospital', 'Cured', 'Critical', 'Death'))
    plt.show()
list = kuwait()
recov = int(list[0])-(int(list[1])+int(list[3]))
print ("- Number of registred corona cases in Kuwait is...............:",list[0])
print ("- Number of people getting treatment at hospitals in Kuwait is:",list[1])
print ("- Number of people at intensive care is.......................:",list[2])
print ("- Number of death due to cornoa is............................:",list[3], "...Death %:",str((int(list[3])/int(list[0]))*100)[0:4]+"%")
print ("- Number of recovard from cornoa in Kuwait is.................:", recov, ".Recovary %:",str((recov/int(list[0]))*100)[0:5]+"%")

graph()
