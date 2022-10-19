def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number == 1:
        s = "Monday"
    if number == 2:
        s = "Tuesday"
    if number == 3:
        s = "Wednesday"
    if number == 4:
        s = "Thursday"
    if number == 5:
        s = "Friday"
    if number == 6:
        s = "Saturday"
    if number == 7:
        s = "Sunday"
    return s