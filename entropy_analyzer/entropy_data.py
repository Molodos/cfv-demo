class EntropyData:
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.byte_counter: dict[bytes, int] = {}

    def count_byte(self, byte: bytes) -> None:
        self.byte_counter[byte] = self.byte_counter.get(byte, 0) + 1

    def get_key_ints(self) -> list[int]:
        return [key[0] for key in self.byte_counter.keys()]

    def get_value_counts(self) -> list[int]:
        return list(self.byte_counter.values())
