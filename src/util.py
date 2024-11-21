from datetime import datetime
import re, string

class UserInputError(Exception):
    pass

def validate_data(content: dict):
    try:
        current_year = datetime.now().year
        year = int(content['year'])

        if year <= 1 or year > current_year:
            raise UserInputError("Invalid year.")
        
    except ValueError:
        raise UserInputError("Year must be an integer.")
    
# Turns data into a unique label
def generate_label(content: dict[str]) -> str:
    author = re.split(', | ', content['author'])[0].lower()
    title = content['title']
    # Deletes punctuation
    title = title.translate(str.maketrans('', '', string.punctuation))
    title = title.split()[0].lower()
    
    year = content['year']
    label = f"{author} {title} {year}"
    return label

