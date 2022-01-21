import textwrap
from datetime import date, datetime

class Formatter():

    def __init__(self):
        pass

    def _add_line_break(self, lines):
        return ''.join([s + "\n" for s in lines])

    def split(self, text, size):
        words = iter(text.split())
        lines, current = [], next(words)
        for word in words:
            if len(current) + 1 + len(word) > size:
                lines.append(current)
                current = word
            else:
                current += " " + word
        lines.append(current)
        return self._add_line_break(lines)
    
    def fast_split(self, text, size):
        lines = textwrap.wrap(text, size, break_long_words=False)
        return self._add_line_break(lines)

    def save_file(self, text):
        file = open(f"output/{datetime.now()}.txt", "w")
        file.write(text)
        file.close()

    def justify(self, text, size):
        lines = textwrap.wrap(text, size, break_long_words=False)
        final_text = ""
        for line_index, line in enumerate(lines):
            new_line = []
            new_line.append(line)

            if len(line) < size:
                count_of_chars = len(line)
                count = 0
                blank_spaces = [c for c in line if c == " "]
                number_of_blank_spaces = len(blank_spaces)

                if number_of_blank_spaces == 0:
                    while len(new_line[0]) < size:
                        temp_line = new_line[0]
                        new_line[0] = temp_line + " "

                last_blank_space = 0
                blank_space_count = 0
                    
                while len(new_line[0]) < size:
                    for index, c in enumerate(new_line[0]):
                        if new_line[0][index] == " " and new_line[0][index + 1] != " ":
                            blank_space_count += 1
                            if blank_space_count > last_blank_space:

                                new_line[0] = new_line[0][:index] + " " + new_line[0][index:]
                                    
                                last_blank_space = blank_space_count
                                blank_space_count = 0

                                if last_blank_space == number_of_blank_spaces:
                                    last_blank_space = 0
                                break
            else:
                new_line[0] = line
                
            final_text += new_line[0] + "\n"

        return final_text
