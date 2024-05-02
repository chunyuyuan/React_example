import pandas as pd
import numpy as np
from scipy import stats


import json


import networkx as nx
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import base64
import sys
import io 
import time
from multiprocessing import Pool
import gc
from sklearn.preprocessing import Normalizer
def normalize(df):
    result = df.copy()
    result.iloc[:,:] = Normalizer(norm='l1').fit_transform(result)
    return result
def createjson(dictcopy, original):
   # print(dictcopy, original)
   # print(original[0])
    i=1
    l=len(dictcopy)
    if(l>len(original)):
        l=len(original)
    while(i<=l):
        dictcopy[i]=original[i-1]
        i+=1
    dictcopy= pd.Series(dictcopy)
    dictcopy=pd.DataFrame(dictcopy).reset_index()
    dictcopy.columns=["index", "value"]
    dictcopya=dictcopy["value"].copy()
    dictcopya=pd.Series(dictcopya)
   # print(dictcopy)
    return dictcopy.to_json(orient='records'),dictcopya
def createjson_adddis(dictcopy, original):
   # print(dictcopy, original)
   # print(original[0])
    i=1
    l=len(dictcopy)
    if(l>len(original)):
        l=len(original)
    while(i<=l):
        dictcopy[i]=original[i-1]
        i+=1
    dictcopy= pd.Series(dictcopy)
    dictcopy=pd.DataFrame(dictcopy).reset_index()
    dictcopy.columns=["index", "value"]
    dictcopya=dictcopy["value"].copy()
    dictcopya=pd.Series(dictcopya)
   # print(dictcopy)
    return dictcopy.to_json(orient='records'),dictcopya
        
    
def createjsonYear(phone_dt_dict, dt_phone):
    i=0

    df = pd.DataFrame(dt_phone)
    while(i<len(dt_phone)):
        phone_dt_dict[df.iloc[i]['Time']]+=1
        i+=1
    phone_dt_dict= pd.Series(phone_dt_dict)
    phone_dt_dict=pd.DataFrame(phone_dt_dict).reset_index()
    phone_dt_dict.columns=["index", "value"]
    return phone_dt_dict.to_json(orient='records')
def createjsonYear_addis(phone_dt_dict, dt_phone):
    i=0

    df = pd.DataFrame(dt_phone)
    while(i<len(dt_phone)):
        phone_dt_dict[df.iloc[i]['Time']]+=1
        i+=1
    phone_dt_dict= pd.Series(phone_dt_dict)
    phone_dt_dict=pd.DataFrame(phone_dt_dict).reset_index()
    phone_dt_dict.columns=["index", "value"]
    phone_dt_dict1=phone_dt_dict["value"].copy()
    phone_dt_dict1=pd.Series(phone_dt_dict1)
    return phone_dt_dict.to_json(orient='records'),phone_dt_dict1

def createjsontravel(minv, maxv,dt_travel):
    travel_s_freq=list()
    travel_d_freq=list()


    travel_s_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['SourceLocation']==0)]))
    travel_s_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['SourceLocation']==1)]))
    travel_s_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['SourceLocation']==2)]))
    travel_s_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['SourceLocation']==3)]))
    travel_s_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['SourceLocation']==4)]))
    travel_s_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['SourceLocation']==5)]))
    travel_s_arr=travel_s_freq.copy()
    travel_s_freq=pd.DataFrame(travel_s_freq)
    travel_s_freq.columns=["value"]
    travel_s_freq["index"]=["0","1","2","3","4","5"]
    travel_s_freq=travel_s_freq.to_json(orient='records')

    travel_d_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['TargetLocation']==0)]))
    travel_d_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['TargetLocation']==1)]))
    travel_d_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['TargetLocation']==2)]))
    travel_d_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['TargetLocation']==3)]))
    travel_d_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['TargetLocation']==4)]))
    travel_d_freq.append(len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)&(dt_travel['TargetLocation']==5)]))
    travel_d_arr=travel_d_freq.copy()
    travel_d_freq=pd.DataFrame(travel_d_freq)
    travel_d_freq.columns=["value"]
    travel_d_freq["index"]=["0","1","2","3","4","5"]
    travel_d_freq=travel_d_freq.to_json(orient='records')
    l=len(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)])
    t=sum(dt_travel[(dt_travel['Time']>=minv)&(dt_travel['Time']<=maxv)]['Weight'])
    re=0
    if(l!=0):
      re=t/l
    return travel_s_freq,travel_d_freq,round(re,3),travel_s_arr,travel_d_arr
    
    
    
