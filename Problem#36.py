# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:39:50 2019

@author: gunja
"""

nums1=[5,6,7,0,0,0];m=3
nums2=[1,2,3];n=3
#op=[1,2,2,3,5,6]

ptr1=m-1
ptr2=n-1
ptr=m+n-1

while(ptr1>=0 and ptr2>=0):
    if(nums1[ptr1]>nums2[ptr2]):
        nums1[ptr]=nums1[ptr1]
        ptr1-=1
        ptr-=1
    else:                 #(nums1[ptr1]<nums2[ptr2]):
        nums1[ptr]=nums2[ptr2]
        ptr2-=1
        ptr-=1
while(ptr2>=0):
    nums1[ptr]=nums2[ptr2]
    ptr2-=1
    ptr-=1

print nums1
        


#TC=O(m+n)  #traversing both array
#SC=O(1)   #not using extra space