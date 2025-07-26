# Sum of Even Numbers upto given number n

n = int(input("Enter a number: "))
sum_even = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += i
print(f"Sum of even numbers from 1 to {n}, is: {sum_even}")