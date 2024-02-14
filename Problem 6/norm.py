"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Bradyn Combs
Lab Time: 2/15/24 2:00 PM
"""

def norm():
    # Write your code here
    num = input()
    nums_entered = []
    for n in range(int(num)):
        val = float(input())
        nums_entered.append(val)
        if(n == 0):
            max = val
        else:
            if val > max:
                max = val
    for val in nums_entered:
        your_value = val/max
        print(f'{your_value:.2f}')

if __name__ == "__main__":
    norm()