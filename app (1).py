#!/usr/bin/env python
# coding: utf-8

# In[3]:
from flask import *  
import pandas as pd
from datetime import datetime
import os,csv
now=datetime.now()
from report import *

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
        
        f = open(f2.filename,'rt')
        reader = csv.reader(f)

#once contents are available, I then put them in a list
        csv_list = []
        for l in reader:
            csv_list.append(l)
        f.close()
#now pandas has no problem getting into a df
        data2 = pd.DataFrame(csv_list)
        data2.drop([0,1],inplace=True)
        data2.columns=data2.iloc[0]
        data2=data2[['Tittel','Refnr.']]
        
        data2['Refnr.'].fillna(0,inplace=True)
        
       # data2=pd.read_csv(f2.filename,encoding='iso-8859-1')
        #data['codatetime']= [data['codatetime'][i][:10] for i in range(len(data['codatetime']))]
        
        #data2['Tittel']=data2['Tittel'].astype(str)
        #data2=data2[[7,6]]
        #data2.drop([0,1,2],axis=0,inplace=True)
        #data2.dropna()
        #data2[7]=data2[7].astype('int64')
        data2.columns=['Title','copfkcaseno']
        
        Report(data,data2,text)
        
        
      
        
        
        return render_template("success.html", name1 = f1.filename, name2 = f2.filename)  
    
    
if __name__ == '__main__':  
    app.run(port=5050)
  


# In[ ]:




