from src.item import Item


class LanguageMixin:
    lang_count = 0
    __language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        self.lang_count += 1
        if self.lang_count % 2 == 0:
            self.__language = "EN"
        else:
            self.__language = "RU"
        return self


class KeyBoard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

