import re
from zipfile import ZipFile


class TextAnalyzer:
    __source_text = ""

    def __init__(self):
        pass

    @property
    def source_text(self):
        return self.__source_text

    @source_text.setter
    def source_text(self, source_text):
        self.__source_text = source_text

    def read_file(self, file_name):
        try:
            file = open(file_name)
        except OSError:
            raise NameError("There is no file with such name")
        except FileNotFoundError:
            raise NameError("There is no file with such name")
        self.__source_text = file.read()
        file.close()

    def count_sentences(self) -> int:
        return len(re.findall(r"[?|\.|!]", self.__source_text))

    def count_asserting_sentences(self) -> int:
        return len(re.findall(r"\.", self.__source_text))

    def count_questioning_sentences(self) -> int:
        return len(re.findall(r"\?", self.__source_text))

    def count_of_prompting_sentences(self) -> int:
        return len(re.findall(r"!", self.__source_text))

    def average_word_len(self) -> float:
        sentences = re.findall(r".*[?!.]", self.__source_text)
        cur_len = 0
        words_count = 0
        for sentence in sentences:
            words = re.findall(r"\b\S\w\b", sentence)
            words_count += len(words)
            for word in words:
                cur_len += len(word)
        return cur_len / words_count

    def average_sentence_len(self) -> float:
        sentences = re.findall(r".*[?!.]", self.__source_text)
        cur_len = 0
        for sentence in sentences:
            cur_len += len(sentence)
        return cur_len / len(sentences)

    def get_emojis_count(self) -> int:
        return len(re.findall(r"\s+[;:](-)*((((\[+)|(\]+)|(\(+)|(\)+))\s+)\b)", self.__source_text))

    def get_words_less_than_5_chars(self) -> list[str]:
        return re.findall(r"\b\w{1,5}\b", self.__source_text)

    def enclose_latin_pairs(self):
        return re.sub(r"([a-z][A-Z])", r"_?_\1_?_", self.__source_text)


def solve_task_2():
    parser = TextAnalyzer()
    while True:
        user_input = input(
            "Enter the required file name: (empty string for preselected name) ")
        try:
            if user_input != "":
                parser.read_file(user_input)
            else:
                parser.read_file(
                    "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR4/txt_sources/rnd_name.txt")
            break
        except NameError as err:
            print(err)
    print("(Text with enclosed pairs of kind 'aB')\n " +
          parser.enclose_latin_pairs())
    sentences_count_info = "Count of sentences in text: " + \
        str(parser.count_sentences())
    print(sentences_count_info)
    asserting_sentences_info = "Count of asserting sentences: " + \
        str(parser.count_asserting_sentences())
    print(asserting_sentences_info)
    questioning_sentences_info = "Count of questioning sentences: " + \
        str(parser.count_questioning_sentences())
    print(questioning_sentences_info)
    prompting_sentences_info = "Count of prompting sentences: " + \
        str(parser.count_of_prompting_sentences())
    print(prompting_sentences_info)
    average_word_length_info = "Average length of word in sentences: " + \
        str(parser.average_word_len())
    print(average_word_length_info)
    emojis_count_info = "Count of emojis in text: " + \
        str(parser.get_emojis_count())
    print(emojis_count_info)

    output_file_path = "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR4/txt_sources/out/task_2.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(sentences_count_info + "\n" +
                          asserting_sentences_info + "\n" + questioning_sentences_info + "\n" + prompting_sentences_info + "\n" + average_word_length_info + "\n" + emojis_count_info)
    with ZipFile("/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR4/txt_sources/out/task_2.zip", "w") as zip:
        zip.write(
            "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR4/txt_sources/out/task_2.txt", "zipped_task2.txt")
        print(zip.infolist())
    return


def main():
    solve_task_2()


if __name__ == "__main__":
    main()
