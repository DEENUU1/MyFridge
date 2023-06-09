import json
from typing import List, Dict, Any, Tuple


def get_data() -> Any:
    """
    Returns data from file
    """
    try:
        with open("/app/algorithms/badwords.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return None


def text_to_list(text: str):
    """
    Returns long text as a list of words
    """
    if text is not None:
        return text.lower().split()


def hate_speech_result(context: str, model: str) -> Tuple[int, str]:
    """
    Count the number of bad words and censored them.
    """
    data = get_data()
    text = text_to_list(context)
    counter = 0
    new_text = []

    if text is not None and data is not None:
        for word in text:
            if word in data["censoredWords"]:
                counter += 1
                censored_word = "*" * len(word)
                new_text.append(censored_word)
            else:
                new_text.append(word)

        new_text = " ".join(new_text)
        return counter, new_text

    return 0, ""
