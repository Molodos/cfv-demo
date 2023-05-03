__author__ = "Michael Weichenrieder"

from os import path

from entropy_analyzer.entropy_processor import EntropyBlock


class FileEntropyCalculator:
    """
    Calculator for file entropy
    """

    @classmethod
    def calculate_overall_entropy(cls, file_path: str) -> EntropyBlock:
        """
        Calculates the overall entropy of a file
        Args:
            file_path: The path of the file to analyze
        Returns: The EntropyBlock object containing the results
        """
        entropy_data: EntropyBlock = EntropyBlock(reference_name=file_path.split(path.sep)[-1])
        with open(file_path, "rb") as f:
            while True:
                b: bytes = f.read(1)
                if not b:
                    break
                entropy_data.process_byte(byte=b)
        return entropy_data
