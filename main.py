from random import randint, random

from config import Settings, get_random_char
from game import Game
from text_object import TextObject


class TextColumn:
    def __init__(
            self,
            start_pos_x: int,
            start_pos_y: int,
            char_count: int,
            font_name: str,
            font_size: int,
            like_column=False
    ):
        self.charset = []
        if like_column:
            velocity_y = random() * 2
            self.charset.extend(
                TextObject(
                    pos_x=start_pos_x,
                    pos_y=start_pos_y - i * font_size,
                    text_func=get_random_char,
                    color=(10, 255 + randint(-100, 0), 20),
                    font_name=font_name,
                    font_size=font_size,
                    velocity_y=velocity_y
                ) for i in range(1, char_count)
            )
        else:
            self.charset.extend([
                TextObject(
                    pos_x=start_pos_x,
                    pos_y=start_pos_y - i * font_size,
                    text_func=get_random_char,
                    color=(10, 255 + randint(-100, 0), 20),
                    font_name=font_name,
                    font_size=font_size,
                    velocity_y=random() * 2
                ) for i in range(1, char_count)
            ])


    def update(self):
        for char in self.charset:
            char.update()

    def draw(self, surface):
        for char in self.charset:
            char.draw(surface)


class Matrix(Game):
    def __init__(self):
        super(Matrix, self).__init__()
        [self.objects.append(TextColumn(
            start_pos_x=x,
            start_pos_y=Settings.HEIGHT // 2,
            char_count=randint(7, 10),
            font_name='Consolas',
            font_size=40
        )) for x in range(0, Settings.WIDTH, 30)]


if __name__ == '__main__':
    Matrix().run()
