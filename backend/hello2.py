from flask import Flask
from flask_cors import CORS
from flask import request
import readData
app = Flask(__name__)
CORS(app)

import pandas as pd
import compute
import numpy as np
#####read data##################

#dt,d1,d2,d3,d4,d5=readData.read('./data/')

from scipy import stats
import json

import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import base64
import io 
from sklearn.preprocessing import Normalizer
print("data reading finished ")
def normalize(df):
    result = df.copy()
    result.iloc[:,:] = Normalizer(norm='l1').fit_transform(result)
    return result
################################
#####email data##################
#dt_email,d1_email,d2_email,d3_email,d4_email,d5_email=readData.read_email('./data/')
#print("email data read finished ")
email_dt_array = pd.Series() 
email_d1_array = pd.Series() 
email_d2_array = pd.Series() 
email_d3_array = pd.Series() 
email_d4_array = pd.Series() 
email_d5_array = pd.Series() 

phone_dt_array = pd.Series() 
phone_d1_array = pd.Series() 
phone_d2_array = pd.Series() 
phone_d3_array = pd.Series() 
phone_d4_array = pd.Series() 
phone_d5_array = pd.Series() 

################################
#####phone data##################
#dt_phone,d1_phone,d2_phone,d3_phone,d4_phone,d5_phone,phone_s_dict,phone_t_dict,phone_year_dict=readData.read_phone('./data/')
print("phone data read finished ")

print("finish")
#####email data##################

print("finish email")

################################
#####procurement data##################

dt_procu, d1_procu ,d2_procu,d3_procu,d4_procu,d5_procu,procu_dict=readData.read_procurement('./data/')
print("finish procurement")
################################

dt_travel, d1_travel ,d2_travel,d3_travel,d4_travel,d5_travel,procu_travel=readData.read_travel('./data/')
################################

demojson=compute.createDemojson('./data/')



@app.route('/')
def hello_world():
    return 'Hello, World!'
    
    
    
