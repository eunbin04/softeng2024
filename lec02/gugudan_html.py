
def main():
    dan = 5
    print("구구단을 출력합니다.")
    with open("gugudan.html", "w") as f:
        f.write("<table border='1'>\n")
        for j in range(1,10):
            f.write(f"<tr><td>{dan} X {j} = <strong>{dan * j}</strong></td></tr>\n")
        f.write("</table>\n")

if __name__ == "__main__":
    main()