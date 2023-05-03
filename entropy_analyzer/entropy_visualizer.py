__author__ = "Michael Weichenrieder"

import matplotlib.pyplot as plt

from entropy_analyzer.entropy_processor import EntropyProcessor


class EntropyVisualizer:
    """
    Visualizer to display entropy analysis results using matplotlib
    """

    @classmethod
    def visualize(cls, entropy_processor: EntropyProcessor) -> None:
        """
        Visualizes the results of an EntropyProcessor
        Args:
            entropy_processor: The processor to take results from
        """
        # Init plot
        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title("Entropy analysis results")

        # Add data
        ax.bar(entropy_processor.get_key_ints(), entropy_processor.get_value_counts(), edgecolor="white", linewidth=0.1)

        # Formatting
        ax.set_title(f"Entropy of '{entropy_processor.reference_name}'")
        ax.set_xlabel("Byte (as int)")
        ax.set_ylabel("Count")

        # Show
        plt.show()