#################################################phone analysis################################################    
@app.route("/phoneanalysis")
def phone_analysis():
    
    print(request)
    #maxv=request.form['valuemax']
    minv = request.args.get('valuemin')
    maxv = request.args.get('valuemax')
  #  mint = request.args.get('mint')
  #  maxt = request.args.get('maxt')
   # label = request.args.get('label')
    print(minv,maxv)
    dt_phone,d1_phone,d2_phone,d3_phone,d4_phone,d5_phone,phone_s_dict,phone_t_dict,phone_year_dict=readData.read_phone('./data/')
    dt_rs=dt_phone['Source'].value_counts().values
    d1_rs=d1_phone['Source'].value_counts().values
    d2_rs=d2_phone['Source'].value_counts().values
    d3_rs=d3_phone['Source'].value_counts().values
    d4_rs=d4_phone['Source'].value_counts().values
    d5_rs=d5_phone['Source'].value_counts().values

   # print(dt_rs,d1_rs,d2_rs,d3_rs,d4_rs,d5_rs)

    dt_rs1=phone_s_dict.copy()
   # dt_rsnew=compute.createjson(dt_rs1,dt_rs)
    dt_rsnew,dtarray=compute.createjson(dt_rs1,dt_rs)
    d1_rs1=phone_s_dict.copy()
    #d1_rsnew=compute.createjson(d1_rs1,d1_rs)
    d1_rsnew,d1array=compute.createjson(d1_rs1,d1_rs)
    d2_rs1=phone_s_dict.copy()
    d2_rsnew,d2array=compute.createjson(d2_rs1,d2_rs)

    d3_rs1=phone_s_dict.copy()
    d3_rsnew,d3array=compute.createjson(d3_rs1,d3_rs)

    d4_rs1=phone_s_dict.copy()
    d4_rsnew,d4array=compute.createjson(d4_rs1,d4_rs)

    d5_rs1=phone_s_dict.copy()
    d5_rsnew,d5array=compute.createjson(d5_rs1,d5_rs)
    
    result=list()
    result.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d5array),3))

    dt_rt=dt_phone['Target'].value_counts().values
    d1_rt=d1_phone['Target'].value_counts().values
    d2_rt=d2_phone['Target'].value_counts().values
    d3_rt=d3_phone['Target'].value_counts().values
    d4_rt=d4_phone['Target'].value_counts().values
    d5_rt=d5_phone['Target'].value_counts().values
    dt_rt1=phone_t_dict.copy()
    dt_rtnew,dtarraynew=compute.createjson(dt_rt1,dt_rt)

    d1_rt1=phone_t_dict.copy()
    d1_rtnew,d1arraynew=compute.createjson(d1_rt1,d1_rt)

    d2_rt1=phone_t_dict.copy()
    d2_rtnew,d2arraynew=compute.createjson(d2_rt1,d2_rt)

    d3_rt1=phone_t_dict.copy()
    d3_rtnew,d3arraynew=compute.createjson(d3_rt1,d3_rt)

    d4_rt1=phone_t_dict.copy()
    d4_rtnew,d4arraynew=compute.createjson(d4_rt1,d4_rt)

    d5_rt1=phone_t_dict.copy()
    d5_rtnew,d5arraynew=compute.createjson(d5_rt1,d5_rt)

    result.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3))
 
    global phone_dt_array
    global phone_d1_array
    global phone_d2_array
    global phone_d3_array
    global phone_d4_array
    global phone_d5_array 
    
    phone_dt_dict=phone_year_dict.copy()

    phone_dt_dictnew,arr=compute.createjsonYear_addis(phone_dt_dict, dt_phone)
    phone_dt_array=arr
    phone_d1_dict=phone_year_dict.copy()

    phone_d1_dictnew,arr1=compute.createjsonYear_addis(phone_d1_dict, d1_phone)
    phone_d1_array=arr1
    phone_d2_dict=phone_year_dict.copy()

    phone_d2_dictnew,arr2=compute.createjsonYear_addis(phone_d2_dict, d2_phone)
    phone_d2_array=arr2
    phone_d3_dict=phone_year_dict.copy()

    phone_d3_dictnew,arr3=compute.createjsonYear_addis(phone_d3_dict, d3_phone)
    phone_d3_array=arr3
    phone_d4_dict=phone_year_dict.copy()

    phone_d4_dictnew,arr4=compute.createjsonYear_addis(phone_d4_dict, d4_phone)
    phone_d4_array=arr4
    phone_d5_dict=phone_year_dict.copy()
    
    phone_d5_dictnew,arr5=compute.createjsonYear_addis(phone_d5_dict, d5_phone)
    phone_d5_array=arr5
    result.append(round(stats.wasserstein_distance(phone_dt_array,phone_d1_array),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array,phone_d2_array),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array,phone_d3_array),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array,phone_d4_array),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array,phone_d5_array),3))  
    result=pd.Series(result)



    return dt_rsnew+"&&"+d1_rsnew+"&&"+d2_rsnew+"&&"+d3_rsnew+"&&"+d4_rsnew+"&&"+d5_rsnew+"&&"+dt_rtnew+"&&"+d1_rtnew+"&&"+d2_rtnew+"&&"+d3_rtnew+"&&"+d4_rtnew+"&&"+d5_rtnew+"&&"+phone_dt_dictnew+"&&"+phone_d1_dictnew+"&&"+phone_d2_dictnew+"&&"+phone_d3_dictnew+"&&"+phone_d4_dictnew+"&&"+phone_d5_dictnew+"&&"+result.to_json(orient='records')


