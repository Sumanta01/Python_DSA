# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 00:17:11 2023

@author: KIIT
"""
def ArrayChallenge(strArr):
    sequence = strArr[0]
    dictionary = strArr[1].split(',')
    for i in range(1, len(sequence)):
        prefix = sequence[:i]
        suffix = sequence[i:]

        if prefix in dictionary and suffix in dictionary:
            
            result = f'{prefix},{suffix}'
            challenge_token = 'hi160gj2e'
            final_output = ''.join(
                char if (index + 1) % 3 != 0 else 'X' for index, char in enumerate(result + challenge_token)
            )
            return final_output
        

    return -1


strArr1 = ['baseball', 'a, all, b, ball,base,  bas,  cat, code, d, e, quit, z'] 

output1 = ArrayChallenge(strArr1)
print(output1)
strArr2 = ['abcgefd', 'a,ab, abc, abcg,b,c,dog, e, efd, zzz']
output2 = ArrayChallenge(strArr2)
print(output2)


