import json


class AnagramGenerator:
    def __init__(self, lengths=[0]) -> None:
        self.lengths = lengths

    def init_words(self):
        pass

    def get_text_input(self):
        text_input = input("\nWhat would you like to 'gram?\n\n")
        stripped_text_input = text_input.strip().replace(" ", "").casefold()
        if not all(char.isalpha() for char in stripped_text_input):
            print("\nInput contains invalid characters, try again.\n")
            self.get_input()
        else:
            self.stripped_text_input = stripped_text_input
            self.total_chars = len(self.stripped_text_input)
            print(f"\nInput valid: {self.stripped_text_input}\n")

    def get_output_lengths(self):
        lengths_input = input(
            "\nWould you like to specify word lenghts for the output?\nMake sure to mention all lengths, and that they sum to the total number of letters in the text input.\nSeparate different lenghts by comma.\n\n"
        )
        stripped_lengths_input = lengths_input.strip().replace(" ", "").casefold()
        if not all(char.isnumeric() or char == "," for char in stripped_lengths_input):
            print("\nInput contains invalid characters, try again.\n")
            self.get_output_lengths()

        else:
            self.stripped_lengths_input = [
                int(item) for item in stripped_lengths_input.split(",") if item
            ]
            self.stripped_lengths_input.sort()
            self.total_length = sum(self.stripped_lengths_input)

        if not self.total_chars == self.total_length:
            print(
                f"\nLengths don't match the total characters ({self.total_chars}), try again.\n"
            )
            self.get_output_lengths()

        else:
            print(f"\nInput valid, lengths: {self.stripped_lengths_input}\n")

    def run(self):
        self.get_text_input()
        self.get_output_lengths()


anagram_generator = AnagramGenerator()
anagram_generator.run()
