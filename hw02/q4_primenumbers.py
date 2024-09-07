from q3_is_primenum import is_prime

def main():
    n = int(input("몇 번까지의 소수를 알고 싶은지 숫자를 입력하시오: "))
    primes = []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    print(primes)


if __name__ == "__main__":
    main()