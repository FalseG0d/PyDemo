n=int(input("Enter the limit"))

for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    for k in range(2*(i-1)-1):
        if i==1:
            break
        print('*', end=" ")
    print("")


