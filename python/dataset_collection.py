from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

"""
The standard MNIST dataset
handwritten digits 0-9, grayscale

Instance Format: torch tensor, (28x28,1), float in [0,1]
Training instances: 60k
Test instances: 10k
"""
MNIST_train = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)
MNIST_test = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
dataloader_MNIST_train = DataLoader(MNIST_train, batch_size=64)
dataloader_MNIST_test = DataLoader(MNIST_test, batch_size=64)

"""
The FashionMNIST dataset
sketches of cloths, 10 classes 0-9, grayscale

Instance Format: torch tensor, (28x28,1), float in [0,1]
Training instances: 60k
Test instances: 10k
"""

FMNIST_train = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)
FMNIST_test = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
dataloader_FMNIST_train = DataLoader(FMNIST_train, batch_size=64)
dataloader_FMNIST_test = DataLoader(FMNIST_test, batch_size=64)