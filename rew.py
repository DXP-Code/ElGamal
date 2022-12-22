import random
from math import pow,gcd



def rand_prime():
    while True:
        p = random.randrange(1000001, 10000000,
                             2)  # randrange - возвращает случайное целое число в заданном диапазоне, т.е. начало и конец.
        if all(p % n != 0 for n in range(3, int((pow(p, 0.5)) + 1), 2)):
            return p

#To fing gcd of two numbers
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)
#For key generation i.e. large random number
def gen_key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key
def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c
#For asymetric encryption
def encryption(msg,q,h,g):
    ct=[]
    k=gen_key(q)
    s=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    print("g^k used= ",p)
    print("g^ak used= ",s)
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,p
#For decryption
def decryption(ct,p,key,q):
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt


a= rand_prime()
msg=input("Введите текст:")
q=random.randint(pow(10,20),pow(10,50))
print(q)
g=random.randint(2,q)
print(g)
key=gen_key(q)
h=power(g,key,q)
print("g= ",g)
print("g^a= ",h)
ct,p=encryption(msg,q,h,g)
print(p)
print("Оригинальное сообщение: ",msg)
print("Зашифрованое сообщение: ",ct)
pt=decryption(ct,p,key,q)
d_msg=''.join(pt)
print("Расшифрованое сообщение: ",d_msg)
