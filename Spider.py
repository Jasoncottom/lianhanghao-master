# -*- coding: utf-8 -*-
# @File : test6.py
# @Author : GAVT
# @Time : 2022/02/10 17:10:05

import requests

host = 'http://www.lianhanghao.com'
path = '/api/bank/lhhTableData'
url = host+path
headers = {
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Accept":"application/json, text/javascript, */*; q=0.01"
    }

def search(pagenum):    
    params = {
        "current":pagenum,
        "size":1,
        "bank_id":"",
        "province_id":"",
        "city_id":"",
        "keywords":""
        }
    results = requests.post(url,json=params,headers=headers).json()
    print (results)    
    bank_dict = {}
    if results['data']['data'] != []:
        for data in results['data']['data']:
            bank_dict[data['hanghao']] = data['bankname']
    else:
        bank_dict['total_num'] = results['data']['total_num']
    #return bank_dict
    #for item in bank_dict.items():
        #for i in range(len(item)):
            #str1 = item[i]
            #str2 = item[i+1]
            #print(str1,' ', str2 ,end="\n")
    #file = open('C:/Users/Jason/Desktop/com.lianhanghao/data.txt', 'a')
    for k,v in bank_dict.items():
        #file.write(str(k)+' '+str(v)+'\n')
        #file.flush();
        print(str(k)+' '+str(v))
    #file.close()        
    
if __name__ == '__main__':
    #for i in range(2,2):
        search(1)
