l = list(map ( int , input("Enter the elements: ").split()))
for i in l:
    if (i%2)==0:
        continue
    else:
        print(i)