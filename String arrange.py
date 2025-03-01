# cook your dish here

def complementDNA(st):
    #A="T",T="A",C="G",G="C"
    res=""
    
    for i in range(0,len(st)):
        if st[i]=='A':
            res+='T'
        elif st[i]=='T':
            res+='A'
        elif st[i]=='C':
            res+='G'
        elif st[i]=='G':
            res+='C'
    
    return res
    
n=int(input())
while n:
    a=input().split()
    st=[i for i in a]
    print(complementDNA(st))
    n-=1
    
    
