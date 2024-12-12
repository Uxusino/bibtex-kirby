import pytest
from datetime import datetime
from util import UserInputError, validate_data, generate_label, parse_request, parse_tags, filter_bibtexs, sort_bibtexs

def test_validate_data_valid():
    content = {'year': str(datetime.now().year)}
    validate_data(content)  # Should not raise an exception

def test_validate_data_invalid_year():
    content = {'year': '0'}
    with pytest.raises(UserInputError):
        validate_data(content)

def test_validate_data_non_integer_year():
    content = {'year': 'abcd'}
    with pytest.raises(UserInputError):
        validate_data(content)

def test_generate_label():
    content = {'author': 'Doe, John', 'title': 'A Great Book', 'year': '2021'}
    label = generate_label(content)
    assert label == 'doe_a_2021'

def test_parse_request():
    content = {'type': 'book', 'author': 'Doe, John', 'title': 'A Great Book', 'year': '2021'}
    result = parse_request(content)
    assert result['label'] == 'doe_a_2021'
    assert result['type'] == 'book'
    assert result['data'] == {'author': 'Doe, John', 'title': 'A Great Book', 'year': '2021'}
    assert result['tags'] is None

def test_parse_request_with_tags():
    content = {'type': 'book', 'author': 'Doe, John', 'title': 'A Great Book', 'year': '2021', 'tags': 'tag1, tag2'}
    result = parse_request(content)
    assert result['label'] == 'doe_a_2021'
    assert result['type'] == 'book'
    assert result['data'] == {'author': 'Doe, John', 'title': 'A Great Book', 'year': '2021'}
    assert result['tags'] == ['tag1', 'tag2']

def test_parse_request_invalid_data():
    content = {'type': 'book', 'author': 'Doe, John', 'title': 'A Great Book', 'year': 'abcd'}
    with pytest.raises(UserInputError):
        parse_request(content)

def test_parse_tags():
    tags_string = "tag1, tag2, tag3"
    tags = parse_tags(tags_string)
    assert tags == ["tag1", "tag2", "tag3"]

def test_filter_bibtexs():
    class MockBibtex:
        def __init__(self, author, title):
            self.data = {'author': author, 'title': title}

    bibtexs = [
        MockBibtex('John Doe', 'A Great Book'),
        MockBibtex('Jane Doe', 'Another Book'),
        MockBibtex('John Smith', 'Yet Another Book')
    ]

    result = filter_bibtexs(bibtexs, 'john')
    assert len(result) == 2
    assert result[0].data['author'] == 'John Doe'
    assert result[1].data['author'] == 'John Smith'

def test_filter_bibtexs_regex():
    class MockBibtex:
        def __init__(self, author, title):
            self.data = {'author': author, 'title': title}

    bibtexs = [
        MockBibtex('John Doe', 'A Great Book'),
        MockBibtex('Jane Doe', 'Another Book'),
        MockBibtex('John Smith', 'Yet Another Book')
    ]

    result = filter_bibtexs(bibtexs, 'j.hn')
    assert len(result) == 2
    assert result[0].data['author'] == 'John Doe'
    assert result[1].data['author'] == 'John Smith'

    result2 = filter_bibtexs(bibtexs, '^Another')
    assert len(result2) == 1
    assert result2[0].data['author'] == 'Jane Doe'



def test_sort_bibtexs():
    class MockBibtex:
        def __init__(self, title, year, creation_time):
            self.data = {'title': title, 'year': year}
            self.creation_time = creation_time

    bibtexs = [
        MockBibtex('C Book', '2021', '2021-01-01'),
        MockBibtex('A Book', '2020', '2020-01-01'),
        MockBibtex('B Book', '2022', '2022-01-01')
    ]

    result = sort_bibtexs(bibtexs, 'label', False)
    assert result[0].data['title'] == 'A Book'
    assert result[1].data['title'] == 'B Book'
    assert result[2].data['title'] == 'C Book'

    result = sort_bibtexs(bibtexs, 'year', False)
    assert result[0].data['year'] == '2020'
    assert result[1].data['year'] == '2021'
    assert result[2].data['year'] == '2022'

    result = sort_bibtexs(bibtexs, 'year', True)
    assert result[0].data['year'] == '2022'
    assert result[1].data['year'] == '2021'
    assert result[2].data['year'] == '2020'

    result = sort_bibtexs(bibtexs, 'creation_time', False)
    assert result[0].creation_time == '2020-01-01'
    assert result[1].creation_time == '2021-01-01'
    assert result[2].creation_time == '2022-01-01'