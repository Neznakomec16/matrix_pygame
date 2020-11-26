from random import randint, random

from config import Settings
from game import Game
from text_object import TextObject, get_random_char


class TextColumn:
    def __init__(
            self,
            start_pos_x: int,
            start_pos_y: int,
            char_count: int,
            font_name: str,
            font_size: int,
            bold=False,
            like_column=False
    ):
        velocity_y = 0.5 + random() * 2
        self.charset = [
            TextObject(
                pos_x=start_pos_x,
                pos_y=start_pos_y - (i * font_size),
                text_func=get_random_char,
                color=(224 if i == 1 else 10, 255 + randint(-100, 0), 20),
                font_name=font_name,
                font_size=font_size,
                velocity_y=velocity_y if like_column else random() * 2,
                bold=bold,
            ) for i in range(1, char_count)
        ]

    def update(self):
        for char in self.charset:
            char.update()

    def draw(self, surface):
        for char in self.charset:
            char.draw(surface)


class Matrix(Game):
    def __init__(self, like_column=False):
        super(Matrix, self).__init__()
        [self.objects.append(TextColumn(
            start_pos_x=x,
            start_pos_y=0,
            char_count=randint(15, 25),
            font_name='font/MS Mincho.ttf',
            font_size=40,
            bold=True,
            like_column=like_column
        )) for x in range(0, Settings.WIDTH, 30)]


if __name__ == '__main__':
    Matrix(like_column=True).run()
