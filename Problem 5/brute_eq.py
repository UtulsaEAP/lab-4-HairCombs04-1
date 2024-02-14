"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Bradyn Combs
Lab Time: 2/15/24 2:00 PM
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    # YOUR CODE HERE
    # created a boolean variable and set it to false 
    check_solution = False
    # loop
    for x in range(-10, 10, 1):
        for y in range(-10, 10, 1):
            # condition if any values of x and y within the range
            # satisfies the expresssions then check_solution will become true
            # and solution will exist
            if a * x + b * y == c and d * x + e * y == f:
                check_solution = True
                print("x = {} , y = {}".format(x,y))

    # condition not satisfied
    if check_solution == False:
        print('There is no solution')
    
if __name__ == "__main__":
    brute_eq()