
# n = int(input())
# s = "12345"
# for i in range(len(s)):
#     s[i]=int(s[i])

# print(s)
n = int(input())
arr = input().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()
ans = set()
for i in range(n-3):
    j,k = i+1, n-1
    while (j<k):
        if arr[i]+arr[j]+arr[k] == 0:
            ans.add([arr[i], arr[j], arr[k]])
            j+=1
            k-=1
        if(arr[i]+arr[j]+arr[k] > 0):
            k-=1
        if(arr[i]+arr[j]+arr[k] < 0):
            j+=1
print(ans)

#you have given a users array,you have to insert a 
#product from products.json 