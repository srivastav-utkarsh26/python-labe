prime = int(input("Enter a number: "))
if prime > 1:
    for i in range(2, prime):
        if (prime % i) == 0:
            print(prime, "is not a prime number")
            break
    else:
        print(prime, "is a prime number")