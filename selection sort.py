def sort(num):
    for i in range(len(num)):
        for j in range(i,len(num)):
            if num[j]<num[i]:
                num[i], num[j] = num[j], num[i]

num=[]

def inp():
    n = int(input("Enter number of elements to sort: "))
    for i in range(n):
        a = int(input("Enter element: "))
        num.append(a)

inp()
sort(num)
print("Sorted array is ", num)