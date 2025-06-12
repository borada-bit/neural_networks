import numpy as np

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        
if __name__ == "__main__":
    # Example usage
    sizes = [784, 30, 10]  # Example sizes for input layer, hidden layer, and output layer
    net = Network(sizes)
    
    print("Number of layers:", net.num_layers)
    print("Sizes of each layer:", net.sizes)
    print("Biases for each layer:", net.biases)
    print("Weights for each layer:", net.weights)     
