def is_even(n):
    return n % 2 == 0

def main():

    total = 0
    for i in range(1, 101):
        if is_even(i):
            total = total + i
    print(f"1부터 100까지 짝수의 합은 {total}입니다.")


if __name__ == '__main__':
    main()