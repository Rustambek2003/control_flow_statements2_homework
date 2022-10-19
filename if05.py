def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n % 10
    n //= 10

    x2 = n % 10
    n //= 10

    x3 = n % 10
    n //= 10

    x4 = n % 10
    n //= 10

    x5 = n % 10

    s = x1
    if s < x2:
        s = x2
    if s < x3:
        s = x3
    if s < x4:
        s = x4
    if s < x5:
        s = x5
    
    return s
print(main(52698))