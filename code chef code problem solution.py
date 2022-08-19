# cook your dish here
a=[]
p=input()  
ulst=p.split() 
for x in range(len(ulst)):
    ulst[x]=int(ulst[x])
for i in range(len(ulst)):
    if ulst[i]>=10:
     a.append(ulst[i])
print(len(a))

