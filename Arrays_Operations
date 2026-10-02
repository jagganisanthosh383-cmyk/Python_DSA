#1st problem - sum of array

'''def sumofArray(a):
  sum=0
  for i in a:
    sum=sum+i
  return sum

n=int(input())
a=list(map(int,input().split()))

print(sumofArray(a))'''


#2nd problem - search

'''def search(a,el):
  c=0
  for i in a:
    if el==i:
      c=c+1
  return c

n=int(input())
a=list(map(int,input().split()))
ele=int(input())

print(search(a,ele))'''


#3rd problem - average

'''n=int(input())
a=list(map(int,input().split()))

sumvalue=0

for i in a:
  sumvalue=sumvalue+i

res=sumvalue/n

print(res)
print(f'{res:.2f}')'''


#4th problem - remove vowels

'''def remove(string):
  result=""

  for ch in string:
    if ch!='a' and ch!='e' and ch!='i' and ch!='o' and ch!='u':
      result=result+ch

  return result

string=input()

result=remove(string)

print(result)'''


#5th problem - traversal

'''def traversal(a):
  print('[',end="")

  for i in range(len(a)-1):
    print(a[i],end=", ")

  print(f'{a[-1]}]')

a=list(map(int,input().split()))

traversal(a)'''


#6th problem - insertion of array

'''def insert(ar,el,ind):
  ar2=[0 for i in range(len(ar)+1)]

  for i in range(ind):
    ar2[i]=ar[i]

  for i in range(ind,len(ar)):
    ar2[i+1]=ar[i]

  ar2[ind]=el

  return ar2

n=int(input())
a=list(map(int,input().split()))[:n]

print(a)

el=int(input())
ind=int(input())

a=insert(a,el,ind)

print(a)'''


#7th problem - deletion of array

'''def delete(ar,ind):
  ar2=[0 for i in range(len(ar)-1)]

  for i in range(ind):
    ar2[i]=ar[i]

  for i in range(ind,len(ar)-1):
    ar2[i]=ar[i+1]

  return ar2

n=int(input())
a=list(map(int,input().split()))[:n]

print(a)

ind=int(input())

a=delete(a,ind)

print(a)'''


#8th problem - right rotation

'''def rotation(a,key):
  ar=[0 for i in range(len(a))]
  ind=0

  key=key%len(a)

  for i in range(len(a)-key,len(a)):
    ar[ind]=a[i]
    ind=ind+1

  for i in range(len(a)-key):
    ar[ind]=a[i]
    ind=ind+1

  return ar

n=int(input())
a=list(map(int,input().split()))[:n]

print(a)

key=int(input())

a=rotation(a,key)

print(a)'''


#9th problem - left rotation

'''def rotation(a,key):
  ar=[0 for i in range(len(a))]
  ind=0

  key=key%len(a)

  for i in range(key,len(a)):
    ar[ind]=a[i]
    ind=ind+1

  for i in range(key):
    ar[ind]=a[i]
    ind=ind+1

  return ar

n=int(input())
a=list(map(int,input().split()))[:n]

print(a)

key=int(input())

a=rotation(a,key)

print(a)'''


#10th problem - sliding window

'''def maxsubarray(a,k):
  sum=0

  for i in range(k):
    sum=sum+a[i]

  max=sum

  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]

    if sum>max:
      max=sum

  return max

a=list(map(int,input().split()))
k=int(input())

print(maxsubarray(a,k))'''


#11th problem - linear search

'''def linearsearch(a,ele):
  ar=[]

  for i in range(len(a)):
    if a[i]==ele:
      ar.append(i)

  return ar

a=list(map(int,input().split()))
ele=int(input())

print(linearsearch(a,ele))'''


#12th problem - remove duplicates

'''def remove_duplicates(arr):
  ar=[]

  for i in arr:
    if i not in ar:
      ar.append(i)

  return ar

a=list(map(int,input().split()))

print(remove_duplicates(a))'''


#13th problem - container with water

'''def max_water_container(heights):
  left=0
  right=len(heights)-1
  max_water=0

  while left<right:
    width=right-left
    height=min(heights[left],heights[right])

    water=width*height

    if water>max_water:
      max_water=water

    if heights[left]<heights[right]:
      left=left+1
    else:
      right=right-1

  return max_water

a=list(map(int,input().split()))

print(max_water_container(a))'''


#14th problem - sum of sub array

'''def max_sum_subarray(arr,k):
  sum=0

  for i in range(k):
    sum=sum+arr[i]

  max=sum

  for i in range(k,len(arr)):
    sum=sum-arr[i-k]+arr[i]

    if sum>max:
      max=sum

  return max

a=list(map(int,input().split()))
k=int(input())

print(max_sum_subarray(a,k))'''


#15th problem - smallest subarray

'''def min_subarray_with_sum(arr,target):
  min_length=len(arr)+1
  sum=0
  start=0

  for end in range(len(arr)):
    sum=sum+arr[end]

    while sum>=target:
      length=end-start+1

      if length<min_length:
        min_length=length

      sum=sum-arr[start]
      start=start+1

  if min_length==len(arr)+1:
    return 0

  return min_length

a=list(map(int,input().split()))
target=int(input())

print(min_subarray_with_sum(a,target))'''


#16th problem - prefix array

'''def prefixarray(a):
  ar=[0 for i in range(len(a))]
  s=0

  for i in range(len(a)):
    s=s+a[i]
    ar[i]=s

  return ar

a=list(map(int,input().split()))

print(prefixarray(a))'''


#17th problem - range sum

'''def prefixarray(a):
  ar=[0 for i in range(len(a))]
  s=0

  for i in range(len(a)):
    s=s+a[i]
    ar[i]=s

  return ar


def range_sum(a,st,end):
  if st==0:
    return a[end]

  return a[end]-a[st-1]


a=list(map(int,input().split()))

prefix=prefixarray(a)

print(prefix)

st=int(input())
end=int(input())

print(range_sum(prefix,st,end))'''


#18th problem - sub array sum equals target

def sumarray(a,k,target):
  s=0

  if k<=0 or k>len(a):
    return -1

  for i in range(k):
    s=s+a[i]

  if s==target:
    return [a[i] for i in range(k)]

  for i in range(k,len(a)):
    s=s+a[i]-a[i-k]

    if s==target:
      return [a[j] for j in range(i-k+1,i+1)]

  return -1


a=list(map(int,input().split()))
k=int(input())
target=int(input())

print(sumarray(a,k,target))