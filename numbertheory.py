def getprimes(number):
    primes = []
    primes.append(2)
    primes.append(3)

    for n in range(4, number**2):
        works = True
        for prime in primes: 
            if n/prime == n//prime:
                works = False
                break
            else:
                continue
        if works == True:
            primes.append(n)
    return primes

def main():
    number = int(input("To what number? "))
    primes = getprimes(number)

    workingnumbers = []
    for c in range (42, number):
        d = True
        for n in range(0, c - 1):
            if (n**2 + n + c) not in primes:
                d = False
                break
        if d == True:
            workingnumbers.append(c)

    print(workingnumbers)

main()