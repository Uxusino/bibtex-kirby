class UserInputError(Exception):
    pass

def validate_data(content: dict):
    try:
        int(content['year'])
    except ValueError:
        raise UserInputError("Year must be an integer.")

