__author__ = "Michael Weichenrieder"


class EntropyBlock:
    """
    Model for managing entropy data for bytes
    """

    def __init__(self, reference_name: str):
        """
        Constructor
        Args:
            reference_name: Name of the thing that is analyzed
        """
        self.reference_name: str = reference_name
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
