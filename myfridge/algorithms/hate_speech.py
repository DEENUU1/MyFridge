import json
from typing import List, Dict, Any, Tuple


def get_data(filename: str) -> Any:
    """
    Returns data from file
    """
    with open("hatewords_english.json", "r") as file:
        return json.load(file)


def text_to_list(text: str):
    """
    Returns long text as a list of words
    """
    return text.lower().split()


def hate_speech_result(data: Any, text: List[str], model) -> None:
    counter = 0
    new_text = []
    for word in text:
        if word in data["censoredWords"]:
            counter += 1
            censored_word = "*" * len(word)
            new_text.append(censored_word)
        new_text.append(word)

    if 0 < counter < 2:
        censored_text = "".join(new_text)
        models.objects.update_or_create(
            text=censored_text,
        )
    model.objects.delete()
