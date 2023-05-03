__author__ = "Michael Weichenrieder"

import matplotlib.pyplot as plt

from entropy_analyzer.entropy_block import EntropyBlock


class EntropyVisualizer:
    """
    Visualizer to display entropy analysis results using matplotlib
    """

    @classmethod
    def visualize_single_block(cls, entropy_block: EntropyBlock) -> None:
        """
        Visualizes the results of a single EntropyBlock
        Args:
            entropy_block: The results block to take results from
        """
        # Init plot
        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title("Entropy analysis results")

        # Add data
        ax.bar(entropy_block.get_key_ints(), entropy_block.get_value_counts())

        # Formatting
        ax.set_title(
            f"Entropy of '{entropy_block.reference_name}': {round(entropy_block.calculate_standardized_entropy(), 10)}")
        ax.set_xlabel("Byte (as int)")
        ax.set_ylabel("Count")

        # Show
        plt.show()

    @classmethod
    def visualize_multiple_blocks(cls, entropy_blocks: list[EntropyBlock]) -> None:
        """
        Visualizes the results of a blocked file analysis
        Args:
            entropy_blocks: The results blocks to take results from
        """
        # Init plot
        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title("Entropy analysis results")

        # Add data
        ax.bar(list(range(len(entropy_blocks))), [block.calculate_standardized_entropy() for block in entropy_blocks])

        # Formatting
        ax.set_title(
            f"Entropy of '{entropy_blocks[0].reference_name}'")
        ax.set_xlabel("Block")
        ax.set_ylabel("Entropy")
        ax.set_ylim(0, 1)

        # Show
        plt.show()
