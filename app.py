#!/usr/bin/env python
# coding: utf-8

# In[28]:


from flask import *  
import pandas as pd
from datetime import datetime
import os
now=datetime.now()

app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        date_time = now.strftime("%d.%m.%Y")
        f1 = request.files['file1']  
        f2 = request.files['file2'] 
        text = request.form['text']

        f1.save(f1.filename)
        f2.save(f2.filename) 
        data=pd.read_csv(f1.filename,encoding='Latin-1')
        data2=pd.read_csv(f2.filename,encoding='iso-8859-1')
        data['codatetime']= [data['codatetime'][i][:10] for i in range(len(data['codatetime']))]
        
        #data2['Tittel']=data2['Tittel'].astype(str)
        #data2=data2[[7,6]]
        #data2.drop([0,1,2],axis=0,inplace=True)
        #data2.dropna()
        #data2[7]=data2[7].astype('int64')
        data2.columns=['Title','copfkcaseno']
        
        
        Subset=['&nbsp;','<p>','</p>']

        for i in range(len(data['cobody'])):
        
            data['cobody'][i]=data['cobody'][i].replace('&nbsp;',' ')
            data['cobody'][i]=data['cobody'][i].replace('<p>','')
            data['cobody'][i]=data['cobody'][i].replace('</p>','')
            if '<strong>' in  data['cobody'][i]:
                
                data['cobody'][i]=data['cobody'][i].replace(data['cobody'][i][data['cobody'][i].index('<strong>'):],'')
        
        today_rahul=data[(data['codatetime']==date_time) & (data['coansvarlig']==text)]
    
        d = {'cokunde': 'first', 'cobody': 'sum', 'coansvarlig': 'first', 'codatetime':'first'}

        Rahul_Case=today_rahul.groupby('copfkcaseno',as_index=False).aggregate(d).reindex(columns=today_rahul.columns)
        Rahul_Case=Rahul_Case.merge(data2,on='copfkcaseno',how='inner')
        
        Rahul_Case.set_index(['copfkcaseno','coansvarlig','cokunde','Title','cobody','codatetime'],inplace=True)
        Rahul_Case.reset_index(inplace=True)
        
        Rahul_Case.columns=['Case ID','Person Incharge','Shop','Query','Answer','Date']
        
        Rahul_Case.to_excel('sheet.xlsx')
        #save_path = r"C:/Users/Karan"
        
        completeName = os.path.join(r'C:\Users\Karan\sheet1.xls')  
        Rahul_Case.to_excel(completeName)

        
        
        return render_template("success.html", name1 = f1.filename, name2 = f2.filename)  
    
    
if __name__ == '__main__':  
    app.run(port=5050)
  

