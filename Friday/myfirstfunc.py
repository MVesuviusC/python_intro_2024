# Can use hinting as well, see this : https://docs.python.org/3/library/typing.html
def add(x,y):
    """Add two numbers

    Args :
        x : (int, float)
        y : (int, float)

    Returns :
        val : (int, float)

    Raises :
    """
    val = x + y
    return val

### Global variables are you enemy
def main():
    """Main driver function

    """
    a = 3
    b = 19
    value = add(a,b)
    print("Sum of {} + {} = {}".format(a,b,value))


if __name__ == "__main__":
    main()
