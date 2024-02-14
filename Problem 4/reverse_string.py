"""
Complete the following python code to reverse the string entered by the user.

Name: Bradyn Combs
Lab Time: 2/15/24 2:00 PM
"""

def reverse_string():
    # YOUR CODE HERE
    var1 = str(input())
    bad_word = ['done', 'd', 'Done']
    while var1 not in bad_word:
        print(var1[::-1])
        var1 = str(input())

if __name__ == "__main__":
    reverse_string()