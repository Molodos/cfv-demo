__author__ = "Michael Weichenrieder"

import matplotlib.pyplot as plt

from entropy_analyzer.entropy_processor import EntropyBlock


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
        ax.bar(entropy_block.get_key_ints(), entropy_block.get_value_counts(), edgecolor="white", linewidth=0.1)

        # Formatting
        ax.set_title(f"Entropy of '{entropy_block.reference_name}'")
        ax.set_xlabel("Byte (as int)")
        ax.set_ylabel("Count")

        # Show
        plt.show()
