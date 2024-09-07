def main():
    n = int(input("팩토리얼을 구할 숫자를 입력해주세요: "))

    if n > 0:
        num = 1
        for i in range(1, n+1):
            num = num * i
        print(f"{n}! = {num} 입니다.")

    else:
        print("자연수를 입력해주세요.")


if __name__ == '__main__':
    main()