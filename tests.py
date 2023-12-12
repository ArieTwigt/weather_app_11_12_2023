import pytest
import re


def calc_size(length, width):

    # cast to the right types
    length_float = float(length)
    width_float = float(width)

    # check if the values are positive
    if length_float < 0 or width_float < 0:
        raise ValueError("The values cannot be negative")

    # calculate size
    size = width_float * length_float

    return size


def remove_vowels_text(text):

    text_clean = re.sub(r'[AEOUI]', '', text, flags=re.IGNORECASE)

    #export the file
    with open("text_data/export/export_text.txt", "w") as file:
        file.write(text_clean)

    return text_clean



# execute the tests
def test_calc_size():
    assert calc_size(4, 4) == 16
    assert calc_size("5", 4) == 20


def test_not_negative():
    with pytest.raises(ValueError):
        calc_size(-4, 10)


def test_content_file():
    # raw file, to test
    with open("text_data/test_text.txt", "r") as file:
        test_text_data = file.read()

    # clean file, to compare with
    with open("text_data/test_text_clean.txt", "r") as file:
        test_text_data_clean = file.read()

    # use the function
    remove_vowels_text(test_text_data)
    
    # read the exporte text file
    with open("text_data/export/export_text.txt", "r") as file:
        exported_text_file = file.read()
    
    assert exported_text_file == test_text_data_clean