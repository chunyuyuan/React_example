import pandas as pd
import numpy as np

#####read data##################
def read(path):


    #####read data##################

    dt=pd.read_csv(path+'CGCS-Template.csv', delimiter = ',')
    print("dt reading finished ")

    d1=pd.read_csv(path+'Q1-Graph1.csv', delimiter = ',')
    print("d1 reading finished ")

    d2=pd.read_csv(path+'Q1-Graph2.csv', delimiter = ',')
    print("d2 reading finished ")

    d3=pd.read_csv(path+'Q1-Graph3.csv', delimiter = ',')
    print("d3 reading finished ")

    d4=pd.read_csv(path+'Q1-Graph4.csv', delimiter = ',')
    print("d4 reading finished ")

    d5=pd.read_csv(path+'Q1-Graph5.csv', delimiter = ',')
    print("d5 reading finished ")
    ################################
    return dt,d1,d2,d3,d4,d5

    
#####read email data##################    
def read_email(path):    
    dt=pd.read_csv(path+'CGCS-Template.csv', delimiter = ',')
    dt['Time']=np.floor(dt['Time']/86400).astype(int)
    print("dt reading finished ")

    d1=pd.read_csv(path+'Q1-Graph1.csv', delimiter = ',')
    d1['Time']=np.floor(d1['Time']/86400).astype(int)
    print("d1 reading finished ")

    d2=pd.read_csv(path+'Q1-Graph2.csv', delimiter = ',')
    d2['Time']=np.floor(d2['Time']/86400).astype(int)
    print("d2 reading finished ")

    d3=pd.read_csv(path+'Q1-Graph3.csv', delimiter = ',')
    d3['Time']=np.floor(d3['Time']/86400).astype(int)
    print("d3 reading finished ")

    d4=pd.read_csv(path+'Q1-Graph4.csv', delimiter = ',')
    d4['Time']=np.floor(d4['Time']/86400).astype(int)
    print("d4 reading finished ")

    d5=pd.read_csv(path+'Q1-Graph5.csv', delimiter = ',')
    d5['Time']=np.floor(d5['Time']/86400).astype(int)
    dt_phone=dt[dt['eType']==1]
    print("dt_phone cut finished ")
    
    dt_email=dt[dt['eType']==0]
    print("dt_email cut finished ")

    d1_email=d1[d1['eType']==0]
    print("d1_email cut finished ")

    d2_email=d2[d2['eType']==0]
    print("d2_email cut finished ")

    d3_email=d3[d3['eType']==0]
    print("d3_email cut finished ")

    d4_email=d4[d4['eType']==0]
    print("d4_email cut finished ")

    d5_email=d5[d5['eType']==0]
    print("d5_email cut finished ")    
  #  return dt_email,d1_email,d2_email,d3_email,d4_email,d5_email
    email_s_length=len(dt_email['Source'].value_counts())
 
    i=1
    email_s_dict=dict()
    while(i<=email_s_length):
        email_s_dict[i]=0    
        i+=1
    email_s_dict=pd.Series(email_s_dict) 
    
    email_t_length=len(dt_email['Target'].value_counts())
   
    i=1
    email_t_dict=dict()
    while(i<=email_t_length):
        email_t_dict[i]=0    
        i+=1
    email_t_dict=pd.Series(email_t_dict) 
    
    i=1
    email_year_dict=dict()
    while(i<=365):
        email_year_dict[i]=0    
        i+=1
    email_year_dict=pd.Series(email_year_dict) 

    return dt_email, d1_email ,d2_email,d3_email,d4_email,d5_email,email_s_dict,email_t_dict,email_year_dict
    

    
    
    
    
#####read phone data##################   
def read_phone(path):   
    dt=pd.read_csv(path+'CGCS-Template.csv', delimiter = ',')
    dt['Time']=np.floor(dt['Time']/86400).astype(int)
    print("dt reading finished ")

    d1=pd.read_csv(path+'Q1-Graph1.csv', delimiter = ',')
    d1['Time']=np.floor(d1['Time']/86400).astype(int)
    print("d1 reading finished ")

    d2=pd.read_csv(path+'Q1-Graph2.csv', delimiter = ',')
    d2['Time']=np.floor(d2['Time']/86400).astype(int)
    print("d2 reading finished ")

    d3=pd.read_csv(path+'Q1-Graph3.csv', delimiter = ',')
    d3['Time']=np.floor(d3['Time']/86400).astype(int)
    print("d3 reading finished ")

    d4=pd.read_csv(path+'Q1-Graph4.csv', delimiter = ',')
    d4['Time']=np.floor(d4['Time']/86400).astype(int)
    print("d4 reading finished ")

    d5=pd.read_csv(path+'Q1-Graph5.csv', delimiter = ',')
    d5['Time']=np.floor(d5['Time']/86400).astype(int)
    dt_phone=dt[dt['eType']==1]
    print("dt_phone cut finished ")


    d1_phone=d1[d1['eType']==1]
    print("d1_phone cut finished ")


    d2_phone=d2[d2['eType']==1]
    print("d2_phone cut finished ")


    d3_phone=d3[d3['eType']==1]
    print("d3_phone cut finished ")


    d4_phone=d4[d4['eType']==1]
    print("d4_phone cut finished ")


    d5_phone=d5[d5['eType']==1]
    print("d5_phone cut finished ")
    phone_s_length=len(dt_phone['Source'].value_counts())
 
    i=1
    phone_s_dict=dict()
    while(i<=phone_s_length):
        phone_s_dict[i]=0    
        i+=1
    phone_s_dict=pd.Series(phone_s_dict) 
    
    phone_t_length=len(dt_phone['Target'].value_counts())
   
    i=1
    phone_t_dict=dict()
    while(i<=phone_t_length):
        phone_t_dict[i]=0    
        i+=1
    phone_t_dict=pd.Series(phone_t_dict) 

    i=1
    phone_year_dict=dict()
    while(i<=365):
        phone_year_dict[i]=0    
        i+=1
    phone_year_dict=pd.Series(phone_year_dict) 
    
   


    return dt_phone, d1_phone ,d2_phone,d3_phone,d4_phone,d5_phone,phone_s_dict,phone_t_dict,phone_year_dict
    
