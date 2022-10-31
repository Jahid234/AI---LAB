n = int(input("Enter the number: "))

for i in range(n+1):    
    print((n - i) * " ", end=" ")
    print((2*i-1)* "*")