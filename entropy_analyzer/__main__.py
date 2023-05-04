__author__ = "Michael Weichenrieder"

from os import path

from entropy_analyzer.entropy_block import EntropyBlock
from entropy_analyzer.entropy_visualizer import EntropyVisualizer
from entropy_analyzer.file_entropy_calculator import FileEntropyCalculator

demo_data_dir: str = path.join(path.dirname(path.realpath(__file__)), "..", "demo_data")


def show_overall_entropy(file_name: str):
    entropy_block: EntropyBlock = FileEntropyCalculator.calculate_overall_entropy(
        file_path=path.join(demo_data_dir, file_name))
    EntropyVisualizer.visualize_single_block(entropy_block)


def show_entropy_blocks(file_name: str):
    entropy_blocks: list[EntropyBlock] = FileEntropyCalculator.calculate_blocked_entropy(
        file_path=path.join(demo_data_dir, file_name), block_size=4096)
    EntropyVisualizer.visualize_multiple_blocks(entropy_blocks)


if __name__ == "__main__":
    """
    Entry point of the script
    """
    base_files: list[str] = ["binary.exe", "random.bin", "utf8.txt"]
    zip_names: list[str] = ["compressed.zip", "compressed_encrypted.zip", "compressed_encrypted_old.zip"]
    for f in base_files + zip_names:
        show_overall_entropy(f)
        # show_entropy_blocks(f)
