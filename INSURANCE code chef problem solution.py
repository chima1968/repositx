# cook your dish here

t=int(input())
while t>0:
    p=input()
    ulst=p.split()
  
    for x in range(len(ulst)):
        ulst[x]=int(ulst[x])
        
        for y in range(x+1,len(ulst)):
             ulst[y]=int(ulst[y])
             if(ulst[x]>ulst[y]):
                  print(ulst[y])
             elif (ulst[x]<ulst[y]):
                 print(ulst[x])
             else:
                print(ulst[x])
        
    t-=1

for i in range(len(ulst)):
    print(ulst[i])