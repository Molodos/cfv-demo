__author__ = "Michael Weichenrieder"

from os import path

from entropy_analyzer.entropy_block import EntropyBlock
from entropy_analyzer.entropy_visualizer import EntropyVisualizer
from entropy_analyzer.file_entropy_calculator import FileEntropyCalculator

demo_data_dir: str = path.join(path.dirname(path.realpath(__file__)), "..", "demo_data")

if __name__ == "__main__":
    """
    Entry point of the script
    """
    file_names: list[str] = ["random.bin", "lorem_ipsum.txt", "compressed.zip", "compressed_encrypted.zip"]
    for file_name in file_names:
        entropy_block: EntropyBlock = FileEntropyCalculator.calculate_overall_entropy(
            file_path=path.join(demo_data_dir, file_name))
        EntropyVisualizer.visualize_single_block(entropy_block)
