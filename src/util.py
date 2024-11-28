"""
This module provides utility functions for validating and processing bibliographic data.
Classes:
    UserInputError(Exception): Custom exception for user input errors.
Functions:
    validate_data(content: dict):
        Validates the 'year' field in the provided content dictionary.
        Raises UserInputError if the year is invalid or not an integer.
    generate_label(content: dict[str]) -> str:
        Generates a unique label for the bibliographic entry based on the author's last name,
        the first word of the title, and the year.
    parse_request(content: dict[str]) -> dict:
        Parses the request content, validates the data, generates a label, and returns a new
        bibliographic entry dictionary containing the label, type, and data.
"""
from datetime import datetime
import re
import string

class UserInputError(Exception):
    pass

def validate_data(content: dict):
    """
    Validates the 'year' field in the given content dictionary.
    Args:
        content (dict): A dictionary containing the data to be validated. 
                        It must include a 'year' key with a string value.
    Raises:
        UserInputError: If the 'year' is not an integer, or if it is less than or equal to 1, 
                        or if it is greater than the current year.
    """
    try:
        current_year = datetime.now().year
        year = int(content['year'])

        if year <= 1 or year > current_year:
            raise UserInputError("Invalid year.")

    except ValueError as exc:
        raise UserInputError("Year must be an integer.") from exc

def generate_label(content: dict[str]) -> str:
    """
    Generates a label for a bibliographic entry based on the author, title, and year.

    Args:
        content (dict[str]): A dictionary containing 'author', 'title', and 'year' keys.

    Returns:
        str: A label in the format 'author_title_year', where 'author' is the lowercase
             surname of the first author, 'title' is the lowercase first word of the title
             with punctuation removed, and 'year' is the publication year.
    """
    author = re.split(', | ', content['author'])[0].lower()
    title = content['title']
    title = title.translate(str.maketrans('', '', string.punctuation))
    title = title.split()[0].lower()

    year = content['year']
    label = f"{author}_{title}_{year}"
    return label

def parse_request(content: dict[str]) -> dict:
    """
    Parses a request dictionary to generate a new bibliography entry.

    Args:
        content (dict[str]): A dictionary containing the request data. 
                             It should include a "type" key and other relevant data.

    Returns:
        dict: A dictionary representing the new bibliography entry with keys:
              - "label": A generated label for the entry.
              - "type": The type of the entry.
              - "data": The filtered data from the input content.

    Raises:
        Exception: If the data validation fails.
    """
    ref_type = content.get("type")
    data = {k: v for k, v in content.items() if v and k != "type"}
    try:
        validate_data(content)
    except Exception as error:
        raise error
    label = generate_label(data)

    new_bib = {
        "label": label,
        "type": ref_type,
        "data": data
    }

    return new_bib

def filter_bibtexs(bibtexs, query):
    return list(filter(lambda b: query.lower() in b.data["author"].lower()
                          or query.lower() in b.data["title"].lower(), bibtexs))
