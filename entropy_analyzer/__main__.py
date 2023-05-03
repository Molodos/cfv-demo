from entropy_analyzer.entropy_calculator import EntropyCalculator
from entropy_analyzer.entropy_data import EntropyData
from entropy_analyzer.entropy_visualizer import EntropyVisualizer

if __name__ == "__main__":
    entropy_data: EntropyData = EntropyCalculator.calculate_entropy(file_name="lorem_ipsum.txt")
    EntropyVisualizer.visualize(entropy_data)
