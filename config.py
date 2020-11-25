from random import choice


class Settings:
    WIDTH = 1600
    HEIGHT = 900
    FPS = 60


class Colours:
    # R  G  B
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


TEXT_SCOPE = ['И', 'а', 'б', 'е', 'л', 'р', 'т', 'ю', 'я']


def get_random_char():
    char = choice(TEXT_SCOPE)
    while True:
        yield char
        ch = choice([True, False])
        char = char if not ch else choice(TEXT_SCOPE)