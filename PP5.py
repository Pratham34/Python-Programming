# Problem Statement:-
# You are given a list that contains some numbers. You have to print a list of the next palindromes only if the number is greater than 10; otherwise, you will print that number.
#
# Input:
# [1, 6, 87, 43]
#
# Output:
# [1, 6, 88, 44]

def next_palindrome(n):
    if n >10:
        n += 1
        while not is_palindrome(n):
            n += 1
        return n
    return n
def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(n):
        numbers[i] = next_palindrome(numbers[i])

    print(f"The required list is {numbers}")
