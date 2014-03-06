import numpy as np

def bin(a):

    return 2.**(-a)

b = []

c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print

n=input('Enter a float number smaller than 1: ')

x = str(n)

res = n

num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

for i in num:

    if bin(i) <= res:

        b.append(i)

        res = res - bin(i)


for i in b:

    c[i-1]=1

k='0.'

for i in c:

    k=k+str(i)

print
print 'In Binary:'
print
print k

        


        

        
