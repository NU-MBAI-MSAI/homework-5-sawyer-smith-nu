## This function takes one argument, a string, that is in the format MM/DD/YYYY.
## The function should the date formatted as YYYY-MM-DD.

def date_format(date_string_to_flip : str) -> str:
    month, day, year = date_string_to_flip.split('/')
    return f"{year}-{month}-{day}"

