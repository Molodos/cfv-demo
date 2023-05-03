__author__ = "Michael Weichenrieder"

from os import path

from entropy_analyzer.entropy_block import EntropyBlock


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
        return cls.calculate_blocked_entropy(file_path=file_path, block_size=-1)[0]

    @classmethod
    def calculate_blocked_entropy(cls, file_path: str, block_size: int) -> list[EntropyBlock]:
        """
        Calculates the entropy of a file divided in blocks
        Args:
            file_path: The path of the file to analyze
            block_size: The size of a block in bytes
        Returns: A list of EntropyBlock objects containing the results
        """
        file_name: str = file_path.split(path.sep)[-1]
        entropy_blocks: list[EntropyBlock] = [EntropyBlock(reference_name=file_name)]
        with open(file_path, "rb") as f:
            while True:
                b: bytes = f.read(1)
                if not b:
                    break
                if block_size != -1 and entropy_blocks[-1].size >= block_size:
                    entropy_blocks.append(EntropyBlock(reference_name=file_name))
                entropy_blocks[-1].process_byte(byte=b)
        return entropy_blocks
