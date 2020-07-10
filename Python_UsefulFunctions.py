# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:06:36 2020

@author: Phanindra.Panthagani
"""


def include_with_substr(Keyword,List,case_sensitive=False):
    '''
    This functions returns all words in the list with the Keyword specified . 
    It can either be case sensitive or not 
    
    Arguments : 
    Keyword : The keyword to be searched in the list 
    List : The list in which to search the keyword 
    case_sensitive : Whether the search is a case sensitive one 
    
    '''
    import re 
    
    Returnlist = [] 
    
    for item in List: 
        if(case_sensitive):
            if(Keyword in item):
                Returnlist.append(item)
        else: #Its not case sensitive_find all possible matches 
            a = re.match(Keyword, item, re.IGNORECASE)
            if(a):
                Returnlist.append(item)
    
    return Returnlist
      
#Using a simple strategy to one hot encode categories given a df 

def Imputeallcolumns_onehotcategorical(df,categ_columns = None ,continouscolumns = None):
    '''
    Function to Impute Cagtegorical columns in a dataframe with mode values 
    This function also one hot encodes categorical columns 
    df : pandas dataframe
    categ_columns : Categorical column names
    continouscolumns : Continous Column names
    
    '''
    verbose=False
    ##Categorical variables
    for col in categ_columns:
        col_mode=df[col].value_counts().index[0] #Calculate the mode of categorical variable 
        #Impute with categorical mode next line
        df[col].fillna(col_mode, inplace=True)
        #one hot encoding categorical variables below
        if(verbose):
            print("One hot encdoing the column",col)
        prefixname = 'one_hot_'+ col
        
        df = pd.concat([df,pd.get_dummies(df[col], prefix= prefixname ,dummy_na=False)],axis=1).drop([col],axis=1)

    ##Continous variables
    for col in continouscolumns:
        if(verbose):
            print("Imputing the continous Col: ",col)
        df[col] = pd.to_numeric(df[col], downcast="float")
        col_median =df[col].median(skipna=True ) #Calculate the mode of categorical variable 
        if(col == 'var12'):
            print("Col median for var 12 is",col_median)
        df[col]= df[col].fillna(col_median)
        #df[col].replace({'NaN': col_median} ,inplace=True)
    return df 
