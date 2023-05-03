__author__ = "Michael Weichenrieder"

import math


class EntropyBlock:
    """
    Model for managing entropy data for bytes
    """

    def __init__(self, reference_name: str, block_number: int = 0):
        """
        Constructor
        Args:
            reference_name: Name of the thing that is analyzed
            block_number: Number of the block
        """
        self.reference_name: str = reference_name
        self.block_number: int = block_number
        self.size: int = 0

        # Initialize byte counter
        self.byte_counter: dict[bytes, int] = {}
        for i in range(256):
            self.byte_counter[i.to_bytes(length=1, byteorder="big", signed=False)] = 0

    def process_byte(self, byte: bytes) -> None:
        """
        Process an input byte for entropy calculations
        Args:
            byte: The byte to be processed
        """
        self.byte_counter[byte] = self.byte_counter.get(byte, 0) + 1
        self.size += 1

    def get_key_ints(self) -> list[int]:
        """
        Get a list of all bytes formatted as integers
        Returns: All possible bytes formatted as integers
        """
        return [int.from_bytes(bytes=key, byteorder="big", signed=False) for key in self.byte_counter.keys()]

    def get_value_counts(self) -> list[int]:
        """
        Get a list of all byte counts in the same order as the keys from get_key_ints()
        Returns: All byte counts
        """
        return list(self.byte_counter.values())

    def calculate_standardized_entropy(self) -> float:
        """
        Calculate the standardized (0-1) entropy
        Returns: The standardized entropy
        """
        relative_frequencies: [float] = [count / self.size for count in self.byte_counter.values()]
        entropy: float = -sum([freq * math.log2(freq) for freq in relative_frequencies if freq != 0])
        standardized_entropy: float = entropy / math.log2(len(relative_frequencies))
        return standardized_entropy
