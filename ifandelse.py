# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 00:03:43 2020

@author: Carlos1
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:06:50 2020

@author: CEC
"""
"""
nativeVLAN=1
dataVLAN=1
if nativeVLAN==dataVLAN:
    print("The native VLAN and the data VLAN are the same. ")

else:
    print("This native VLAN and the data VLAN are the different. ")
    
"""

aclNum=int (input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <=99:
    print("This is a standard IPv4 ACL. ")
elif aclNum >= 100 and aclNum <=199:
    print("This is a extended IPv4 ACL. ")
else:
   print("This is not extended or standard IPv4 ACL. ")
    
