# test_day_02_part_02.py

from day_02_part_02 import find_common_letters

def test_find_common_letters():
    box_ids = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz'
    ]
    expected_output = 'fgij'
    assert find_common_letters(box_ids) == expected_output