#################################################email analysis################################################  
#################################################phone analysis################################################    
@app.route("/phoneanalysis1")
def phone_analysis1():
    
    print(request)
    #maxv=request.form['valuemax']
    minv =int( request.args.get('valuemin')[1:])
    maxv = int(request.args.get('valuemax')[1:])
  #  mint = request.args.get('mint')
  #  maxt = request.args.get('maxt')
   # label = request.args.get('label')
    print(minv,maxv)
    dt_phone,d1_phone,d2_phone,d3_phone,d4_phone,d5_phone,phone_s_dict,phone_t_dict,phone_year_dict=readData.read_phone('./data/')
    dt_rs=dt_phone['Source'][(dt_phone['Time']>=minv)&(dt_phone['Time']<=maxv)].value_counts().values
    d1_rs=d1_phone['Source'][(d1_phone['Time']>=minv)&(d1_phone['Time']<=maxv)].value_counts().values
    d2_rs=d2_phone['Source'][(d2_phone['Time']>=minv)&(d2_phone['Time']<=maxv)].value_counts().values
    d3_rs=d3_phone['Source'][(d3_phone['Time']>=minv)&(d3_phone['Time']<=maxv)].value_counts().values
    d4_rs=d4_phone['Source'][(d4_phone['Time']>=minv)&(d4_phone['Time']<=maxv)].value_counts().values
    d5_rs=d5_phone['Source'][(d5_phone['Time']>=minv)&(d5_phone['Time']<=maxv)].value_counts().values

   # print(dt_rs,d1_rs,d2_rs,d3_rs,d4_rs,d5_rs)

    dt_rs1=phone_s_dict.copy()
  #  dt_rsnew=compute.createjson(dt_rs1,dt_rs)

    d1_rs1=phone_s_dict.copy()
   # d1_rsnew=compute.createjson(d1_rs1,d1_rs)

    d2_rs1=phone_s_dict.copy()
  #  d2_rsnew=compute.createjson(d2_rs1,d2_rs)

    d3_rs1=phone_s_dict.copy()
  #  d3_rsnew=compute.createjson(d3_rs1,d3_rs)

    d4_rs1=phone_s_dict.copy()
  #  d4_rsnew=compute.createjson(d4_rs1,d4_rs)

    d5_rs1=phone_s_dict.copy()
  #  d5_rsnew=compute.createjson(d5_rs1,d5_rs)

    
    
    dt_rsnew,dtarray=compute.createjson_adddis(dt_rs1,dt_rs)
   # print(dtarray)

 
    d1_rsnew,d1array=compute.createjson_adddis(d1_rs1,d1_rs)


    d2_rsnew,d2array=compute.createjson_adddis(d2_rs1,d2_rs)


    d3_rsnew,d3array=compute.createjson_adddis(d3_rs1,d3_rs)

   
    d4_rsnew,d4array=compute.createjson_adddis(d4_rs1,d4_rs)

    
    d5_rsnew,d5array=compute.createjson_adddis(d5_rs1,d5_rs)
    result=list()
    result.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d5array),3))


    dt_rt=dt_phone['Target'][(dt_phone['Time']>=minv)&(dt_phone['Time']<=maxv)].value_counts().values
    d1_rt=d1_phone['Target'][(d1_phone['Time']>=minv)&(d1_phone['Time']<=maxv)].value_counts().values
    d2_rt=d2_phone['Target'][(d2_phone['Time']>=minv)&(d2_phone['Time']<=maxv)].value_counts().values
    d3_rt=d3_phone['Target'][(d3_phone['Time']>=minv)&(d3_phone['Time']<=maxv)].value_counts().values
    d4_rt=d4_phone['Target'][(d4_phone['Time']>=minv)&(d4_phone['Time']<=maxv)].value_counts().values
    d5_rt=d5_phone['Target'][(d5_phone['Time']>=minv)&(d5_phone['Time']<=maxv)].value_counts().values
    dt_rt1=phone_t_dict.copy()
    dt_rtnew=compute.createjson(dt_rt1,dt_rt)

    d1_rt1=phone_t_dict.copy()
  #  d1_rtnew=compute.createjson(d1_rt1,d1_rt)

    d2_rt1=phone_t_dict.copy()
  #  d2_rtnew=compute.createjson(d2_rt1,d2_rt)

    d3_rt1=phone_t_dict.copy()
   # d3_rtnew=compute.createjson(d3_rt1,d3_rt)

    d4_rt1=phone_t_dict.copy()
   # d4_rtnew=compute.createjson(d4_rt1,d4_rt)

    d5_rt1=phone_t_dict.copy()
    #d5_rtnew=compute.createjson(d5_rt1,d5_rt)

    dt_rtnew,dtarraynew=compute.createjson_adddis(dt_rt1,dt_rt)

  
    d1_rtnew,d1arraynew=compute.createjson_adddis(d1_rt1,d1_rt)

  
    d2_rtnew,d2arraynew=compute.createjson_adddis(d2_rt1,d2_rt)


    d3_rtnew,d3arraynew=compute.createjson_adddis(d3_rt1,d3_rt)

    d4_rtnew,d4arraynew=compute.createjson_adddis(d4_rt1,d4_rt)

  
    d5_rtnew,d5arraynew=compute.createjson_adddis(d5_rt1,d5_rt)
    result.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3)) 
    
    if(minv==0):
     minv=0
    else :
     minv=minv-1
  #  print(len(email_dt_array[minv:(maxv-1)]))
  #  print(len(email_dt_array))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d1_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d2_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d3_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d4_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d5_array[minv:(maxv-1)]),3))
    result=pd.Series(result)  
    #print(result)    




    return dt_rsnew+"&&"+d1_rsnew+"&&"+d2_rsnew+"&&"+d3_rsnew+"&&"+d4_rsnew+"&&"+d5_rsnew+"&&"+dt_rtnew+"&&"+d1_rtnew+"&&"+d2_rtnew+"&&"+d3_rtnew+"&&"+d4_rtnew+"&&"+d5_rtnew+"&&"+result.to_json(orient='records')
      

