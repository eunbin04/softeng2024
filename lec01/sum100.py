from lec01.odd_even import is_even


def main():
    total = 0

    for i in range(1, 101):
        #total = total + i
        if is_even(i):
            total += i
    print(f"1부터 100까지 짝수의 합은 {total}입니다.")

    even_100 = [i for i in range(1, 101) if is_even(i)]
    print(f"1부터 100까지 짝수의 합은 {sum(even_100)}입니다.")


if __name__ == '__main__':
    main()