def createDemojson(path):

    dt=pd.read_csv(path+'CGCS-Template.csv', delimiter = ',')
    dt=dt[dt['eType']==5]
    print("dt reading finished ")

    d1=pd.read_csv(path+'Q1-Graph1.csv', delimiter = ',')
    d1=d1[d1['eType']==5]
    print("d1 reading finished ")

    d2=pd.read_csv(path+'Q1-Graph2.csv', delimiter = ',')
    d2=d2[d2['eType']==5]

    print("d2 reading finished ")

    d3=pd.read_csv(path+'Q1-Graph3.csv', delimiter = ',')
    d3=d3[d3['eType']==5]
    print("d3 reading finished ")

    d4=pd.read_csv(path+'Q1-Graph4.csv', delimiter = ',')
    d4=d4[d4['eType']==5]
    print("d4 reading finished ")

    d5=pd.read_csv(path+'Q1-Graph5.csv', delimiter = ',')
    d5=d5[d5['eType']==5]
    print("d5 reading finished ")
    demoindex=[459381, 466907, 473173, 503218, 503701, 510031, 520660, 523927, 527449, 536346, 537281, 552988, 567195, 571970, 575030, 577992, 580426, 589943, 595298, 595581, 606730, 616315, 620120, 621924, 630626, 632961, 640784, 642329, 644226]
    gt=list()
    g1=list()
    g2=list()
    g3=list()
    g4=list()
    g5=list()
    gt1=list()
    g11=list()
    g21=list()
    g31=list()
    g41=list()
    g51=list()

    
    i=0
    while i<len(demoindex):
        gt.append(len(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]))
        if((len(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]))!=0):
            gt1.append(sum(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]['Weight'])/len(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]))
        else:
            gt1.append(0)
            
        g1.append(len(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]))
        if((len(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]))!=0):
            g11.append(sum(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]['Weight'])/len(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]))
        else:
            g11.append(0)
            
        g2.append(len(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]))
        if((len(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]))!=0):
            g21.append(sum(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]['Weight'])/len(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]))
        else:
            g21.append(0)
            
        g3.append(len(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]))
        if((len(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]))!=0):
            g31.append(sum(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]['Weight'])/len(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]))
        else:
            g31.append(0)
            
        g4.append(len(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]))
        if((len(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]))!=0):
            g41.append(sum(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]['Weight'])/len(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]))
        else:
            g41.append(0)       
            
        g5.append(len(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]))
        if((len(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]))!=0):
            g51.append(sum(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]['Weight'])/len(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]))
        else:
            g51.append(0)


        i+=1
    
    result=list()
    result.append(round(stats.wasserstein_distance(gt,g1),3))
    result.append(round(stats.wasserstein_distance(gt,g2),3))
    result.append(round(stats.wasserstein_distance(gt,g3),3))
    result.append(round(stats.wasserstein_distance(gt,g4),3))
    result.append(round(stats.wasserstein_distance(gt,g5),3))
    result.append(round(stats.wasserstein_distance(gt1,g11),3))
    result.append(round(stats.wasserstein_distance(gt1,g21),3))
    result.append(round(stats.wasserstein_distance(gt1,g31),3))
    result.append(round(stats.wasserstein_distance(gt1,g41),3))
    result.append(round(stats.wasserstein_distance(gt1,g51),3))
  
    gt=pd.DataFrame(gt)
    g1=pd.DataFrame(g1)
    g2=pd.DataFrame(g2)
    g3=pd.DataFrame(g3)
    g4=pd.DataFrame(g4)
    g5=pd.DataFrame(g5)
    gt1=pd.DataFrame(gt1)
    g11=pd.DataFrame(g11)
    g21=pd.DataFrame(g21)
    g31=pd.DataFrame(g31)
    g41=pd.DataFrame(g41)
    g51=pd.DataFrame(g51)

    
    gt.columns=["value"]
    g1.columns=["value"]
    g2.columns=["value"]
    g3.columns=["value"]
    g4.columns=["value"]
    g5.columns=["value"]
    gt1.columns=["value"]
    g11.columns=["value"]
    g21.columns=["value"]
    g31.columns=["value"]
    g41.columns=["value"]
    g51.columns=["value"]
    gt["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g1["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g2["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g3["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g4["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g5["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    gt1["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g11["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g21["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g31["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g41["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g51["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
   
    result=pd.Series(result)
  #  print(result)
    return gt.to_json(orient='records')+"&&"+g1.to_json(orient='records')+"&&"+g2.to_json(orient='records')+"&&"+g3.to_json(orient='records')+"&&"+g4.to_json(orient='records')+"&&"+g5.to_json(orient='records')+"&&"+gt1.to_json(orient='records')+"&&"+g11.to_json(orient='records')+"&&"+g21.to_json(orient='records')+"&&"+g31.to_json(orient='records')+"&&"+g41.to_json(orient='records')+"&&"+g51.to_json(orient='records')+"&&"+result.to_json(orient='records')

def drawfig(path,name,minv,maxv,book,item,travel,demog,selectvalue,checked):
  #  print(book,item,travel,demog)
  #  print(selectvalue,checked)
   # %matplotlib inline
    import matplotlib.pyplot as plt
    df = pd.read_csv(path)
    df1=df
   
    df1['Time']=np.floor(df['Time']/86400).astype(int)
    df1=df1[(df1['Time']>=minv)&(df1['Time']<=maxv)]
    df1=df1[df1['eType']!=5]
    if(travel=='false'):
      df1=df1[df1['eType']!=6]
    if(item=='false'):
      df1=df1[(df1['eType']!=2)&(df1['eType']!=3)]
    people = list(df1[(df1['eType']==1)|(df1['eType']==0)]['Source'].unique())

    people =people+( list(df1[df1['eType']<=1]['Target'].unique()))
    people =people+( list(df1['Source'].unique()))

    people=list(set(people))
    if(book=='true'):
      p2=df[df['eType']==4].Source
      cc1=p2.isin(people).loc[lambda x : x==True].index
      df1=df1.append(df.loc[cc1],ignore_index=True)
    if(demog=='true'):
      p1=df[df['eType']==5].Source
      cc=p1.isin(people).loc[lambda x : x==True].index
      df1=df1.append(df.loc[cc],ignore_index=True)
    print()
    
   ## df1=df1.append(df.loc[cc],ignore_index=True)
   # print(df1)
    G = nx.from_pandas_edgelist(df1, 'Source', 'Target', edge_attr='eType')
    #G=nx.Graph()
    durations = [i['eType'] for i in dict(G.edges).values()]
    colors = ['black','black','blue','blue','green','pink','brown']
  #  print(durations)
    color=list()
    i=0
    while i < len(durations):
        color.append(colors[durations[i]])
        i=i+1
    layout = nx.circular_layout(G)


    item = list(df1[df1['eType']==2]['Target'].unique())
    item = item+ list(df1[df1['eType']==3]['Target'].unique())

    item=list(set(item))
    book=list(df1[df1['eType']==4]['Target'].unique())
    travel=list(df1[df1['eType']==6]['Target'].unique())
    demo=list(df1[df1['eType']==5]['Target'].unique())
  #  print(book)
  #  print(demo)
    radii = [28,25,30,65,40]  # for concentric circles
    label={}
    for ea in layout.keys():
        new_r = 1
        if ea in  item:
            new_r = radii[1]
            label[ea]=""
        elif ea in people:
            new_r = radii[3]
            label[ea]=""
        elif ea in book:
            new_r = radii[0]
            label[ea]=""
        elif ea in travel:
            new_r = radii[2]
            label[ea]=""
        elif ea in demo:
            new_r = radii[4]
            label[ea]=""
        else:
            pass
        layout[ea] *= new_r 
    #print(people)
    people=sorted(people, key=lambda x: G.degree(x))
   # print(people)
   # print(G.degree(people))
    nx.draw_networkx_labels(G, layout,labels=label)
    nx.draw_networkx_nodes(G, layout,
                           nodelist=people,
                           node_color='r',
                           node_size=100,
                           alpha=0.8,with_labels=False)

    nx.draw_networkx_nodes(G, layout,
                           nodelist=item,
                           node_color='b',
                           node_size=50,
                           alpha=0.8)
    nx.draw_networkx_nodes(G, layout,
                           nodelist=book,
                           node_color='g',
                           node_size=100,
                           alpha=0.8)
    nx.draw_networkx_nodes(G, layout,
                           nodelist=travel,
                           node_color='brown',
                           node_size=100,
                           alpha=0.8)
    nx.draw_networkx_nodes(G, layout,
                           nodelist=demo,
                           node_color='grey',
                           node_size=50,
                           alpha=0.8)

    nx.draw_networkx_edges(G, layout, width=0.2, alpha=1,edge_color=color)

  #  plt.axis('off')
    #nx.draw(G, layout, width=1.0, alpha=0.5)

    #print(layout)
   # print(df1[df1['eType']==3])
    t = plt.text(0.5, 0.5, name, horizontalalignment='center', verticalalignment='center',fontsize=60)
    t.set_alpha(.2)
    pic_IObytes = io.BytesIO()
 #   print(minv,maxv)
  #  print(G)
    plt.axis('off')
   # time.sleep(2)
    plt.savefig(pic_IObytes,  format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.getvalue())
    
  #  
    
    #from matplotlib import pyplot as plt
  #  import matplotlib.image as mpimg
  #  print(pic_hash)
  #  i = base64.b64decode(pic_hash)
  #  i = io.BytesIO(i)
  #  i = mpimg.imread(i, format='png')
  #  plt.savefig('foo.png')
    plt.clf()
    
    collected = gc.collect() 
    time.sleep(.300)
# Prints Garbage collector  
# as 0 object 
    print("Garbage collector: collected", 
          "%d objects." % collected)
    
   # plt.imshow(i)
    #plt.show()
     # { value: 'Degree Centrality', label: 'Degree Centrality' },
         # { value: 'Eigenvector Centrality', label: 'Eigenvector Centrality' },
         # { value: 'Closeness Centrality', label: 'Closeness Centrality' },
         # { value: 'Betweenness Centrality', label: 'Betweenness Centrality' },
         # { value: 'Katz Centrality', label: 'Katz Centrality' },
         # { value: 'Harmonic Centrality', label: 'Harmonic Centrality' },
         # { value: 'Pagerank Centrality', label: 'Pagerank Centrality' },
         # { value: 'Hits Centrality', label: 'Hits Centrality' },
    

    
      #  if (selectvalue=='Hits'):
        #    value=round(pd.Series(nx.hits(G)[0]).mean(),3)
         
            
    
   
   # print(value)       
        #  if (selectvalue=='Hits'):
          #  value=round(pd.Series(nx.hits(G)[0]).max(),3)
          
      
   # plt.close()
    return pic_hash   
    
def figana(path,name,minv,maxv,book,item,travel,demog,selectvalue,checked):
  #  print(book,item,travel,demog)
  #  print(selectvalue,checked)
   # %matplotlib inline
    df = pd.read_csv(path)
    df1=df
   
    df1['Time']=np.floor(df['Time']/86400).astype(int)
    df1=df1[(df1['Time']>=minv)&(df1['Time']<=maxv)]
    df1=df1[df1['eType']!=5]
    if(travel=='false'):
      df1=df1[df1['eType']!=6]
    if(item=='false'):
      df1=df1[(df1['eType']!=2)&(df1['eType']!=3)]
    people = list(df1[(df1['eType']==1)|(df1['eType']==0)]['Source'].unique())

    people =people+( list(df1[df1['eType']<=1]['Target'].unique()))
    people =people+( list(df1['Source'].unique()))

    people=list(set(people))
    if(book=='true'):
      p2=df[df['eType']==4].Source
      cc1=p2.isin(people).loc[lambda x : x==True].index
      df1=df1.append(df.loc[cc1],ignore_index=True)
    if(demog=='true'):
      p1=df[df['eType']==5].Source
      cc=p1.isin(people).loc[lambda x : x==True].index
      df1=df1.append(df.loc[cc],ignore_index=True)
    print()
    
   ## df1=df1.append(df.loc[cc],ignore_index=True)
   # print(df1)
    G = nx.from_pandas_edgelist(df1, 'Source', 'Target', edge_attr='eType')
    #G=nx.Graph()
  #  durations = [i['eType'] for i in dict(G.edges).values()]
   # colors = ['black','black','blue','blue','green','pink','brown']
  #  print(durations)
   # color=list()
   # i=0
   # while i < len(durations):
       # color.append(colors[durations[i]])
       # i=i+1
   # layout = nx.circular_layout(G)


  #  item = list(df1[df1['eType']==2]['Target'].unique())
  #  item = item+ list(df1[df1['eType']==3]['Target'].unique())

   # item=list(set(item))
   # book=list(df1[df1['eType']==4]['Target'].unique())
 #   travel=list(df1[df1['eType']==6]['Target'].unique())
   # demo=list(df1[df1['eType']==5]['Target'].unique())
  #  print(book)
  #  print(demo)
  #  radii = [28,25,30,65,40]  # for concentric circles
  #  label={}
  #  for ea in layout.keys():
     #   new_r = 1
     #   if ea in  item:
      #      new_r = radii[1]
      #      label[ea]=""
      #  elif ea in people:
      #      new_r = radii[3]
       #     label[ea]=""
       # elif ea in book:
       #     new_r = radii[0]
       #     label[ea]=""
       # elif ea in travel:
        #    new_r = radii[2]
        #    label[ea]=""
       # elif ea in demo:
       #     new_r = radii[4]
       #     label[ea]=""
       # else:
       #     pass
       # layout[ea] *= new_r 
    #print(people)
   # people=sorted(people, key=lambda x: G.degree(x))
   # print(people)
   # print(G.degree(people))
   # nx.draw_networkx_labels(G, layout,labels=label)
   # nx.draw_networkx_nodes(G, layout,
        #                   nodelist=people,
        #                   node_color='r',
        #                   node_size=100,
        #                   alpha=0.8,with_labels=False)

   # nx.draw_networkx_nodes(G, layout,
       #                    nodelist=item,
        #                   node_color='b',
         #                  node_size=50,
         #                  alpha=0.8)
    #nx.draw_networkx_nodes(G, layout,
     #                      nodelist=book,
      #                     node_color='g',
      #                     node_size=100,
       #                    alpha=0.8)
  #  nx.draw_networkx_nodes(G, layout,
       #                    nodelist=travel,
        #                   node_color='brown',
        #                   node_size=100,
        #                   alpha=0.8)
   # nx.draw_networkx_nodes(G, layout,
              #             nodelist=demo,
               #            node_color='grey',
                #           node_size=50,
                 #          alpha=0.8)

   # nx.draw_networkx_edges(G, layout, width=0.2, alpha=1,edge_color=color)

  #  plt.axis('off')
    #nx.draw(G, layout, width=1.0, alpha=0.5)

    #print(layout)
   # print(df1[df1['eType']==3])
   # t = plt.text(0.5, 0.5, name, horizontalalignment='center', verticalalignment='center',fontsize=60)
  #  t.set_alpha(.2)
  #  pic_IObytes = io.BytesIO()
 #   print(minv,maxv)
  #  print(G)
    
   # time.sleep(2)
  #  plt.savefig(pic_IObytes,  format='png')
   # pic_IObytes.seek(0)
   # pic_hash = base64.b64encode(pic_IObytes.getvalue())
    
   # plt.axis('off')
    
    #from matplotlib import pyplot as plt
  #  import matplotlib.image as mpimg
  #  print(pic_hash)
  #  i = base64.b64decode(pic_hash)
  #  i = io.BytesIO(i)
  #  i = mpimg.imread(i, format='png')
  #  plt.savefig('foo.png')
  #  plt.clf()
  #  
   # plt.imshow(i)
    #plt.show()
     # { value: 'Degree Centrality', label: 'Degree Centrality' },
         # { value: 'Eigenvector Centrality', label: 'Eigenvector Centrality' },
         # { value: 'Closeness Centrality', label: 'Closeness Centrality' },
         # { value: 'Betweenness Centrality', label: 'Betweenness Centrality' },
         # { value: 'Katz Centrality', label: 'Katz Centrality' },
         # { value: 'Harmonic Centrality', label: 'Harmonic Centrality' },
         # { value: 'Pagerank Centrality', label: 'Pagerank Centrality' },
         # { value: 'Hits Centrality', label: 'Hits Centrality' },
    
    
    value=list()
    #if(checked=='false'):
    #average
       # if (selectvalue== 'Degree Centrality'):
    if len(G)!=0:
        value.append(round(pd.Series(nx.degree_centrality(G)).mean(),3))
    else:
        value.append(sys.maxsize)
      #  if (selectvalue=='Eigenvector Centrality'):
   # if len(G)!=0:  
   #     value.append(round(pd.Series(nx.eigenvector_centrality(G,max_iter=10)).mean(),3))
 #   else:
   #     value.append(sys.maxsize)
      #  if (selectvalue=='Closeness Centrality'):
    if len(G)!=0:
        value.append(round(pd.Series(nx.closeness_centrality(G)).mean(),3))
    else:
        value.append(sys.maxsize)  #  if (selectvalue=='Betweenness Centrality'):
    if len(G)!=0:
        value.append(round(pd.Series(nx.betweenness_centrality(G)).mean(),3))
    else:
        value.append(sys.maxsize)  #  if (selectvalue=='Katz Centrality'):
    if len(G)!=0:
        value.append(round(pd.Series(nx.katz_centrality_numpy(G)).mean(),3))
    else:
        value.append(sys.maxsize)  #  if (selectvalue=='Harmonic Centrality'):
    if len(G)!=0:
        value.append(round(pd.Series(nx.harmonic_centrality(G)).mean(),3))
    else:
        value.append(sys.maxsize) #  if (selectvalue=='Pagerank'):
    if len(G)!=0:
        value.append(round(pd.Series(nx.pagerank(G)).mean(),3))
    else:
        value.append(sys.maxsize)
    if len(G)!=0:
        value.append(round(G.number_of_nodes(),3))
    else:
        value.append(sys.maxsize)
    if len(G)!=0:
        value.append(round(G.number_of_edges(),3))
    else:
        value.append(sys.maxsize)
    if len(G)!=0:
        value.append(round(pd.Series([val for (node, val) in G.degree()]).mean(),3))
    else:
        value.append(sys.maxsize)
    if len(G)!=0:
        value.append(round(pd.Series(list(nx.average_neighbor_degree(G).values())).mean(),3))
    else:
        value.append(sys.maxsize)
    
      #  if (selectvalue=='Hits'):
        #    value=round(pd.Series(nx.hits(G)[0]).mean(),3)
         
            
    
   
   # print(value)       
        #  if (selectvalue=='Hits'):
          #  value=round(pd.Series(nx.hits(G)[0]).max(),3)
          
      
    collected = gc.collect() 
    	

 

 
# Wait for 300 milliseconds
# .3 can also be used
    time.sleep(.300)
  
# Prints Garbage collector  
# as 0 object 
    print("Garbage collector: collected", 
          "%d objects." % collected)
    return value 

def analysis(minv,maxv):
    path='./data/'

    gr1=list()
    gr2=list()
    gr3=list()
    gr4=list()
    gr5=list()
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

    
    
    dt_rsnew,dtarray=createjson_adddis(dt_rs1,dt_rs)
   # print(dtarray)

 
    d1_rsnew,d1array=createjson_adddis(d1_rs1,d1_rs)


    d2_rsnew,d2array=createjson_adddis(d2_rs1,d2_rs)


    d3_rsnew,d3array=createjson_adddis(d3_rs1,d3_rs)

   
    d4_rsnew,d4array=createjson_adddis(d4_rs1,d4_rs)

    
    d5_rsnew,d5array=createjson_adddis(d5_rs1,d5_rs)
    result=list()
    result.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d5array),3))
    gr1.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    gr2.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    gr3.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    gr4.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    gr5.append(round(stats.wasserstein_distance(dtarray,d5array),3))


    dt_rt=dt_phone['Target'][(dt_phone['Time']>=minv)&(dt_phone['Time']<=maxv)].value_counts().values
    d1_rt=d1_phone['Target'][(d1_phone['Time']>=minv)&(d1_phone['Time']<=maxv)].value_counts().values
    d2_rt=d2_phone['Target'][(d2_phone['Time']>=minv)&(d2_phone['Time']<=maxv)].value_counts().values
    d3_rt=d3_phone['Target'][(d3_phone['Time']>=minv)&(d3_phone['Time']<=maxv)].value_counts().values
    d4_rt=d4_phone['Target'][(d4_phone['Time']>=minv)&(d4_phone['Time']<=maxv)].value_counts().values
    d5_rt=d5_phone['Target'][(d5_phone['Time']>=minv)&(d5_phone['Time']<=maxv)].value_counts().values
    dt_rt1=phone_t_dict.copy()
    dt_rtnew=createjson(dt_rt1,dt_rt)

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

    dt_rtnew,dtarraynew=createjson_adddis(dt_rt1,dt_rt)

  
    d1_rtnew,d1arraynew=createjson_adddis(d1_rt1,d1_rt)

  
    d2_rtnew,d2arraynew=createjson_adddis(d2_rt1,d2_rt)


    d3_rtnew,d3arraynew=createjson_adddis(d3_rt1,d3_rt)

    d4_rtnew,d4arraynew=createjson_adddis(d4_rt1,d4_rt)

  
    d5_rtnew,d5arraynew=createjson_adddis(d5_rt1,d5_rt)
    result.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3)) 
    gr1.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    gr2.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    gr3.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    gr4.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    gr5.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3)) 
    
    if(minv==0):
     minv=0
    else :
     minv=minv-1
  #  print(len(email_dt_array[minv:(maxv-1)]))
  #  print(len(email_dt_array))
   # global phone_dt_array
   # global phone_d1_array
   # global phone_d2_array
   # global phone_d3_array
   # global phone_d4_array
   # global phone_d5_array 
    
    phone_dt_dict=phone_year_dict.copy()

    phone_dt_dictnew,arr=createjsonYear_addis(phone_dt_dict, dt_phone)
    phone_dt_array=arr
    phone_d1_dict=phone_year_dict.copy()

    phone_d1_dictnew,arr1=createjsonYear_addis(phone_d1_dict, d1_phone)
    phone_d1_array=arr1
    phone_d2_dict=phone_year_dict.copy()

    phone_d2_dictnew,arr2=createjsonYear_addis(phone_d2_dict, d2_phone)
    phone_d2_array=arr2
    phone_d3_dict=phone_year_dict.copy()

    phone_d3_dictnew,arr3=createjsonYear_addis(phone_d3_dict, d3_phone)
    phone_d3_array=arr3
    phone_d4_dict=phone_year_dict.copy()

    phone_d4_dictnew,arr4=createjsonYear_addis(phone_d4_dict, d4_phone)
    phone_d4_array=arr4
    phone_d5_dict=phone_year_dict.copy()
    
    phone_d5_dictnew,arr5=createjsonYear_addis(phone_d5_dict, d5_phone)
    phone_d5_array=arr5
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d1_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d2_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d3_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d4_array[minv:(maxv-1)]),3))
    result.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d5_array[minv:(maxv-1)]),3))

    gr1.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d1_array[minv:(maxv-1)]),3))
    gr2.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d2_array[minv:(maxv-1)]),3))
    gr3.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d3_array[minv:(maxv-1)]),3))
    gr4.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d4_array[minv:(maxv-1)]),3))
    gr5.append(round(stats.wasserstein_distance(phone_dt_array[minv:(maxv-1)],phone_d5_array[minv:(maxv-1)]),3))
    
    
    result=pd.Series(result)  
    collected = gc.collect() 
   
