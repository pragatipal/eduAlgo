import time

def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'_{"_" * (width + indent * 2)}_\n'  # upper_border
    if title:
        box += f'_{space}{title:<{width}}{space}_\n'  # title
        box += f'_{space}{"-" * len(title):<{width}}{space}_\n'  # underscore
    box += ''.join([f'_{space}{line:<{width}}{space}_\n' for line in lines])
    box += f'_{"_" * (width + indent * 2)}_'  # lower_border
    print(box)

# from __init__ import print_msg_box

# linear search algorithm
def linear_search(array, x, hint=False):
    start = time.time()
    flag=-1
    for i in range(len(array)):
        if array[i] == x:
            flag=i
    end = time.time()
    if (hint == True):
        linear_search_hint()
    print("Linear Search Runtime = {}".format(end - start))
    return flag


def linear_search_hint():
    message = """
    Linear Search
    ------------------------------------
    Purpose : searching a required number
    Method : Iterating, Comparing
    Time Complexity: Worst Case - O(n)
    Hint :
    Starting from 0th element of array[] and comparing every element to x search one by one.
    Pseudocode:
    --> for i in range[0,length of array]
                if(array[i]= x)
                    return i
        return "Not found"
    Visualization:
    Number to search => x=3
    Given Array :
    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+
    First Iteration (i=0):
    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+
    [checking if 5==x, which is not true so going on the next iteration]
    Second Iteration (i=1):
    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+
    [checking if 4==x, which is not true so going on the next iteration]
    Third Iteration (i=2):
    +-----+-----+-----+
    |  5  |  4  |  3  |
    +-----+-----+-----+
    [checking if 3==x, which is true so the search returns location of x in the array ]
    If no element in the array matched x=3 then it would return "Not found"
    Learn More Here - https://en.wikipedia.org/wiki/Linear_search
    """
    print_msg_box(message)
