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
    if a >= b and b >= c:
        s = b
    if b >= a and a >= c:
        s = a
    if b >= c and c >= a:
        s = c
    return s
print(main(5,5,-1))