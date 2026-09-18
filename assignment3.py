def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


def check_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"


num = int(input("Enter an integer: "))
print(f"{num} is {check_even_odd(num)}.")
print(f"{num} is {check_prime(num)}.")