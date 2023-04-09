# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:38:12 2023

@author: 91703_0zbjuu
"""

import requests
from bs4 import BeautifulSoup
from pyhtml2pdf import converter
import os
os.chdir('Users\91703_0zbjuu\Downloads')

url="https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html"
url2="https://pythonnumericalmethods.berkeley.edu/notebooks/"
reqs= requests.get(url)
soup=BeautifulSoup(reqs.text, 'html.parser')

urls=[]
for link in soup.find_all('a'):
    ll=link.get('href')
    print(ll)
    try:
        if ll[-5:]=='.html':\
          converter.convert(url2+urll,ll[:5]+".pdf")
    except:
        pass
from glob import glob
import shtil

fol =["%.2d" % i for i in range(27)]
os.mkdir('0')

for i in fol:
    os.mkdir('0/'+1)
    fil=glob('chapter'+i+'*.pdf')
    for ii in fil:
        os.rename(ii, '0/'+i+'/'+ii)