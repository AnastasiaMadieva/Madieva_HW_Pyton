import pytest
from StringUtils import StringUtils

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("hello world", "Hello world"),
    ],
)
def test_capitalize_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.capitilize (input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", ""), ("    ", "    ")],
)
def test_capitalize_negative(input_text, expected_output):
    processor = StringUtils()
    assert processor.capitilize(input_text) == expected_output

@pytest.mark.parametrize (
    "input_text, expected_output",
    [("    hello", "hello"), ("    123", "123")],
)
def test_trim (input_text, expected_output):
    processor = StringUtils()
    assert processor.trim(input_text) == expected_output

@pytest.mark.parametrize (
    "input_text, expected_output",
    [("1,2,3,4", ["1", "2", "3", "4"]), ("a,b,c,d", ["a", "b", "c", "d"])], 
)
def test_to_list (input_text, expected_output):
    processor = StringUtils()
    assert processor.to_list(input_text) == expected_output

@pytest.mark.parametrize (
    "input_text, simbol, expected_output",
    [("SkyPro", "S", True), ("SkyPro", "U", False)], 
)
def test_contains (input_text, simbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_text, simbol) == expected_output

@pytest.mark.parametrize (
    "input_text, simbol, expected_output",
    [("SkyPro", "S", "kyPro"), ("SkyPro", "P", "Skyro")], 
)
def test_delete_simbol (input_text, simbol, expected_output):
    processor = StringUtils()
    assert processor.delete_symbol(input_text, simbol) == expected_output

@pytest.mark.parametrize (
    "input_text, simbol, expected_output",
    [("SkyPro", "S", True), ("SkyPro", "U", False)], 
)
def test_start_with (input_text, simbol, expected_output):
    processor = StringUtils()
    assert processor.starts_with(input_text, simbol) == expected_output


@pytest.mark.parametrize (
    "input_text, simbol, expected_output",
    [("SkyPro", "o", True), ("SkyPro", "U", False)], 
)
def test_end_with (input_text, simbol, expected_output):
    processor = StringUtils()
    assert processor.end_with(input_text, simbol) == expected_output

@pytest.mark.parametrize (
    "input_text, expected_output",
    [("hello", False), ("", True)],
)
def test_is_empty (input_text, expected_output):
    processor = StringUtils()
    assert processor.is_empty(input_text) == expected_output

@pytest.mark.parametrize (
    "input_text, joiner, expected_output",
    [(["Sky", "Pro"], "-", "Sky-Pro"), (["Sky", "Pro"], ", ", "Sky, Pro"), ([1,2,3,4], ", ", "1, 2, 3, 4") ], 
)
def test_list_to_string (input_text, joiner, expected_output):
    processor = StringUtils()
    assert processor.list_to_string(input_text, joiner) == expected_output