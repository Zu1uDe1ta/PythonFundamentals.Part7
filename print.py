
languages = {
    1: "English",
    2: "Spanish",
    3: "Portuguese"
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.
    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    for language in lang_options:
        print(language)