# Prints Garbage collector  
# as 0 object 
    print("Garbage collector: collected", 
          "%d objects." % collected)
  #  print(result)
    
    
    dt_email=dt[dt['eType']==0]
   # print("dt_email cut finished ")

    d1_email=d1[d1['eType']==0]
   # print("d1_email cut finished ")

    d2_email=d2[d2['eType']==0]
  #  print("d2_email cut finished ")

    d3_email=d3[d3['eType']==0]
  #  print("d3_email cut finished ")

    d4_email=d4[d4['eType']==0]
   # print("d4_email cut finished ")

    d5_email=d5[d5['eType']==0]
   # print("d5_email cut finished ")    
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
    dt_rs=dt_email['Source'].value_counts().values
    d1_rs=d1_email['Source'].value_counts().values
    d2_rs=d2_email['Source'].value_counts().values
    d3_rs=d3_email['Source'].value_counts().values
    d4_rs=d4_email['Source'].value_counts().values
    d5_rs=d5_email['Source'].value_counts().values

    #print(dt_rs,d1_rs,d2_rs,d3_rs,d4_rs,d5_rs)

    dt_rs1=email_s_dict.copy()
    dt_rsnew,dtarray=createjson(dt_rs1,dt_rs)

    d1_rs1=email_s_dict.copy()
    d1_rsnew,d1array=createjson(d1_rs1,d1_rs)

    d2_rs1=email_s_dict.copy()
    d2_rsnew,d2array=createjson(d2_rs1,d2_rs)

    d3_rs1=email_s_dict.copy()
    d3_rsnew,d3array=createjson(d3_rs1,d3_rs)

    d4_rs1=email_s_dict.copy()
    d4_rsnew,d4array=createjson(d4_rs1,d4_rs)

    d5_rs1=email_s_dict.copy()
    d5_rsnew,d5array=createjson(d5_rs1,d5_rs)

    result=list()
    result.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    result.append(round(stats.wasserstein_distance(dtarray,d5array),3))
    
    gr1.append(round(stats.wasserstein_distance(dtarray,d1array),3))
    gr2.append(round(stats.wasserstein_distance(dtarray,d2array),3))
    gr3.append(round(stats.wasserstein_distance(dtarray,d3array),3))
    gr4.append(round(stats.wasserstein_distance(dtarray,d4array),3))
    gr5.append(round(stats.wasserstein_distance(dtarray,d5array),3))

    dt_rt=dt_email['Target'].value_counts().values
    d1_rt=d1_email['Target'].value_counts().values
    d2_rt=d2_email['Target'].value_counts().values
    d3_rt=d3_email['Target'].value_counts().values
    d4_rt=d4_email['Target'].value_counts().values
    d5_rt=d5_email['Target'].value_counts().values
    dt_rt1=email_t_dict.copy()
    dt_rtnew,dtarraynew=createjson(dt_rt1,dt_rt)

    d1_rt1=email_t_dict.copy()
    d1_rtnew,d1arraynew=createjson(d1_rt1,d1_rt)

    d2_rt1=email_t_dict.copy()
    d2_rtnew,d2arraynew=createjson(d2_rt1,d2_rt)

    d3_rt1=email_t_dict.copy()
    d3_rtnew,d3arraynew=createjson(d3_rt1,d3_rt)

    d4_rt1=email_t_dict.copy()
    d4_rtnew,d4arraynew=createjson(d4_rt1,d4_rt)

    d5_rt1=email_t_dict.copy()
    d5_rtnew,d5arraynew=createjson(d5_rt1,d5_rt)
    


    result.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    result.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3))

    gr1.append(round(stats.wasserstein_distance(dtarraynew,d1arraynew),3))
    gr2.append(round(stats.wasserstein_distance(dtarraynew,d2arraynew),3))
    gr3.append(round(stats.wasserstein_distance(dtarraynew,d3arraynew),3))
    gr4.append(round(stats.wasserstein_distance(dtarraynew,d4arraynew),3))
    gr5.append(round(stats.wasserstein_distance(dtarraynew,d5arraynew),3))
    
    email_dt_dict=email_year_dict.copy()

    email_dt_dictnew,arr=createjsonYear_addis(email_dt_dict, dt_email)
    
    global email_dt_array
    global email_d1_array
    global email_d2_array
    global email_d3_array
    global email_d4_array
    global email_d5_array
    email_dt_array=arr
    
    
    email_d1_dict=email_year_dict.copy()

    email_d1_dictnew,arr1=createjsonYear_addis(email_d1_dict, d1_email)
    email_d1_array=arr1
    email_d2_dict=email_year_dict.copy()

    email_d2_dictnew,arr2=createjsonYear_addis(email_d2_dict, d2_email)
    email_d2_array=arr2
    email_d3_dict=email_year_dict.copy()

    email_d3_dictnew,arr3=createjsonYear_addis(email_d3_dict, d3_email)
    email_d3_array=arr3
    email_d4_dict=email_year_dict.copy()

    email_d4_dictnew,arr4=createjsonYear_addis(email_d4_dict, d4_email)
    email_d4_array=arr4
    email_d5_dict=email_year_dict.copy()

    email_d5_dictnew,arr5=createjsonYear_addis(email_d5_dict, d5_email)
    email_d5_array=arr5
   # print("email finish analysis")
    #print(len(email_dt_array),len(email_d1_array),round(stats.wasserstein_distance(email_dt_array,email_d1_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d1_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d2_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d3_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d4_array),3))
    result.append(round(stats.wasserstein_distance(email_dt_array,email_d5_array),3))
    
    gr1.append(round(stats.wasserstein_distance(email_dt_array,email_d1_array),3))
    gr2.append(round(stats.wasserstein_distance(email_dt_array,email_d2_array),3))
    gr3.append(round(stats.wasserstein_distance(email_dt_array,email_d3_array),3))
    gr4.append(round(stats.wasserstein_distance(email_dt_array,email_d4_array),3))
    gr5.append(round(stats.wasserstein_distance(email_dt_array,email_d5_array),3))
    
    result=pd.Series(result)
  #  print(result)
    dt_procu=dt[dt['eType']==2]
  #  print("dt_procu cut finished ")


    d1_procu=d1[d1['eType']==2]
  #  print("d1_procu cut finished ")


    d2_procu=d2[d2['eType']==2]
  #  print("d2_procu cut finished ")


    d3_procu=d3[d3['eType']==2]
  #  print("d3_procu cut finished ")


    d4_procu=d4[d4['eType']==2]
  #  print("d4_procu cut finished ")


    d5_procu=d5[d5['eType']==2]
  #  print("d5_procu cut finished ")
    

   

    procu_dict=[{"template":0},{"graph1":0},{"graph2":0},{"graph3":0},{"graph4":0},{"graph5":0}]

    procu_dict=pd.Series(procu_dict) 
    procu_freq=list()
    procu_freq.append(len(dt_procu[(dt_procu['Time']>=minv)&(dt_procu['Time']<=maxv)]))
    procu_freq.append(len(d1_procu[(d1_procu['Time']>=minv)&(d1_procu['Time']<=maxv)]))
    procu_freq.append(len(d2_procu[(d2_procu['Time']>=minv)&(d2_procu['Time']<=maxv)]))
    procu_freq.append(len(d3_procu[(d3_procu['Time']>=minv)&(d3_procu['Time']<=maxv)]))
    procu_freq.append(len(d4_procu[(d4_procu['Time']>=minv)&(d4_procu['Time']<=maxv)]))
    procu_freq.append(len(d5_procu[(d5_procu['Time']>=minv)&(d5_procu['Time']<=maxv)]))

    t=(len(dt_procu[(dt_procu['Time']>=minv)&(dt_procu['Time']<=maxv)]))
    v1=(len(d1_procu[(d1_procu['Time']>=minv)&(d1_procu['Time']<=maxv)]))
    v2=(len(d2_procu[(d2_procu['Time']>=minv)&(d2_procu['Time']<=maxv)]))
    v3=(len(d3_procu[(d3_procu['Time']>=minv)&(d3_procu['Time']<=maxv)]))
    v4=(len(d4_procu[(d4_procu['Time']>=minv)&(d4_procu['Time']<=maxv)]))
    v5=(len(d5_procu[(d5_procu['Time']>=minv)&(d5_procu['Time']<=maxv)])) 
    
    gr1.append(abs(v1-t))
    gr2.append(abs(v2-t))
    gr3.append(abs(v3-t))
    gr4.append(abs(v4-t))
    gr5.append(abs(v5-t))
    

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
   
    t=(int(sum(dt_procu[(dt_procu['Time']>=minv)&(dt_procu['Time']<=maxv)]['Weight'])))
    v1=(int(sum(d1_procu[(d1_procu['Time']>=minv)&(d1_procu['Time']<=maxv)]['Weight'])))
    v2=(int(sum(d2_procu[(d2_procu['Time']>=minv)&(d2_procu['Time']<=maxv)]['Weight'])))
    v3=(int(sum(d3_procu[(d3_procu['Time']>=minv)&(d3_procu['Time']<=maxv)]['Weight'])))
    v4=(int(sum(d4_procu[(d4_procu['Time']>=minv)&(d4_procu['Time']<=maxv)]['Weight'])))
    v5=(int(sum(d5_procu[(d5_procu['Time']>=minv)&(d5_procu['Time']<=maxv)]['Weight'])))

    gr1.append(abs(v1-t))
    gr2.append(abs(v2-t))
    gr3.append(abs(v3-t))
    gr4.append(abs(v4-t))
    gr5.append(abs(v5-t))

    procu_weight=pd.DataFrame(procu_weight)
    procu_weight.columns=["value"]
    procu_weight["index"]=["template","graph1","graph2","graph3","graph4","graph5"]
  #  print(procu_freq,procu_weight)
    dt_travel=dt[dt['eType']==6]
   # print("dt_procu cut finished ")


    d1_travel=d1[d1['eType']==6]
   # print("d1_procu cut finished ")


    d2_travel=d2[d2['eType']==6]
   # print("d2_procu cut finished ")


    d3_travel=d3[d3['eType']==6]
   # print("d3_procu cut finished ")


    d4_travel=d4[d4['eType']==6]
   # print("d4_procu cut finished ")


    d5_travel=d5[d5['eType']==6]
   # print("d5_procu cut finished ")
    
