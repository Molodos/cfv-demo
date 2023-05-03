__author__ = "Michael Weichenrieder"

from os import path

from entropy_analyzer.entropy_processor import EntropyProcessor


class FileEntropyCalculator:
    """
    Calculator for file entropy
    """

    @classmethod
    def calculate_entropy(cls, file_path: str) -> EntropyProcessor:
        """
        Calculates the entropy of a file
        Args:
            file_path: The path of the file to analyze
        Returns: The EntropyProcessor object containing the results
        """
        entropy_data: EntropyProcessor = EntropyProcessor(reference_name=file_path.split(path.sep)[-1])
        with open(file_path, "rb") as f:
            while True:
                b: bytes = f.read(1)
                if b == b"":
                    break
                entropy_data.process_byte(byte=b)
        return entropy_data
