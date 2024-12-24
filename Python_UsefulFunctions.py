# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:06:36 2020

@author: Phanindra.Panthagani
"""

import pandas as pd

def value_counts_PP(pdSeries):
    """
    Enhancement of value counts function to include the percentages

    Author : @ Phanindra Panthagani

    input : pdSeries 
    output : result_df which is an output dataframe consisting of value_counts and percentage
    """

    # Get the value counts
    value_counts = pdSeries.value_counts()
    
    # Calculate the percentage
    percentage = (value_counts / len(pdSeries)) * 100
    
    # Combine value counts and percentage into a DataFrame
    result_df = pd.DataFrame({'Count': value_counts, 'Percentage': percentage})
    
    return result_df




def describe_more(df,normalize_ind=False, weight_column=None, skip_columns=[], dropna=True):
    """"
    Purpose: Analyze input Pandas DataFrame and return stats per column
    Details: The function calculates levels for categorical variables and allows to analyze summarized information

    To view wide table set following Pandas options:
    pd.set_option('display.width', 1000)
    pd.set_option('max_colwidth',200)
    
    """
    var = [] ; l = [] ; t = []; unq =[]; min_l = []; max_l = [];
    assert isinstance(skip_columns, list), "Argument skip_columns should be list"
    if weight_column is not None:
        if weight_column not in list(df.columns):
            raise AssertionError('weight_column is not a valid column name in the input DataFrame')
      
    for x in df:
        if x in skip_columns:
            pass
        else:
            var.append( x )
            uniq_counts = len(pd.value_counts(df[x],dropna=dropna))
            uniq_counts = len(pd.value_counts(df[x], dropna=dropna)[pd.value_counts(df[x],dropna=dropna)>0])
            l.append(uniq_counts)
            t.append( df[ x ].dtypes )
            min_l.append(df[x].apply(str).str.len().min())
            max_l.append(df[x].apply(str).str.len().max())
            if weight_column is not None and x not in skip_columns:
                df2 = df.groupby(x).agg({weight_column: 'sum'}).sort_values(weight_column, ascending=False)
                df2['authtrans_vts_cnt']=((df2[weight_column])/df2[weight_column].sum()).round(2)
                unq.append(df2.head(n=100).to_dict()[weight_column])
            else:
                df_cat_d = df[x].value_counts(normalize=normalize_ind,dropna=dropna).round(decimals=2)
                df_cat_d = df_cat_d[df_cat_d>0]
                #unq.append(df[x].value_counts().iloc[0:100].to_dict())
                unq.append(df_cat_d.iloc[0:100].to_dict())
            
    levels = pd.DataFrame( { 'A_Variable' : var , 'Levels' : l , 'Datatype' : t ,
                             'Min Length' : min_l,
                             'Max Length': max_l,
                             'Level_Values' : unq} )
    #levels.sort_values( by = 'Levels' , inplace = True )
    return levels


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
