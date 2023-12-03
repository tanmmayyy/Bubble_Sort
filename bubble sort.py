def bubble_sort():
    n=int(input("Enter the number of elements in the list: "))
    l=[]

    for i in range(1,n+1):
        ele=int(input("Enter the element: "))
        l.append(ele)
        
    for i in range (0,len(l)):
        for j in range(0,i):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
    print("The sorted list is:",l)

bubble_sort()
