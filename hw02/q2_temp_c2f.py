def main():
    temp_c = int(input("섭씨온도를 입력해주세요: "))
    temp_f = 9/5 * temp_c + 32
    print(f"{temp_c}℃ => {temp_f:.1f}℉")

if __name__ == "__main__":
    main()