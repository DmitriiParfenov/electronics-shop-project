from src.item import Item


class MixinLanguage:
    """Класс-миксин для изменения языка раскладки клавиатуры"""

    __language = 'EN'

    @property
    def language(self) -> str:
        return self.__language

    @classmethod
    def change_lang(cls):
        """Класс-метод изменяет язык раскладки клавиатуры с EN на RU и наоборот. Возвращает объект класса."""
        if cls.__language == 'EN':
            cls.__language = 'RU'
        else:
            cls.__language = 'EN'
        return cls


class Keyboard(Item, MixinLanguage):
    """Класс Keyboard, унаследованный от Item, MixinLanguage"""

    def __str__(self):
        """Возвращает строку с названием класса и полями при инизиализации экземпляров класса, а также текущий язык
             раскладки клавиатуры в дружественном формате"""
        return super().__str__() + f'Language = {self.language}'
