# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:30:19 2020

@author: Karan
"""

# In[3]:
import pandas as pd
from datetime import datetime
import os,csv
now=datetime.now()

def Report(data,data2,text):
     date_time = now.strftime("%d.%m.%Y")
     data['codatetime']= [data['codatetime'][i][:10] for i in range(len(data['codatetime']))]
     Subset=['&nbsp;','<p>','</p>']
        #indexNames = data[data['cokunde'] == 'DataNova~Inhouse' ].index
        
        #for i in range(len(data['cokunde'])):
        #    if data['cokunde'] == 'DataNova~Inhouse':
        #        data.drop(i,axis=0,inplace=True)
            


     for i in range(len(data['cobody'])):
        
            data['cobody'][i]=data['cobody'][i].replace('&nbsp;',' ')
            data['cobody'][i]=data['cobody'][i].replace('<p>','')
            data['cobody'][i]=data['cobody'][i].replace('</p>','')
            data['cobody'][i]=data['cobody'][i].replace('</Br>','')
            data['cobody'][i]=data['cobody'][i].replace('</br>','')
            data['cobody'][i]=data['cobody'][i].replace('<br>','')
            data['cobody'][i]=data['cobody'][i].replace('<Br>','')
            data['cobody'][i]=data['cobody'][i].replace('<br/>','')
            if '<strong>' in  data['cobody'][i]:
                  
                    data['cobody'][i]=data['cobody'][i].replace(data['cobody'][i][data['cobody'][i].index('<strong>'):],'')
        
            today_rahul=data[(data['codatetime']==date_time) & (data['coansvarlig']==text)]
    
            d = {'cokunde': 'first', 'cobody': 'sum', 'coansvarlig': 'first', 'codatetime':'first'}

            Rahul_Case=today_rahul.groupby('copfkcaseno',as_index=False).aggregate(d).reindex(columns=today_rahul.columns)
            Rahul_Case=Rahul_Case.merge(data2,on='copfkcaseno',how='inner')
        
            Rahul_Case.set_index(['copfkcaseno','coansvarlig','cokunde','Title','cobody','codatetime'],inplace=True)
            Rahul_Case.reset_index(inplace=True)
        
            Rahul_Case.columns=['Case ID','Person Incharge','Shop','Query','Answer','Date']
        
            #Rahul_Case.to_excel('sheet.xlsx')
        #save_path = r"C:/Users/Karan"
        
            #completeName = os.path.join(r'C:\Users\Karan\sheet1.xls')  
           # Rahul_Case.to_excel(completeName)

        
        
    
    
  


# In[ ]:




