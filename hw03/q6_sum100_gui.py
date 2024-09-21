import tkinter as tk
from tkinter import simpledialog, messagebox

def is_even(n):
    return n % 2 == 0

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='숫자 입력', prompt=text)


def main():
    window = tk.Tk()
    window.withdraw()  
    input_num = gui_input("1부터 100까지 짝수의 합은?")
    n = int(input_num)


    total = 0

    for i in range(1, 100):
        if is_even(i):
            total += i


    if n == 2450:
        result = f"정답입니다!"

    else:
        result = f"틀렸습니다! 정답은 {total}입니다"


    messagebox.showinfo("결과", result)


    window.destroy()  


if __name__ == "__main__":
    main()