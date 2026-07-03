def add(*numbers):
    print(numbers)

add(10,20)
add(1,2,3,4,5)


def sum(*k):
    t=0
    for i in k:
        t+=i
    print(t)
sum(1 , 2 , 3,4 , 5) 