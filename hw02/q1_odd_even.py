def main():
    n = int(input("숫자를 입력하세요: "))

    if n % 2 == 0:
        print(f"{n}은 짝수입니다.")
        if n == 0:
            print(f"{n}은 0입니다.")

    elif n < 0:
            print(f"{n}은 홀수도 짝수도 아닙니다.")

    else:
        print(f"{n}은 홀수입니다.")


if __name__ == "__main__":
    main()