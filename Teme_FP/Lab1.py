# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#ex9/L1
#a) Zerlege eine Zahl in ihre Primfaktoren

# n=int(input("n= "))
# d=2
# while n>1:
#     p=0
#     while n%d==0:
#         p=p+1
#         n=n/d
#
#     if p>0:
#         print (d,"^",p," ")
#     d=d+1

#b)  längste aufeinanderfolgende Teilfolge wobei aufeinanderfolgenden Elemente dieselben Ziffern enthalten
#funktioniert bis jetzt nicht

# l=[2,4,55,123,321,213,45,54,30]
# ct=0
# a=[]
# b=[]
# for i in range (1,len(l)-1):
#     while l[i]>0:
#         a=l[i]%10
#         l[i]=l[i]/10
#     while l[i+1]>0:
#         b=l[i+1]%10
#         l[i+1]=l[i+1]/10
#     for x in range (1,len(a)):
#         if a[x]>a[x+1]:
#             a[x],a[x+1]=a[x+1],a[x]
#     for y in range (1,len(b)):
#         if a[y]>a[y+1]:
#             a[y],a[y+1]=a[y+1],a[y]
#     if a==b:
#         ct=ct+1
# print (ct)

#ex6/L1
#a) Lesen Sie eine Sequenz von natürlichen Zahlen (Sequenz mit 0 beendet) und bestimmen Sie die Anzahl von 0 Ziffern des Produkts der gelesenen Zahlen
# n=not 0
# v=[]
# while n!=0:
#     n=int(input("n= "))
#     v.append(n)
# p=1
# a=1
# ct=0
# for i in range (0,len(v)-1):
#     p=p*v[i]
#     a=a*v[i] # eine Kopie von p um am Ende das Produkt anzuzeigen
# while p>9:
#     if p%10==0:
#         ct=ct+1
#     p=p/10
# print ("Das Produkt der gelesen Zahlen ist ",int(a))
# print ("Die 0 Ziffern Anzahl ist ",ct)

#b) längste  zusammenhängende  Teilfolge  so, dass die Summe von zwei aufeinanderfolgenden Elementen eine Primzahl ist
# funktioniert nicht
# l=[3,5,2,9,4,3,10,5,9,4]
# a=l[0]
# c=l[1]
# s=a+c
# rezultat=[]
# temp=[]
# for i in range (2,len(l)-1):
#     ct=0
#     for d in range (1,s):
#         if s%d==0:
#             ct=ct+1
#     if ct==2:
#         temp.append(a)
#     elif len(temp)>len(rezultat):
#         rezultat = temp
#         temp = []
#     a=c
#     c=l[i]
#     s=a+c
# print (rezultat)

#ex11/L1
#a) die ersten n Paare von Zwillingszahlen, wobei n eine gegebene natürliche Zahl und keine Nullzahl ist. Zwei Primzahlen p und q heißen twin, wenn q -p = 2 ist

# n=int(input("n= "))
# ct=0
# q=5
# p=3
#
# def qIsPrime(q):
#     for i in range (2,q):
#         if q%i==0:
#             return False
#     return True
#
# def pIsPrime(p):
#     for i in range (2,p):
#         if p%i==0:
#             return False
#     return True
#
# while n!=ct:
#     if qIsPrime(q) and pIsPrime(p) and q-p==2:
#         print("(",q,",",p,")")
#         ct=ct+1
#     q=q+1
#     qIsPrime(q)
#     p=p+1
#     pIsPrime(p)

# b) finde die am längsten abnehmende aufeinanderfolgende Teilfolge
# l=[2,3,4,3,2,1,7,12,9,8,7,4,3,10,11,8,7,6,5]
# temp=[]
# rez=[]
# for i in range (1,len(l)):
#     if l[i-1]>l[i]:
#         temp.append(l[i-1])
#     elif len(temp)>len(rez):
#         temp.append(l[i-1])
#         rez=temp
#         temp=[]
# print (rez)

# ex8/L1
# a) Bestimmen Sie den Wert x ^ n
# def ex8a():
#
#     x=float(input("x= "))
#     n=int(input("n= "))
#     m=1
#     i=1
#     if n==1:
#         print (int(x))
#     else:
#         while i<=n:
#             m=m*x
#             i=i+1
#     print (m)
#
# ex8a()

# b)  die längste aufeinanderfolgende Teilfolge wobei jede zwei aufeinanderfolgende Elemente entgegengesetzte Vorzeichen haben
def ex8b():
    l=[1,3,-2,4,-5,-6,4,-3,2,-1,5,-5,6,-2,5,-6,2]
    #a=l[0]
    #c=l[1]
    temp=[]
    rez=[]

    for i in range (0,len(l)-1):
        if l[i]>0 and l[i+1]<0 or l[i]<0 and l[i+1]>0:
            temp.append(l[i])
        elif len(temp)>len(rez):
            temp.append(l[i])
            rez=temp
            temp=[]

    if len(temp)>len(rez):
        #temp.append(l[i])
        rez=temp
        #temp=[]
    if l[-1]<0 and l[-2]>0 or l[-1]>0 and l[-2]<0:
        temp.append(l[-1])
    if len(temp)>len(rez):
        rez = temp
        temp = []

    print (rez)


ex8b()