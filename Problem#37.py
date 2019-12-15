# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:52:54 2019

@author: gunja
"""


#Brute Force
nums1=[[1,4,7,11,15],
       [2,5,8,12,19],
       [3,6,9,16,12],
       [10,13,14,17,24],
       [18,21,23,26,30]]

target=8
foundbit=0

for i in range(len(nums1)):
    for j in range(len(nums1[0])):
        if nums1[i][j]==target:
            foundbit=1
if foundbit==1:
    print "True"
else:
    print "False"
    
#TC=O(nXm)
#SC=O(1)
    
###############################################################################
    
ptr1=len(nums1)-1
ptr2=0
foundbit=0

while(ptr1>=0 and ptr2<=len(nums1[0])-1):
    print ptr1
    print ptr2
    if(target==nums1[ptr1][ptr2]):
        foundbit=1
        break
    if(target>nums1[ptr1][ptr2]):
        ptr2+=1
    else:
        ptr1-=1

if foundbit==1:
    print "True"
else:
    print "False"
    
#TC=O(n+m)
#SC=O(1)
    