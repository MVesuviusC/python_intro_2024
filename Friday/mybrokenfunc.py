# Can use hinting as well, see this : https://docs.python.org/3/library/typing.html
result = 10
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