#####read procurement data##################   
def read_procurement(path):   
    dt=pd.read_csv(path+'CGCS-Template.csv', delimiter = ',')
    dt['Time']=np.floor(dt['Time']/86400).astype(int)
    print("dt reading finished ")

    d1=pd.read_csv(path+'Q1-Graph1.csv', delimiter = ',')
    d1['Time']=np.floor(d1['Time']/86400).astype(int)
    print("d1 reading finished ")

    d2=pd.read_csv(path+'Q1-Graph2.csv', delimiter = ',')
    d2['Time']=np.floor(d2['Time']/86400).astype(int)
    print("d2 reading finished ")

    d3=pd.read_csv(path+'Q1-Graph3.csv', delimiter = ',')
    d3['Time']=np.floor(d3['Time']/86400).astype(int)
    print("d3 reading finished ")

    d4=pd.read_csv(path+'Q1-Graph4.csv', delimiter = ',')
    d4['Time']=np.floor(d4['Time']/86400).astype(int)
    print("d4 reading finished ")

    d5=pd.read_csv(path+'Q1-Graph5.csv', delimiter = ',')
    d5['Time']=np.floor(d5['Time']/86400).astype(int)
    dt_procu=dt[dt['eType']==2]
    print("dt_procu cut finished ")


    d1_procu=d1[d1['eType']==2]
    print("d1_procu cut finished ")


    d2_procu=d2[d2['eType']==2]
    print("d2_procu cut finished ")


    d3_procu=d3[d3['eType']==2]
    print("d3_procu cut finished ")


    d4_procu=d4[d4['eType']==2]
    print("d4_procu cut finished ")


    d5_procu=d5[d5['eType']==2]
    print("d5_procu cut finished ")
    

   

    procu_dict=[{"template":0},{"graph1":0},{"graph2":0},{"graph3":0},{"graph4":0},{"graph5":0}]

    procu_dict=pd.Series(procu_dict) 

    
   


    return dt_procu, d1_procu ,d2_procu,d3_procu,d4_procu,d5_procu,procu_dict
#####read travel data##################   
def read_travel(path):   
    dt=pd.read_csv(path+'CGCS-Template.csv', delimiter = ',')
    dt['Time']=np.floor(dt['Time']/86400).astype(int)
    print("dt reading finished ")

    d1=pd.read_csv(path+'Q1-Graph1.csv', delimiter = ',')
    d1['Time']=np.floor(d1['Time']/86400).astype(int)
    print("d1 reading finished ")

    d2=pd.read_csv(path+'Q1-Graph2.csv', delimiter = ',')
    d2['Time']=np.floor(d2['Time']/86400).astype(int)
    print("d2 reading finished ")

    d3=pd.read_csv(path+'Q1-Graph3.csv', delimiter = ',')
    d3['Time']=np.floor(d3['Time']/86400).astype(int)
    print("d3 reading finished ")

    d4=pd.read_csv(path+'Q1-Graph4.csv', delimiter = ',')
    d4['Time']=np.floor(d4['Time']/86400).astype(int)
    print("d4 reading finished ")

    d5=pd.read_csv(path+'Q1-Graph5.csv', delimiter = ',')
    d5['Time']=np.floor(d5['Time']/86400).astype(int)
    dt_procu=dt[dt['eType']==6]
    print("dt_procu cut finished ")


    d1_procu=d1[d1['eType']==6]
    print("d1_procu cut finished ")


    d2_procu=d2[d2['eType']==6]
    print("d2_procu cut finished ")


    d3_procu=d3[d3['eType']==6]
    print("d3_procu cut finished ")


    d4_procu=d4[d4['eType']==6]
    print("d4_procu cut finished ")


    d5_procu=d5[d5['eType']==6]
    print("d5_procu cut finished ")
    

   

    procu_dict=[{"template":0},{"graph1":0},{"graph2":0},{"graph3":0},{"graph4":0},{"graph5":0}]

    procu_dict=pd.Series(procu_dict) 

    
   


    return dt_procu, d1_procu ,d2_procu,d3_procu,d4_procu,d5_procu,procu_dict