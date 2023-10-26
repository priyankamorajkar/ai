import numpy as np
class NeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def _sigmoid_derivative(self, x):
        return x * (1 - x)
    def train(self, inputs, outputs, training_iterations):
        for _ in range(training_iterations):
            output = self.learn(inputs)
            error = outputs - output
            factor = inputs.T.dot(error * self._sigmoid_derivative(output))
            self.synaptic_weights += factor
    def learn(self, inputs):
        return self._sigmoid(inputs.dot(self.synaptic_weights))
if __name__ == '__main__':
    neural_network = NeuralNet()
    inputs = np.array([[0, 1, 1], [1, 1, 0], [1, 0, 1]])
    outputs = np.array([[1, 0, 1]]).T
    neural_network.train(inputs, outputs, 10000)
    print("Accuracy is:")
    print(neural_network.learn(np.array([1, 0, 1])))
