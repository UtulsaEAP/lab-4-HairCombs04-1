"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Bradyn Combs
Lab Time: 2/15/24 2:00 PM
"""

def inc_5():
    # Write your code here
    num1 = int(input())
    num2 = int(input())

    if num1 <= num2:
        while num1 <= num2:
            print(num1, end=' ')
            num1 += 5
        print()
    else:
        print('Second integer can\'t be less than the first.')
    
if __name__ == '__main__':
    inc_5()