#krishnamurthy number
print("krishnamurthy number")
strong_num=input("enter a number : ")

for digit in strong_num:
    digit=int(digit)
    factorial = 1
    for i in range(1,digit+1):
        factorial*=i
    print(f"factorial of {digit} is {factorial}")
