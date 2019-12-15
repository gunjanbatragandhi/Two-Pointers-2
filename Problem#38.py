# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:11:20 2019

@author: gunjan
"""

#Duplicate removal - 1
nums = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,4,5,5,5,6,8]

ptr1=0
ptr2=1


while(ptr2!=len(nums))   : 
    if(nums[ptr2]==nums[ptr2-1]):
        ptr2+=1
    else:
        nums[ptr1+1]=nums[ptr2]
        ptr2+=1
        ptr1+=1
        
nums[0:ptr1+1]

#Duplicate removal - 2
nums = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,4,5,5,5,6,8]
#nums = [1,1,1,2,2,2,2,2,3,4,5,5,5,6,8,99]

ptr1=0
ptr2=1
flag=0

while(ptr2!=len(nums))   : 
    if((nums[ptr2]==nums[ptr2-1]) and flag==0): # copy 2nd no
        flag=1
        nums[ptr1+1]=nums[ptr2]
        ptr2+=1
        ptr1+=1
    elif((nums[ptr2]==nums[ptr2-1]) and flag==1): # do nothing
        ptr2+=1
    else:
        nums[ptr1+1]=nums[ptr2] # 
        ptr2+=1
        ptr1+=1
        flag=0
        
nums[0:ptr1+1]
        
        
        
