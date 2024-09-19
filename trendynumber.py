***
Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
If the given number is a trendy number, then print "Trendy Number". Otherwise, print "Not a Trendy Number".
Refer the sample output for formatting.
Sample Input:
791
Sample Output:
Trendy Number
***
def is_trendy_number(n):
    if 100 <= n <= 999:
        middle_digit = (n // 10) % 10
        if middle_digit % 3 == 0:
            return "Trendy Number"
    return "Not a Trendy Number"
n = int(input())
print(is_trendy_number(n), "program")
