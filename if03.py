def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a >= b and b >= c) or (c >= b and b >= a):
        s = b
    if (b >= a and a >= c) or (c >= a and a >= b):
        s = a
    if (b >= c and c >= a) or (a >= c and c >= b):
        s = c
    return s
print(main(5,5,5))