def leap_year(year):
    """
    Figures out if the year is a leap year or not
    """
    if (year % 400) == 0 or ((year % 100) > 0 and (year % 4) == 0):
        return True
    return False
