x,y = [int(x) for x in input("Enter day 1, day 2 of the same year:").split(",")]
def week_elapsed(x:int, y:int) -> int: 
    return ((abs(x - y) + 1) // 7)
print (week_elapsed(x,y))