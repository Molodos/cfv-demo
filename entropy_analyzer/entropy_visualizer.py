import matplotlib.pyplot as plt

from entropy_analyzer.entropy_data import EntropyData


class EntropyVisualizer:

    @classmethod
    def visualize(cls, entropy_data: EntropyData) -> None:
        # Add data
        fig, ax = plt.subplots()
        ax.bar(entropy_data.get_key_ints(), entropy_data.get_value_counts(), edgecolor="white", linewidth=0.1)

        # Formatting
        ax.set_xlim(0, 255)
        ax.set_title(f"Entropy of '{entropy_data.file_name}'")
        ax.set_xlabel("Byte (as int)")
        ax.set_ylabel("Count")

        # Show
        plt.show()
