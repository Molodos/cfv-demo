from os import path

from entropy_analyzer.entropy_data import EntropyData


class EntropyCalculator:
    demo_data_dir: str = path.join(path.dirname(path.realpath(__file__)), "..", "demo_data")

    @classmethod
    def calculate_entropy(cls, file_name: str) -> EntropyData:
        entropy_data: EntropyData = EntropyData(file_name=file_name)
        with open(path.join(cls.demo_data_dir, file_name), "rb") as f:
            while True:
                b: bytes = f.read(1)
                if b == b"":
                    break
                entropy_data.count_byte(byte=b)
        return entropy_data
