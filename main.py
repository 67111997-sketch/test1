# main.py

from myfunc import add
from myfunc2 import add

def main():
    # ตัวอย่างการใช้
    a = float(input("ป้อนค่า A: "))
    b = float(input("ป้อนค่า B: "))
    result = add(a, b)
    print(f"ผลลัพธ์ของ {a} + {b} คือ {result}")

if __name__ == "__main__":
    main()