"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Bradyn Combs
Lab Time: 2/15/24 2:00 PM
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.
    word = word.replace('i','1')
    word = word.replace('a','@')
    word = word.replace('m','M')
    word = word.replace('B','8')
    word = word.replace('s','$')
    word = word + '!'
    print(word)

if __name__ == "__main__":
    password_mod()