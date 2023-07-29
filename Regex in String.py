# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:08:04 2023

@author: KIIT
"""

import re

st="Have you ever been jealouse .to your girlfriend with other boys !"
match=re.search("been", st)
print(match)
match2=re.search("\.", st)
print(match2)
print("startng index: ",match.start())
print("Ending index: ",match.end())


de="Hello i am you boy friend and my no is : 1283643773 and my passcode is 8767543"

regex="\d+"
match3=re.findall(regex, de)
print(match3)

p=re.compile("[a-f]")
print(p.findall("Are you a good housewife i did not prefer you ?"))