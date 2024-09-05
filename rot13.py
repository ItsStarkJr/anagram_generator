import string


class Rot13:
    def __init__(self, text) -> None:
        self.text = text

    def rot13(self):
        # Define the translation table for ROT13
        rot13_translation = str.maketrans(
            string.ascii_lowercase + string.ascii_uppercase,
            string.ascii_lowercase[13:]
            + string.ascii_lowercase[:13]
            + string.ascii_uppercase[13:]
            + string.ascii_uppercase[:13],
        )

        # Translate the input text using the ROT13 translation table

        self.translation = self.text.translate(rot13_translation)
        print(self.translation)

    def run(self):
        self.rot13()
