

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def stupid_count_tokens(tokens, text):
    res = 0
    for token in tokens:
        if token in text:
            res += 1
    return res
