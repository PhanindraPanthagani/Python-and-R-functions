#!/usr/bin/env python
# coding: utf-8

# In[1]:




#Read data 

def read_data(colnames,collist):
    #rownames is a list containing all row names 
    #oollist is a list of list containing values in each column 
    ncols=len(colnames)
    data_dictionary= {}
    count = 0
    for col in colnames : 
        data_dictionary[col]= collist[count]
        count = count+1
        
    return data_dictionary


# In[2]:


#Reading Problem 1 data 
colnames_prob1= ['Claim Number','Accident Year','Report Year','Transaction Date','Loss Payment','Case Reserve Balance']
collist_prob1 = [[1,1,1,2,2,3,3,3],[2007,2007,2007,2007,2007,2008,2008,2008],[2007,2007,2007,2008,2008,2008,2008,2008],
           ['1-Apr-07','1-Jul-08','1-Jun-09','1-May-08','1-Jul-09','1-Aug-08','1-Mar-09','1-Jul-10'],
                 [200,400,1000,1000,400,100,200,400],
                [600,1200,0,400,0,400,100,0]]
data_dict_prob1 = read_data(colnames_prob1,collist_prob1)


# In[3]:


#Reading Problem 2 data 
colnames_prob2= ['Policy','Number of Vehicles','Effective Date','Expiration Date']
collist_prob2 = [['A','B','C','D','E'],[2,3,1,2,1],['January 1,2018','March 1,2018','July 1,2018','October 1,2018','November 1,2018'],
                 ['June 30,2018','August 31,2018','December 31,2018','March 31,2019','April 30,2019']]
                 
data_dict_prob2 = read_data(colnames_prob2,collist_prob2)


# In[4]:


#Reading Problem 3 data 
colnames_prob3= ['Name','2016 Expense Ratio','2017 Expense Ratio','2018($000S)']
collist_prob3 = [['Direct Premium Written','Direct Premium Earned','Commision and Brokerage Expenses Incurred',
                  'Other Acquisition Expense Incurred','General Expenses','Taxes License & Fees Incurred'],
                 ['','','12%','12.8%','15.0%','2.1%'],['','','13%','12.7%','5.5%','2.2%'],[1000*6100,1000*5920,1000*945,1000*760,1000*325,1000*130]]
                 
data_dict_prob3 = read_data(colnames_prob3,collist_prob3)


# In[5]:


#Reading Problem 4 data 
#EarnedPremiumtable
colnames_prob4_EarnedPremiumtable =['Calendar Year','Earned Premium($)']
collist_prob4_EarnedPremiumtable = [[2017,2018],[3850000,4200000]]
data_dict_prob4_EarnedPremiumtable = read_data(colnames_prob4_EarnedPremiumtable,collist_prob4_EarnedPremiumtable)
#RateChange Table
colnames_prob4_RateChangetable= ['Rate Change Effective date','Overall Rate Change']
collist_prob4_RateChangetable = [['January 1,2017','July 1,2017'],['10%','5%']]
data_dict_prob4_RateChangetable= read_data(colnames_prob4_RateChangetable,collist_prob4_RateChangetable)


#Written Premium Table name
colnames_prob4_WrittenPremiumtable =['Quarter and Year','Average Written Premium at Current Rate Level']
collist_prob4_WrittenPremiumtable = [['2Q 2016','4Q 2016','2Q 2017','4Q 2017','2Q 2018','4Q 2018'],
                                     ['$1771','$1806','$1840','$1877','$1914','$1953']]
data_dict_prob4_WrittenPremiumtable= read_data(colnames_prob4_WrittenPremiumtable,collist_prob4_WrittenPremiumtable)

# data_dict_prob4
data_dict_prob4 = { 'EarnedPremiumtable' : data_dict_prob4_EarnedPremiumtable,
                    'RateChangetable'   : data_dict_prob4_RateChangetable,
                    'WrittenPremiumtable' :data_dict_prob4_WrittenPremiumtable}

data_dict_prob4


# In[6]:


#Reading Problem 5 data 
#PremiumTransactions
colnames_prob5_PremiumTransactions =['Policy','Original Effective Date','Original Expiration Date','Transaction Effective Date',
                                    'Full-Term Premium($)','Notes']
collist_prob5_PremiumTransactions = [['A','A','B','C','C'],['July 1,2016','July 1,2016','April 1,2017','October 1,2017','October 1,2017'],
                                    ['June 30,2017','June 30,2017','March 31,2018','September 30,2018','September 30,2018'],
                                    ['July 1,2016','April 1,2017','April 1,2017','October 1,2017','April 1,2018'],
                                    [800,400,1000,500,'N/A'],['Start of New Policy','Additional Premium to Endorsement',
                                                             'Start of New Policy','Start of New Policy','Policy Canceled']]
data_dict_prob5_PremiumTransactions = read_data(colnames_prob5_PremiumTransactions,collist_prob5_PremiumTransactions)

#Loss Transactions
colnames_prob5_LossTransactions =['Policy','Accident Date','Payment Date','Loss Payment($)']
collist_prob5_LossTransactions=[['A','A','B','C'],['October 1,2016','January 1,2017','October 1,2017','January 1,2018'],
                               ['October 15,2016','January 15,2017','January 15,2018','January 15,2018'],
                               [500,200,500,750]]

data_dict_prob5_LossTransactions = read_data(colnames_prob5_LossTransactions,collist_prob5_LossTransactions)


# data_dict_prob5
data_dict_prob5 = { 'PremiumTransactions' : data_dict_prob5_PremiumTransactions,
                    'LossTransactions'   : data_dict_prob5_LossTransactions}

data_dict_prob5


# In[9]:


#Reading Problem 6 data 
colnames_prob6= ['Effective Date','Overall Average Rate Change','Rate Per Exposure($)','Class Factor X',
                 'Class Factor Y','Class Factor Z','Expense Fee($)']
collist_prob6 = [['January 1,2016','July 1,2017','October 1,2017','April 1,2018'],['0.0%','10.0%','0.0%','1.0%'],
                ['1,000','1,112','1,175','1,175'],[1.2,1.2,1.1,1.1],[0.85,0.85,0.85,0.75],[1.0,1.0,1.0,1.0],
                 [120,120,120,132]]
                 
data_dict_prob6 = read_data(colnames_prob6,collist_prob6)


# In[10]:


import pickle

datapicklefile = {'data_dict_prob1': data_dict_prob1,
                 'data_dict_prob2': data_dict_prob2,
                 'data_dict_prob3': data_dict_prob3,
                 'data_dict_prob4': data_dict_prob4,
                 'data_dict_prob5': data_dict_prob5,
                 'data_dict_prob6': data_dict_prob6}


# In[11]:


#Dump the dictionary above into a pickle file 
with open('data.pickle', 'wb') as handle:
    pickle.dump(datapicklefile, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('data.pickle', 'rb') as handle:
    b = pickle.load(handle)

print(datapicklefile == b)


# In[ ]:





# In[ ]:




