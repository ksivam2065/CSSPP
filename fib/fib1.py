import sys


total =3

#recursively count down
#ex if x=5 output 1 2 3 4 5 
def myfunction(x):
    if(x==0):
       return 0
    else:
        print(myfunction(x-1))
        return x

#going up to ex : x=10
def myfunction2(x):
    if(x>=10):
        return 10
    else:
        print(myfunction2(x+1))
        return x
        

#fibnanci sequence up to a certain count
#fib_place 6 output 0 1 1 2 3 5
def fib_place(x):
    if(x > 2):
        return fib_place(x-2)+ fib_place(x-1)
    else:
        return x
    

#print(fib_place(1))
#myfunction(5)
#myfunction2(1)

def main():
    print("hello")
    #print(fib_place(int(argv[1])))


if __name__=="__main__":
    main ()
