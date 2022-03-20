n= int(input("Enter the numbers:"))
list=[]
even_count=0
odd_count =0
for i in range(1,n+1):
    list.append(i)
    #print(a)
print('Sample numbers:',list)
for num in list:
    if(num%2==0):
        even_count=even_count+1
    elif(num%2 !=0):
        odd_count=odd_count+1  
print("Number of even numbers :",even_count)
print("Number of odd numbers  :",odd_count)          


