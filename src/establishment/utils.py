from rest_framework.exceptions import ValidationError


def locations_clearance(locations):
    """
    Removes spaces from location str
    Can be modified.
    :param locations:
    :return: str
    """
    result = ''
    for symbol in locations:
        if symbol != ' ':
            result += symbol
    return result


def opening_hours_clearance(opening_hours):
    """
    Checks for correct opening hours (24H format)
    :param opening_hours:
    :return:
    """
    opening_hours = opening_hours.split('-')
    try:
        if ((opening_hours[0].isalnum() == 0 or
             opening_hours[1].isalnum() == 0)
                or (int(opening_hours[0]) not in range(0, 25)
                    or int(opening_hours[1]) not in range(0, 25))):
            raise ValidationError(
                'Invalid opening hour. Should be 0-24'
            )
    except IndexError:
        raise ValidationError(
            'Invalid opening hour. Should be str. Example 7-24'
        )
