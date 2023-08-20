#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request


# In[2]:


driver = webdriver.Chrome()


# In[3]:


#url 입력

url = 'https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do'
driver.get(url)
time.sleep(1)


# In[19]:


res = req.urlopen(url)
soup= BeautifulSoup(res,'html.parser')
body = soup.find('tbody') 
items = body.find_all('tr') #표 안에 있는 항목 가져오기


# In[20]:


information=[]
for i in range(1,5): #1~5페이지 까지 크롤링
    for item in items: 
        a=item.text[1:-14].split('\n')
        information.append(a[:9])
    css = f'#paging > div > a:nth-child({i})'
    sample = driver.find_element(By.CSS_SELECTOR,css) 
    sample.click() 


# In[21]:


import pandas as pd
df = pd.DataFrame(information, 
                  columns= ['지역','주택구분', '분양/임대','주택명', '시공사','문의처','모집공고일','청약기간','당첨자발표'])
df


# In[22]:


import seaborn as sns 
plt.rc('font',family='Malgun Gothic')


# In[24]:


sns.countplot(data = df, x='지역')

