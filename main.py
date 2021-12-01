from typing import MutableSequence

def bubblesort(a: MutableSequence) -> None:

    n= len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[i-1]>a[j]:
                a[j-1], a[j]=a[j],a[j-1]

if __name__ == '__main__':
    num=int(input('number'))
    x=[None]*num

    for i in range(num):
        x[i]=int(input(f'x[{i}]'))

    bubblesort(x)

    for i in range(num):
        print(f'x[{i}]={x[i]}')