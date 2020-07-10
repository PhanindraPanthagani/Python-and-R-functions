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
            