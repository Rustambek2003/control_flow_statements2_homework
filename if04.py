from pkg_resources import safe_extra


def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a == b:
        s = 0
    else:
        if a > b:
            s = a
        else:
            s = b
    return s