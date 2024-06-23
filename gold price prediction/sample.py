import tensorflow_datasets as tfds

# Load MNIST dataset
mnist_dataset = tfds.load(name='mnist', split=tfds.Split.TRAIN)
print(mnist_dataset.shape)