from torchvision import datasets

from polyaxon_client.tracking import get_data_paths

def main():
    datasets.MNIST(get_data_paths()['mnist'], train=True, download=True)
    datasets.MNIST(get_data_paths()['mnist'], train=False, download=True)

if __name__ == '__main__':
    main()