#################################################email analysis################################################     
@app.route("/emailanalysis")
def email_analysis():
    print(request)
    dt_email, d1_email ,d2_email,d3_email,d4_email,d5_email,email_s_dict,email_t_dict,email_year_dict=readData.read_email('./data/')
    #time = request.args.get('time')
  #  mint = request.args.get('mint')
  #  maxt = request.args.get('maxt')
   # label = request.args.get('label')
   # print(time,mint,maxt,label)

    dt_rs=dt_email['Source'].value_counts().values
    d1_rs=d1_email['Source'].value_counts().values
    d2_rs=d2_email['Source'].value_counts().values
    d3_rs=d3_email['Source'].value_counts().values
    d4_rs=d4_email['Source'].value_counts().values
    d5_rs=d5_email['Source'].value_counts().values

    #print(dt_rs,d1_rs,d2_rs,d3_rs,d4_rs,d5_rs)

    dt_rs1=email_s_dict.copy()
    dt_rsnew,dtarray=compute.createjson(dt_rs1,dt_rs)

    d1_rs1=email_s_dict.copy()
    d1_rsnew,d1array=compute.createjson(d1_rs1,d1_rs)

    d2_rs1=email_s_dict.copy()
    d2_rsnew,d2array=compute.createjson(d2_rs1,d2_rs)

    d3_rs1=email_s_dict.copy()
    d3_rsnew,d3array=compute.createjson(d3_rs1,d3_rs)

    d4_rs1=email_s_dict.copy()
    d4_rsnew,d4array=compute.createjson(d4_rs1,d4_rs)

    d5_rs1=email_s_dict.copy()
    d5_rsnew,d5array=compute.createjson(d5_rs1,d5_rs)

    result=list()
    result.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d5array),3))

    dt_rt=dt_email['Target'].value_counts().values
    d1_rt=d1_email['Target'].value_counts().values
    d2_rt=d2_email['Target'].value_counts().values
    d3_rt=d3_email['Target'].value_counts().values
    d4_rt=d4_email['Target'].value_counts().values
    d5_rt=d5_email['Target'].value_counts().values
    dt_rt1=email_t_dict.copy()
    dt_rtnew,dtarraynew=compute.createjson(dt_rt1,dt_rt)

    d1_rt1=email_t_dict.copy()
    d1_rtnew,d1arraynew=compute.createjson(d1_rt1,d1_rt)

    d2_rt1=email_t_dict.copy()
    d2_rtnew,d2arraynew=compute.createjson(d2_rt1,d2_rt)

    d3_rt1=email_t_dict.copy()
    d3_rtnew,d3arraynew=compute.createjson(d3_rt1,d3_rt)

    d4_rt1=email_t_dict.copy()
    d4_rtnew,d4arraynew=compute.createjson(d4_rt1,d4_rt)

    d5_rt1=email_t_dict.copy()
    d5_rtnew,d5arraynew=compute.createjson(d5_rt1,d5_rt)
    


    result.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3))
    
    email_dt_dict=email_year_dict.copy()

    email_dt_dictnew,arr=compute.createjsonYear_addis(email_dt_dict, dt_email)
    
    global email_dt_array
    global email_d1_array
    global email_d2_array
    global email_d3_array
    global email_d4_array
    global email_d5_array
    email_dt_array=arr
    
    
    email_d1_dict=email_year_dict.copy()

    email_d1_dictnew,arr1=compute.createjsonYear_addis(email_d1_dict, d1_email)
    email_d1_array=arr1
    email_d2_dict=email_year_dict.copy()

    email_d2_dictnew,arr2=compute.createjsonYear_addis(email_d2_dict, d2_email)
    email_d2_array=arr2
    email_d3_dict=email_year_dict.copy()

    email_d3_dictnew,arr3=compute.createjsonYear_addis(email_d3_dict, d3_email)
    email_d3_array=arr3
    email_d4_dict=email_year_dict.copy()

    email_d4_dictnew,arr4=compute.createjsonYear_addis(email_d4_dict, d4_email)
    email_d4_array=arr4
    email_d5_dict=email_year_dict.copy()

    email_d5_dictnew,arr5=compute.createjsonYear_addis(email_d5_dict, d5_email)
    email_d5_array=arr5
   # print("email finish analysis")
    #print(len(email_dt_array),len(email_d1_array),round(stats.wasserstein_distance(email_dt_array,email_d1_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d1_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d2_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d3_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d4_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d5_array),3))
    result=pd.Series(result)
   # print(result)
    return dt_rsnew+"&&"+d1_rsnew+"&&"+d2_rsnew+"&&"+d3_rsnew+"&&"+d4_rsnew+"&&"+d5_rsnew+"&&"+dt_rtnew+"&&"+d1_rtnew+"&&"+d2_rtnew+"&&"+d3_rtnew+"&&"+d4_rtnew+"&&"+d5_rtnew+"&&"+email_dt_dictnew+"&&"+email_d1_dictnew+"&&"+email_d2_dictnew+"&&"+email_d3_dictnew+"&&"+email_d4_dictnew+"&&"+email_d5_dictnew+"&&"+result.to_json(orient='records')

   
