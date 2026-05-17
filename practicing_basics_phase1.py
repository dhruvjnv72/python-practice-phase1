'''1 FizzBuzz with a twist '''

# for j in range(1,1001): 
#     if j%3==0 and j%5==0 and j%7==0 : 
#         print("FizzBuzzWhiz")
#     elif j%3==0 and j%5==0 : 
#         print("FizzBuzz")
#     elif j%3==0 and j%7==0 :
#         print("FizzWhiz")
#     elif j%3==0 :
#         print("Fizz")
#     elif j%5==0 :
#         print("Buzz")
#     elif j%7==0 :
#         print("Whiz")
#     else : 
#         continue

''' 2. Pyramid printer '''

# n=int(input())
# for j in range(n): 
#     print(" "*(n-j-1),end="")
#     print("*"*(2*j+1),end="")
#     print(" "*(n-j-1))

''' 3. Number pattern '''

# n=int(input())
# for j in range(1,n+1): 
#     for i in range(j):
#         print(i+1,end=" ") 
#     print()

''' 4. Collatz conjecture '''

# n=int(input())
# while n!=1 : 
#     print(n,end=" ")
#     if n%2==0 : 
#         n//=2
#     else : 
#         n=(n*3)+1
# print(1)

''' #5 Prime sieve '''

# n=int(input())
# sieve=[True]*(n+1)
# sieve[0],sieve[1]=False,False
# for i in range(2,n): 
#     if sieve[i]:
#         for j in range(i,n//(i)+1):
#             sieve[j*i]=False
# prime=[]
# for j in range(n+1) :
#     if sieve[j] :
#         prime.append(j)
# print(prime)

# n=int(input())
# sieve=[True]*(n+1)
# sieve[0],sieve[1]=False,False
# for i in range(2,n): 
#     if sieve[i]:
#         for j in range(i*i,n+1,i): 
#             sieve[j]=False
# prime=[]
# for j in range(n+1) :
#     if sieve[j] :
#         prime.append(j)
# print(prime)

''' 6. Pascal's triangle '''

# n=int(input())
# pascal=[]
# for j in range(n): 
#     rt=[]
#     print(" "*(n-j-1),end="")
#     for i in range(j+1): 
#         if i==0 or i==(j) : 
#             rt.append(1) 
#             print(1,end=" ")
#         else : 
#             my=pascal[j-1][i]+pascal[j-1][i-1]
#             rt.append(my)
#             print(my,end=" ")
#     print()
#     pascal.append(rt)

''' #7 Caesar cipher'''

# import string 
# alpha = string.ascii_lowercase
# encrypt=input()
# encryptby=int(input())
# decrypt=input()
# decryptby=int(input())
# for i in range(len(encrypt)): 
#     if encrypt[i].lower() in alpha : 
#         rty=alpha[(alpha.index(encrypt[i].lower())+encryptby)%26]
#         print(rty.upper() if encrypt[i].isupper() else rty,end="")
#     else : 
#         print(encrypt[i],end="")
# print()
# for j in range(len(decrypt)): 
#     if decrypt[j].lower() in alpha :
#         rty=alpha[(alpha.index(decrypt[j].lower())-decryptby)%26] 
#         print(rty.upper() if decrypt[j].isupper() else rty,end="")
#     else : 
#         print(decrypt[j],end="")
# print()

''' #8 Anagram checker '''

# x=input()
# y=input() 
# dicti1={}
# dicti2={}
# for char in x : 
#     er=char.lower()
#     if er!=" " :
#         if er in dicti1: 
#             dicti1[er]+=1
#         else : 
#             dicti1[er]=1
# for chr in y : 
#     ep=chr.lower()
#     if ep!=" " : 
#         if ep in dicti2: 
#             dicti2[ep]+=1
#         else : 
#             dicti2[ep]=1
# print(dicti1,dicti2)
# if dicti1==dicti2 : 
#     print("YES")
# else : 
#     print("NO")

# x=input().split()
# dic=[]
# for chr in x : 
#     dicti1={}
#     for char in chr : 
#         er=char.lower()
#         if er!=" " :
#             if er in dicti1: 
#                 dicti1[er]+=1
#             else : 
#                 dicti1[er]=1
#     dic.append(dicti1)
# fro=[True]*(len(x))
# lst=[]
# for j in range(len(x)): 
#     if fro[j] : 
#         lstr=[]
#         for i in range(j,len(x)):
#             if dic[i]==dic[j] :
#                         fro[i]=False
#                         lstr.append(x[i])
#         lst.append(lstr)
# print(lst)

# x=input().split()
# dic={}
# for char in x : 
#     key="".join(sorted(char.lower()))
#     if key in dic : 
#         dic[key].append(char)
#     else : 
#         dic[key]=[char]
# print(str(list(dic.values())).replace(" ",""))

''' #9 String compression '''

x=input()
stri=""
r=1
for char in range(1,len(x)) :
    if x[char]==x[char-1]: 
        r+=1 
    else : 
        if r==1 : 
            stri+=x[char-1]
        else : 
            stri+=(x[char-1])
            stri+=str(r)
        r=1
if r==1 : 
    print(stri+x[-1])
else : 
    print(stri+x[-1]+str(r))




