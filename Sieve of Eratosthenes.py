#Maurice Koh
#zhi.koh1@marist.edu
#The Sieve of Eratosthenes


def main():
    #n = max number
    #a = all the prime numbers
    #b = other

    n = int(input("Enter a maximum integer: "))
    a = []
    b =[]
    for i in range(2,n+1):
        a.append(i)   
    while len(a)>0:
        prime = a.pop(0)
        print(prime)
        for x in a:
            if x % prime == 0: 
               a.remove(x)
    return b
    print(prime)
    
main()