#################################################email analysis################################################     
@app.route("/emailanalysis1")
def email_analysis1():
    print(request)
    dt_email, d1_email ,d2_email,d3_email,d4_email,d5_email,email_s_dict,email_t_dict,email_year_dict=readData.read_email('./data/')
    #time = request.args.get('time')
  #  mint = request.args.get('mint')
  #  maxt = request.args.get('maxt')
   # label = request.args.get('label')
   # print(time,mint,maxt,label)
    minv =int( request.args.get('valuemin')[1:])
    maxv = int(request.args.get('valuemax')[1:])
    dt_rs=dt_email['Source'][(dt_email['Time']>=minv)&(dt_email['Time']<=maxv)].value_counts().values
    d1_rs=d1_email['Source'][(d1_email['Time']>=minv)&(d1_email['Time']<=maxv)].value_counts().values
    d2_rs=d2_email['Source'][(d2_email['Time']>=minv)&(d2_email['Time']<=maxv)].value_counts().values
    d3_rs=d3_email['Source'][(d3_email['Time']>=minv)&(d3_email['Time']<=maxv)].value_counts().values
    d4_rs=d4_email['Source'][(d4_email['Time']>=minv)&(d4_email['Time']<=maxv)].value_counts().values
    d5_rs=d5_email['Source'][(d5_email['Time']>=minv)&(d5_email['Time']<=maxv)].value_counts().values

  #  print(dt_rs,d1_rs,d2_rs,d3_rs,d4_rs,d5_rs)

    dt_rs1=email_s_dict.copy()
    dt_rsnew,dtarray=compute.createjson_adddis(dt_rs1,dt_rs)
   # print(dtarray)

    d1_rs1=email_s_dict.copy()
    d1_rsnew,d1array=compute.createjson_adddis(d1_rs1,d1_rs)

    d2_rs1=email_s_dict.copy()
    d2_rsnew,d2array=compute.createjson_adddis(d2_rs1,d2_rs)

    d3_rs1=email_s_dict.copy()
    d3_rsnew,d3array=compute.createjson_adddis(d3_rs1,d3_rs)

    d4_rs1=email_s_dict.copy()
    d4_rsnew,d4array=compute.createjson_adddis(d4_rs1,d4_rs)

    d5_rs1=email_s_dict.copy()
    d5_rsnew,d5array=compute.createjson_adddis(d5_rs1,d5_rs)
    result=list()
    result.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d5array),3))
    
    

    dt_rt=dt_email['Target'][(dt_email['Time']>=minv)&(dt_email['Time']<=maxv)].value_counts().values
    d1_rt=d1_email['Target'][(d1_email['Time']>=minv)&(d1_email['Time']<=maxv)].value_counts().values
    d2_rt=d2_email['Target'][(d2_email['Time']>=minv)&(d2_email['Time']<=maxv)].value_counts().values
    d3_rt=d3_email['Target'][(d3_email['Time']>=minv)&(d3_email['Time']<=maxv)].value_counts().values
    d4_rt=d4_email['Target'][(d4_email['Time']>=minv)&(d4_email['Time']<=maxv)].value_counts().values
    d5_rt=d5_email['Target'][(d5_email['Time']>=minv)&(d5_email['Time']<=maxv)].value_counts().values
    dt_rt1=email_t_dict.copy()
    dt_rtnew,dtarraynew=compute.createjson_adddis(dt_rt1,dt_rt)

    d1_rt1=email_t_dict.copy()
    d1_rtnew,d1arraynew=compute.createjson_adddis(d1_rt1,d1_rt)

    d2_rt1=email_t_dict.copy()
    d2_rtnew,d2arraynew=compute.createjson_adddis(d2_rt1,d2_rt)

    d3_rt1=email_t_dict.copy()
    d3_rtnew,d3arraynew=compute.createjson_adddis(d3_rt1,d3_rt)

    d4_rt1=email_t_dict.copy()
    d4_rtnew,d4arraynew=compute.createjson_adddis(d4_rt1,d4_rt)

    d5_rt1=email_t_dict.copy()
    d5_rtnew,d5arraynew=compute.createjson_adddis(d5_rt1,d5_rt)
    
    result.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3))
  #  print(result)
    if(minv==0):
     minv=0
    else :
     minv=minv-1
  #  print(len(email_dt_array[minv:(maxv-1)]))
  #  print(len(email_dt_array))
    result.append(round(stats.wasserstein_distance(email_dt_array[minv:(maxv-1)],email_d1_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(email_dt_array[minv:(maxv-1)],email_d2_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(email_dt_array[minv:(maxv-1)],email_d3_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(email_dt_array[minv:(maxv-1)],email_d4_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(email_dt_array[minv:(maxv-1)],email_d5_array[minv:(maxv-1)]),3))
    result=pd.Series(result)
    print("email finish analysis")


    return dt_rsnew+"&&"+d1_rsnew+"&&"+d2_rsnew+"&&"+d3_rsnew+"&&"+d4_rsnew+"&&"+d5_rsnew+"&&"+dt_rtnew+"&&"+d1_rtnew+"&&"+d2_rtnew+"&&"+d3_rtnew+"&&"+d4_rtnew+"&&"+d5_rtnew+"&&"+result.to_json(orient='records')
      
#################################################procurement analysis################################################     
@app.route("/procurementanalysis")
def procurement_analysis():  
    minv =int( request.args.get('valuemin')[1:])
    maxv = int(request.args.get('valuemax')[1:])
    procu_freq=list()
    procu_freq.append(len(dt_procu[(dt_procu['Time']>=minv)&(dt_procu['Time']<=maxv)]))
    procu_freq.append(len(d1_procu[(d1_procu['Time']>=minv)&(d1_procu['Time']<=maxv)]))
    procu_freq.append(len(d2_procu[(d2_procu['Time']>=minv)&(d2_procu['Time']<=maxv)]))
    procu_freq.append(len(d3_procu[(d3_procu['Time']>=minv)&(d3_procu['Time']<=maxv)]))
    procu_freq.append(len(d4_procu[(d4_procu['Time']>=minv)&(d4_procu['Time']<=maxv)]))
    procu_freq.append(len(d5_procu[(d5_procu['Time']>=minv)&(d5_procu['Time']<=maxv)]))
    procu_freq=pd.DataFrame(procu_freq)
    procu_freq.columns=["value"]
    procu_freq["index"]=["template","graph1","graph2","graph3","graph4","graph5"]
    
    procu_weight=list()
    procu_weight.append(int(sum(dt_procu[(dt_procu['Time']>=minv)&(dt_procu['Time']<=maxv)]['Weight'])))
    procu_weight.append(int(sum(d1_procu[(d1_procu['Time']>=minv)&(d1_procu['Time']<=maxv)]['Weight'])))
    procu_weight.append(int(sum(d2_procu[(d2_procu['Time']>=minv)&(d2_procu['Time']<=maxv)]['Weight'])))
    procu_weight.append(int(sum(d3_procu[(d3_procu['Time']>=minv)&(d3_procu['Time']<=maxv)]['Weight'])))
    procu_weight.append(int(sum(d4_procu[(d4_procu['Time']>=minv)&(d4_procu['Time']<=maxv)]['Weight'])))
    procu_weight.append(int(sum(d5_procu[(d5_procu['Time']>=minv)&(d5_procu['Time']<=maxv)]['Weight'])))
    procu_weight=pd.DataFrame(procu_weight)
    procu_weight.columns=["value"]
    procu_weight["index"]=["template","graph1","graph2","graph3","graph4","graph5"]

    return procu_freq.to_json(orient='records')+"&&"+procu_weight.to_json(orient='records')
    
    
    
    #[{"template":0},{"graph1":0},{"graph2":0},{"graph3":0},{"graph4":0},{"graph5":0}]
#################################################procurement analysis################################################     
#################################################procurement analysis################################################     
@app.route("/travelanalysis")
def travel_analysis():  
    minv =int( request.args.get('valuemin')[1:])
    maxv = int(request.args.get('valuemax')[1:])
    print(minv,maxv)
    dt_travel_s_freq,dt_travel_d_freq,ret,dt_s_arr,dt_d_arr=compute.createjsontravel(minv, maxv,dt_travel)
    d1_travel_s_freq,d1_travel_d_freq,re1,d1_s_arr,d1_d_arr=compute.createjsontravel(minv, maxv,d1_travel)
    d2_travel_s_freq,d2_travel_d_freq,re2,d2_s_arr,d2_d_arr=compute.createjsontravel(minv, maxv,d2_travel)
    d3_travel_s_freq,d3_travel_d_freq,re3,d3_s_arr,d3_d_arr=compute.createjsontravel(minv, maxv,d3_travel)
    d4_travel_s_freq,d4_travel_d_freq,re4,d4_s_arr,d4_d_arr=compute.createjsontravel(minv, maxv,d4_travel)
    d5_travel_s_freq,d5_travel_d_freq,re5,d5_s_arr,d5_d_arr=compute.createjsontravel(minv, maxv,d5_travel)
  #  dt_travel_d_freq+"&&"+d1_travel_d_freq+"&&"+d2_travel_d_freq+"&&"+d3_travel_d_freq+"&&"+d4_travel_d_freq+"&&"+d5_travel_d_freq
    result=list()
    result.append(ret)
    result.append(re1)
    result.append(re2)
    result.append(re3)
    result.append(re4)
    result.append(re5)
    result=pd.DataFrame(result)
    result.columns=["value"]
    result["index"]=["template","graph1","graph2","graph3","graph4","graph5"]
    re=list()
    re.append(round(stats.wasserstein_distance(dt_s_arr,d1_s_arr),3))
    re.append(round(stats.wasserstein_distance(dt_s_arr,d2_s_arr),3))
    re.append(round(stats.wasserstein_distance(dt_s_arr,d3_s_arr),3))
    re.append(round(stats.wasserstein_distance(dt_s_arr,d4_s_arr),3))
    re.append(round(stats.wasserstein_distance(dt_s_arr,d5_s_arr),3))
    re.append(round(stats.wasserstein_distance(dt_d_arr,d1_d_arr),3))
    re.append(round(stats.wasserstein_distance(dt_d_arr,d2_d_arr),3))
    re.append(round(stats.wasserstein_distance(dt_d_arr,d3_d_arr),3))
    re.append(round(stats.wasserstein_distance(dt_d_arr,d4_d_arr),3))
    re.append(round(stats.wasserstein_distance(dt_d_arr,d5_d_arr),3))
    re=pd.Series(re)
    return dt_travel_s_freq+"&&"+d1_travel_s_freq+"&&"+d2_travel_s_freq+"&&"+d3_travel_s_freq+"&&"+d4_travel_s_freq+"&&"+d5_travel_s_freq+"&&"+dt_travel_d_freq+"&&"+d1_travel_d_freq+"&&"+d2_travel_d_freq+"&&"+d3_travel_d_freq+"&&"+d4_travel_d_freq+"&&"+d5_travel_d_freq+"&&"+result.to_json(orient='records')+"&&"+re.to_json(orient='records')
    
    
    
    #[{"template":0},{"graph1":0},{"graph2":0},{"graph3":0},{"graph4":0},{"graph5":0}]
#################################################demograph analysis################################################ 
@app.route("/demoanalysis")
def demo_analysis(): 
    return demojson
    
@app.route("/graphanalysis1")
def graph_analysis1(): 
    minv =int( request.args.get('valuemin')[1:])
    maxv = int(request.args.get('valuemax')[1:])  
    
    book = request.args.get('book')
    item = request.args.get('item')
    travel = request.args.get('travel')
    demog = request.args.get('demog')
    print(book,item,travel,demog)
    selectvalue=request.args.get('selectvalue')
    checked=request.args.get('checked')
   # print(selectvalue,checked)
    
    
    valuea=compute.figana("./data/CGCS-Templaterew.csv","template",minv,maxv,book,item,travel,demog,selectvalue,checked)  
    valueb=compute.figana("./data/Q1-Graph1rew.csv","graph1",minv,maxv,book,item,travel,demog,selectvalue,checked) 
    valuec=compute.figana("./data/Q1-Graph2rew.csv","graph2",minv,maxv,book,item,travel,demog,selectvalue,checked)  
    valued=compute.figana("./data/Q1-Graph3rew.csv","graph3",minv,maxv,book,item,travel,demog,selectvalue,checked) 
    valuee=compute.figana("./data/Q1-Graph4rew.csv","graph4",minv,maxv,book,item,travel,demog,selectvalue,checked) 
    valueg=compute.figana("./data/Q1-Graph5rew.csv","graph5",minv,maxv,book,item,travel,demog,selectvalue,checked)
    
    #value.append(valuea)
   # print(valuea)
  #  valuea.append(valueb)
  #  valuea.append(valuec)
   # valuea.append(valued)
   # valuea.append(valuee)
   # valuea.append(valueg)
    valuea=pd.DataFrame(valuea)
    valuea.columns=["Template"]
    valuea['Graph1']=valueb
    valuea['Graph2']=valuec
    valuea['Graph3']=valued
    valuea['Graph4']=valuee
    valuea['Graph5']=valueg
    
    valuere=valuea.copy()
    
    valuea['Graph1']=abs(valueb-valuea["Template"])
    valuea['Graph2']=abs(valuec-valuea["Template"])
    valuea['Graph3']=abs(valued-valuea["Template"])
    valuea['Graph4']=abs(valuee-valuea["Template"])
    valuea['Graph5']=abs(valueg-valuea["Template"])
    valuea["Template"]=valuea["Template"]-valuea["Template"]
    
    
    valuea.to_json(orient='records')
   # print(valuea)
    normalized_df=normalize(valuea)
    normalized_df["index"]=["Degree Centrality","Closeness Centrality","Betweenness Centrality","Katz Centrality","Harmonic Centrality","Pagerank","Number of Nodes","Number of Edges","Degree","Average Neighbor Degree"]
 
    print(normalized_df)
    valuea["index"]=["Degree Centrality","Closeness Centrality","Betweenness Centrality","Katz Centrality","Harmonic Centrality","Pagerank","Number of Nodes","Number of Edges","Degree","Average Neighbor Degree"]
  
    valuea.set_index('index')
  #  valuea["index"]=["Degree Centrality","Closeness Centrality","Betweenness Centrality","Katz Centrality","Harmonic Centrality","Pagerank","Number of Nodes","Number of Edges","Degree","Average Neighbor Degree"]
    print(valuea)
    return normalized_df.to_json(orient='records')








if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
