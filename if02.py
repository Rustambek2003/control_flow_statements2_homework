def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a < b and a < c:
        s = a
    if b < a and b < c:
        s = b
    if c < a and c < b:
        s = c

    return s