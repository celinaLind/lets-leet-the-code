# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks. 

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
    # use integer division (cuts off the remainder)
    # 8 // 5 => 1
    max_big = goal // 5
    # set max_big equal to the number of big bricks provided if there are more in max_big
    if max_big > big:
        max_big = big
    
    remainder = goal - (max_big * 5) # subtract goal by the max value of big

    return small >= remainder