import random


class TextConverterService:
    _text: str
    _converted_text: str | None = None

    def __init__(self, text: str):
        self._text = text

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text
        self._converted_text = None

    @property
    def converted_text(self):
        if not self._converted_text:
            self.__convert()
        return self._converted_text

    def __convert(self) -> str:
        if self._converted_text:
            return self._converted_text
        words = self._text.split()
        result = []
        for word in words:
            if len(word) > 3:
                inner_text = list(word[1:-1])
                random.shuffle(inner_text)
                result.append(f'{word[0]}{"".join(inner_text)}{word[-1]}')
            else:
                result.append(word)
        self._converted_text = ' '.join(result)
