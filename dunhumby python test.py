#!/usr/bin/env python
# coding: utf-8

# ### Given the list of basket values, do the following:
# #### a. Print out whether each basket is small (basket value < £5), medium (£5 ≤ basket value < £10) or large (basket value ≥ £10);
# #### b. Sum and print the value of the medium value baskets.
# #### basket_values = [3.43,9.73,7.56,9.52,15.23,2.25,6.44,7.38]
# 

# In[1]:


basket_values = [3.43,9.73,7.56,9.52,15.23,2.25,6.44,7.38]


# In[2]:


medium_total_value= 0
for val in basket_values:
    if val < 5:
        print("This basket is small at £", val)
    elif val >= 10:
        print("This basket is large at £", val)
    else:
        print("This basket is medium at £", val)
        medium_total_value+=val
print("The sum of the medium value baskets is: ", medium_total_value)


# ### 2. You are given the following nested dictionaries, which represent items in a basket. Do the following:
# #### a. Return the product name for item 7527.
# #### b. Return the total value of this basket.
# #### c. Add another entry for a product that costs £4.95, has ID 7524 and name ‘poppy seeds’.
# #### basket = {'2624': {'price': 0.5, 'prod_name': 'salt'},
# #### '2894': {'price': 3.25, 'prod_name': 'yeast'},
# #### '7527': {'price': 2.5, 'prod_name': 'flour'}}
# 

# In[3]:


basket = {'2624': {'price': 0.5, 'prod_name': 'salt'}, '2894': {'price': 3.25, 'prod_name': 'yeast'}, '7527': {'price': 2.5, 'prod_name': 'flour'}}


# In[4]:


### a. return the product name for item 7527
print("The product name for item 7527 is", basket['7527']['prod_name'])
### b. return the total value of this basket
total_value = sum(basket[x]['price'] for x in basket)
print("The total value of the basket is £",total_value)
### c. add another entry for a product that costs £4.95, has ID 7524 and name ‘poppy seeds’
basket['7524']={'price': 4.95, 'prod_name': 'poppy seeds'}
print(basket) # to confirm added entry


# ### 3. Below is the source code for a function called ‘get_sql_string’.
# ###### 1 def get_sql_string(stores):
# ###### 2 store_names = [x.split(', ')[0] for x in stores]
# ###### 3 store_names = [x.replace(' ', '_') for x in store_names]
# ###### 4 store_regions = [x.split(',')[1] for x in stores]
# ###### 5 locations = store_names + store_regions
# ###### 6 columns = ['sales_' + x.lower() for x in locations]
# ###### 7 return ', '.join(columns)
# #### a. There is a bug in line 4. What should the line be?
# #### b. Assuming this bug was fixed, what would be returned if the following command was
# #### executed:
# #### my_stores = ['Fulham Palace Rd, Hammersmith', 'Crown St, Reading',
# #### 'Leavesden Green, Watford']
# #### get_sql_string(my_stores)
# 

# In[5]:


my_stores = ['Fulham Palace Rd, Hammersmith', 'Crown St, Reading','Leavesden Green, Watford']


# In[6]:


def get_sql_string(stores):
    store_names = [x.split(', ')[0] for x in stores]
    store_names = [x.replace(' ', '_') for x in store_names]
    # The bug in the following line was that the x.split was missing a space after the comma so there was an
    # added space in the returned column strings
    store_regions = [x.split(', ')[1] for x in stores] 
    locations = store_names + store_regions
    columns = ['sales_' + x.lower() for x in locations]
    return ', '.join(columns)
print("Print the result of get_sql_string with the corrected line 4:")
print(get_sql_string(my_stores))


# ### 4. Write a function that: 
# ##### a. accepts a list of strings as input.
# ##### b. returns an alphabetically ordered list of unique strings.
# ##### c. prints the string(s) with maximum length in the console.

# In[7]:


def my_func(lst_str):
    max_len=len(max(lst_str, key=len))
    [print(x) for x in lst_str if len(x) == max_len]
    sort_lst = set(sorted(lst_str))
    return sort_lst
test_lst = ['hi', 'how', 'are', 'you', 'today', 'today', 'is', 'a', 'good', 'day', 'asdfg']
my_func(test_lst)


# ### Section 2

# #### 1. Find the nth largest salary.
# #### 2. List the highest salary paid for each job.
# #### 3. In which year did most people join the company? Display the year and the number of Employees.
# #### 4. Create a new column with the length of service of the Employees (in the form n years and m months).
# #### 5. List all the Employees who have at least one person reporting to them.

# In[8]:


import pandas as pd
import numpy as np


# In[9]:


df_emp = pd.read_csv('employee.csv')
df_dept = pd.read_csv('dept.csv')


# In[10]:


df_emp.head()


# In[11]:


df_dept.head()


# In[12]:


# Problem 1
def find_nth_salary(n, df):
    df_salaries = df.sort_values(['SAL'], ascending=False).reset_index(drop=True)[['SAL']]
    df_salaries=(df_salaries.SAL.unique())
    return int(df_salaries[n-1])

find_nth_salary(2,df_emp)


# In[13]:


# Problem 2
def find_highest_salary(job,df):
    df = df[df.JOB==job]
    salaries = df.sort_values(['SAL'], ascending=False).reset_index(drop=True)[['SAL']]
    return int(salaries.values[0])
find_highest_salary('Analyst', df_emp)


# In[14]:


# 3. In which year did most people join the company? Display the year and the number of Employees
df_emp['HIREYEAR'] = pd.to_datetime(df_emp['HIREDATE']).dt.strftime('%Y')
year_count = df_emp['HIREYEAR'].value_counts().max()
common_year = df_emp['HIREYEAR'].value_counts().idxmax()
print("The most people joined the company in", common_year," with ",year_count," people joining.")


# In[15]:


#4. Create a new column with the length of service of the Employees (in the form n years and m months).
service_months = ((pd.to_datetime("today") - pd.to_datetime(df_emp['HIREDATE'])))/np.timedelta64(1,'M') 
service_years = ((pd.to_datetime("today") - pd.to_datetime(df_emp['HIREDATE'])))/np.timedelta64(1,'Y')
service_years = service_years.astype(int).astype(str)+' years '
service_months_units = (service_months%12).astype(int).astype(str)+' months'

df_emp['SERVICE'] = service_years +service_months_units
df_emp.head()


# In[16]:


# List all the Employees who have at least one person reporting to them.
df_emp['HAS_UNDERLINGS'] = df_emp['EMPNO'].isin(df_emp['MGR'].values)
managers=df_emp['NAME'][df_emp['HAS_UNDERLINGS']==True]   
print(managers)


# In[ ]:




