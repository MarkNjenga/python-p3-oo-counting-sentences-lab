class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = 0
        for i in range(len(self.value)):
            if self.value[i] in ".!?" and (i == len(self.value) - 1 or self.value[i + 1] != self.value[i]):
                sentences += 1
        return sentences