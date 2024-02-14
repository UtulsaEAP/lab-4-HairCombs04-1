"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Bradyn Combs
Lab Time: 2:00 PM

"""

def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    if user_num > 0:
        a_str = f'{user_num:b}'
        print(a_str[::-1])

if __name__ == "__main__":
    reverse_binary()