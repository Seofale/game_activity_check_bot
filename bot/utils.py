from typing import Union


def get_index_safe(index: int, list_: list, default=None) -> Union[int, None]:
    try:
        return list_[index]
    except IndexError:
        return default