#dt_travel, d1_travel ,d2_travel,d3_travel,d4_travel,d5_travel,procu_travel
   

    procu_dict=[{"template":0},{"graph1":0},{"graph2":0},{"graph3":0},{"graph4":0},{"graph5":0}]

    procu_dict=pd.Series(procu_dict) 

    dt_travel_s_freq,dt_travel_d_freq,ret,dt_s_arr,dt_d_arr=createjsontravel(minv, maxv,dt_travel)
    d1_travel_s_freq,d1_travel_d_freq,re1,d1_s_arr,d1_d_arr=createjsontravel(minv, maxv,d1_travel)
    d2_travel_s_freq,d2_travel_d_freq,re2,d2_s_arr,d2_d_arr=createjsontravel(minv, maxv,d2_travel)
    d3_travel_s_freq,d3_travel_d_freq,re3,d3_s_arr,d3_d_arr=createjsontravel(minv, maxv,d3_travel)
    d4_travel_s_freq,d4_travel_d_freq,re4,d4_s_arr,d4_d_arr=createjsontravel(minv, maxv,d4_travel)
    d5_travel_s_freq,d5_travel_d_freq,re5,d5_s_arr,d5_d_arr=createjsontravel(minv, maxv,d5_travel)
  #  dt_travel_d_freq+"&&"+d1_travel_d_freq+"&&"+d2_travel_d_freq+"&&"+d3_travel_d_freq+"&&"+d4_travel_d_freq+"&&"+d5_travel_d_freq
    result=list()
    result.append(ret)
    result.append(re1)
    result.append(re2)
    result.append(re3)
    result.append(re4)
    result.append(re5)
    
    gr1.append(abs(re1-ret))
    gr2.append(abs(re2-ret))
    gr3.append(abs(re3-ret))
    gr4.append(abs(re4-ret))
    gr5.append(abs(re5-ret))
    
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
    
    gr1.append(round(stats.wasserstein_distance(dt_s_arr,d1_s_arr),3))
    gr2.append(round(stats.wasserstein_distance(dt_s_arr,d2_s_arr),3))
    gr3.append(round(stats.wasserstein_distance(dt_s_arr,d3_s_arr),3))
    gr4.append(round(stats.wasserstein_distance(dt_s_arr,d4_s_arr),3))
    gr5.append(round(stats.wasserstein_distance(dt_s_arr,d5_s_arr),3))
    gr1.append(round(stats.wasserstein_distance(dt_d_arr,d1_d_arr),3))
    gr2.append(round(stats.wasserstein_distance(dt_d_arr,d2_d_arr),3))
    gr3.append(round(stats.wasserstein_distance(dt_d_arr,d3_d_arr),3))
    gr4.append(round(stats.wasserstein_distance(dt_d_arr,d4_d_arr),3))
    gr5.append(round(stats.wasserstein_distance(dt_d_arr,d5_d_arr),3))
    
    
    re=pd.Series(re)
  #  print(re)
   # dt=pd.read_csv(path+'CGCS-Template.csv', delimiter = ',')
    dt=dt[dt['eType']==5]
  #  print("dt reading finished ")

   # d1=pd.read_csv(path+'Q1-Graph1.csv', delimiter = ',')
    d1=d1[d1['eType']==5]
  #  print("d1 reading finished ")

   # d2=pd.read_csv(path+'Q1-Graph2.csv', delimiter = ',')
    d2=d2[d2['eType']==5]

  #  print("d2 reading finished ")

  #  d3=pd.read_csv(path+'Q1-Graph3.csv', delimiter = ',')
    d3=d3[d3['eType']==5]
  #  print("d3 reading finished ")

   # d4=pd.read_csv(path+'Q1-Graph4.csv', delimiter = ',')
    d4=d4[d4['eType']==5]
  #  print("d4 reading finished ")

   # d5=pd.read_csv(path+'Q1-Graph5.csv', delimiter = ',')
    d5=d5[d5['eType']==5]
   # print("d5 reading finished ")
    demoindex=[459381, 466907, 473173, 503218, 503701, 510031, 520660, 523927, 527449, 536346, 537281, 552988, 567195, 571970, 575030, 577992, 580426, 589943, 595298, 595581, 606730, 616315, 620120, 621924, 630626, 632961, 640784, 642329, 644226]
    gt=list()
    g1=list()
    g2=list()
    g3=list()
    g4=list()
    g5=list()
    gt1=list()
    g11=list()
    g21=list()
    g31=list()
    g41=list()
    g51=list()

    
    i=0
    while i<len(demoindex):
        gt.append(len(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]))
        if((len(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]))!=0):
            gt1.append(sum(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]['Weight'])/len(dt[(dt['Source']==demoindex[i])|(dt['Target']==demoindex[i])]))
        else:
            gt1.append(0)
            
        g1.append(len(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]))
        if((len(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]))!=0):
            g11.append(sum(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]['Weight'])/len(d1[(d1['Source']==demoindex[i])|(d1['Target']==demoindex[i])]))
        else:
            g11.append(0)
            
        g2.append(len(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]))
        if((len(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]))!=0):
            g21.append(sum(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]['Weight'])/len(d2[(d2['Source']==demoindex[i])|(d2['Target']==demoindex[i])]))
        else:
            g21.append(0)
            
        g3.append(len(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]))
        if((len(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]))!=0):
            g31.append(sum(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]['Weight'])/len(d3[(d3['Source']==demoindex[i])|(d3['Target']==demoindex[i])]))
        else:
            g31.append(0)
            
        g4.append(len(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]))
        if((len(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]))!=0):
            g41.append(sum(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]['Weight'])/len(d4[(d4['Source']==demoindex[i])|(d4['Target']==demoindex[i])]))
        else:
            g41.append(0)       
            
        g5.append(len(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]))
        if((len(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]))!=0):
            g51.append(sum(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]['Weight'])/len(d5[(d5['Source']==demoindex[i])|(d5['Target']==demoindex[i])]))
        else:
            g51.append(0)


        i+=1
    
    result=list()
    result.append(round(stats.wasserstein_distance(gt,g1),3))
    result.append(round(stats.wasserstein_distance(gt,g2),3))
    result.append(round(stats.wasserstein_distance(gt,g3),3))
    result.append(round(stats.wasserstein_distance(gt,g4),3))
    result.append(round(stats.wasserstein_distance(gt,g5),3))
    result.append(round(stats.wasserstein_distance(gt1,g11),3))
    result.append(round(stats.wasserstein_distance(gt1,g21),3))
    result.append(round(stats.wasserstein_distance(gt1,g31),3))
    result.append(round(stats.wasserstein_distance(gt1,g41),3))
    result.append(round(stats.wasserstein_distance(gt1,g51),3))
    
    gr1.append(round(stats.wasserstein_distance(gt,g1),3))
    gr2.append(round(stats.wasserstein_distance(gt,g2),3))
    gr3.append(round(stats.wasserstein_distance(gt,g3),3))
    gr4.append(round(stats.wasserstein_distance(gt,g4),3))
    gr5.append(round(stats.wasserstein_distance(gt,g5),3))
    gr1.append(round(stats.wasserstein_distance(gt1,g11),3))
    gr2.append(round(stats.wasserstein_distance(gt1,g21),3))
    gr3.append(round(stats.wasserstein_distance(gt1,g31),3))
    gr4.append(round(stats.wasserstein_distance(gt1,g41),3))
    gr5.append(round(stats.wasserstein_distance(gt1,g51),3))
  
    gt=pd.DataFrame(gt)
    g1=pd.DataFrame(g1)
    g2=pd.DataFrame(g2)
    g3=pd.DataFrame(g3)
    g4=pd.DataFrame(g4)
    g5=pd.DataFrame(g5)
    gt1=pd.DataFrame(gt1)
    g11=pd.DataFrame(g11)
    g21=pd.DataFrame(g21)
    g31=pd.DataFrame(g31)
    g41=pd.DataFrame(g41)
    g51=pd.DataFrame(g51)

    
    gt.columns=["value"]
    g1.columns=["value"]
    g2.columns=["value"]
    g3.columns=["value"]
    g4.columns=["value"]
    g5.columns=["value"]
    gt1.columns=["value"]
    g11.columns=["value"]
    g21.columns=["value"]
    g31.columns=["value"]
    g41.columns=["value"]
    g51.columns=["value"]
    gt["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g1["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g2["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g3["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g4["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g5["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    gt1["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g11["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g21["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g31["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g41["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
    g51["index"]=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
   
    result=pd.Series(result)
   # print(gr1,gr2,gr3,gr4,gr5)
    gr1=pd.DataFrame(gr1)
    gr1.columns=["graph1"]
    gr1['graph2']=gr2
    gr1['graph3']=gr3
    gr1['graph4']=gr4
    gr1['graph5']=gr5
    normalized_df=normalize(gr1)
    normalized_df['index']=["phone call", "phone receive","phone communication","email send","email receive","email communication","procurement freq","procurement weight","demographics freq","demographics weight","source location","target location","trip time"]
    print(normalized_df)
    collected = gc.collect() 
    	

 

 
# Wait for 300 milliseconds
# .3 can also be used
    time.sleep(.300)
  
# Prints Garbage collector  
# as 0 object 
    print("Garbage collector: collected", 
          "%d objects." % collected)
    return normalized_df

    

    

