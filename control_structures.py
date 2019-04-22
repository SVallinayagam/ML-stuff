# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:40:03 2019

@author: RPS
"""

import random
import requests
import pandas as pd
import pymysql
'''
data = random.randint(1,1000)
if data > 500:
    print ("Random number is: %d"%data)
    else:
    print ("Random number is < 500: %d"%data)
'''     
def generate_employee_code():
    emp_code=[]
    for _ in range(1,100):
        emp_code.append(random.randint(1,500))
    return emp_code

def list_demo():
    datalist=["citi","hcl",1234]
    for _ in datalist:
        if type(_) == str:
            print(_)
                        
def tuple_demo():
    datalist=("citi","hcl",1234)
    for _ in datalist:
        if type(_) == str:
            print(_)
            
def dictionary():
    product_data=[{'pcode':2345, 'pname': 'apple'},
                  {'pcode':2345, 'pname': 'samsung'},
                  {'pcode':3456, 'pname': 'nokia'},
                  {'pcode':2345, 'pname': 'vivo'}]
    for _ in product_data:
        for(k,v) in _.items(): 
            if(v == 2345):
                print(_)
    
      
def JSON():
    response = requests.get('https://jsonplaceholder.typicode.com/users')                                     
    print(response)
    for user in response.json():
        for(k,v) in user.items():
            if (k == 'username'):
                print(v)

def pandas():
    df = pd.read_csv("input_csv.txt")
    #print("Shape", df.shape)
    #print(df["BMI"])
    #print(df[0:1])
    #specific column
    #print(df.iloc[:,:])
    print(df.iloc[0:3,0])
    
    
def mysql_demo():   
    try:
        conn = pymysql.connect(host ="localhost",user="root", password="rps@1", db="test", cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("insert into test.test values('%s','%d')"%("balji",25))
        cursor.execute("select * from test.test")
        result = cursor.fetchall()
        for _ in result:
            for(k,v) in _.items():
                print(_) 
                #print(result)
                conn.commit()
    except pymysql.Error as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()
        
        
def missing_values():
    df = pd.read_csv("missing_values.txt")
    print(df)
    
            