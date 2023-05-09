__author__ = "Michael Weichenrieder"

import json
import math
import time
from os import path
from threading import Thread
from typing import Any

from cfv_demo.entropy_analyzer.entropy_block import EntropyBlock
from cfv_demo.entropy_analyzer.file_entropy_calculator import FileEntropyCalculator


class FileProcessor(Thread):
    """
    Processes files in the background
    """

    FILE_PATH: str = path.join(path.dirname(path.realpath(__file__)), "uploads")
    RESULT_PATH: str = path.join(path.dirname(path.realpath(__file__)), "results")

    @classmethod
    def process(cls, file_id: str, file_name: str) -> None:
        """
        Start processing a file
        Args:
            file_id: The uuid of the file
            file_name: Original file name
        """
        file_processor: FileProcessor = FileProcessor(file_id=file_id, file_name=file_name)
        file_processor.start()

    def __init__(self, file_id: str, file_name: str):
        """
        Create a new processor
        Args:
            file_id: The uuid of the file to process
            file_name: Original file name
        """
        super().__init__()
        self.file_id: str = file_id
        self.file_name: str = file_name
        self.setDaemon(True)

    def run(self) -> None:
        """
        Thread contents: Do processing work
        """
        start: float = time.time()
        file: str = path.join(self.FILE_PATH, f"{self.file_id}.bin")
        overall_entropy: EntropyBlock = FileEntropyCalculator.calculate_overall_entropy(file_path=file)
        block_size: int = max(4096, math.ceil(overall_entropy.size / 256))
        blocked_entropy: list[EntropyBlock] = FileEntropyCalculator.calculate_blocked_entropy(file_path=file,
                                                                                              block_size=block_size)
        results: dict[str, Any] = {
            "file_name": self.file_name,
            "processing_seconds": time.time() - start,
            "overall_entropy": {
                "size": overall_entropy.size,
                "entropy": round(overall_entropy.calculate_standardized_entropy(), 8),
                "bytes": overall_entropy.get_key_ints(),
                "byte_counts": overall_entropy.get_value_counts()
            },
            "blocked_entropy": {
                "block_size": block_size,
                "block_ids": list(range(0, len(blocked_entropy))),
                "block_entropies": [round(block.calculate_standardized_entropy(), 8) for block in blocked_entropy]
            }
        }
        with open(path.join(self.RESULT_PATH, f"{self.file_id}.json"), "w") as outfile:
            outfile.write(json.dumps(results, indent=4))
