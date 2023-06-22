# This is an example of the Factory pattern based on Text Converter

from abc import ABC, abstractmethod


class Text:
    def __init__(self, result: str):
        self.result = result

    # additional methods can be implemented in this class,
    # ex. def get_result_size(self):


class TextConverter(ABC):
    # @abstractmethod - declared VideoToTextConverter uses this parent method implementation
    def extract_text(self):
        print('Abstract Converter')


class ImageToTextConverter(TextConverter):
    def __init__(self, input_file: str):
        self.__input_file = input_file

    def extract_text(self) -> Text:
        print(f'ImageToText converter start extracting from {self.__input_file}')
        return Text(result='result of ImageToTextConverter')


class SoundToTextConverter(TextConverter):
    def __init__(self, input_file: str):
        self.__input_file = input_file

    def extract_text(self) -> Text:
        print(f'SoundToText converter start extracting from {self.__input_file}')
        return Text(result='result of SoundToTextConverter')


class VideoToTextConverter(TextConverter):
    pass


class ConverterFactory:
    converter = {
        'png': ImageToTextConverter,
        'jpg': ImageToTextConverter,
        'mp3': SoundToTextConverter,
        'wav': SoundToTextConverter,
    }

    def start_converter(self, user_input: str):
        file_type = user_input.split('.')[-1]
        return self.converter[file_type](user_input)


if __name__ == '__main__':
    factory = ConverterFactory()

    converter = factory.start_converter('img-sample-1.png')
    txt = converter.extract_text()
    print(txt.result)

    converter_2 = factory.start_converter('sample-3s.mp3')
    txt = converter_2.extract_text()
    print(txt.result)

    video_converter = VideoToTextConverter().extract_text()
