import matplotlib.pyplot as plt
import collections

def plotDiseasesFrequencyBarChart(dataset, label_names):
    labels_frequency = dict(collections.Counter(dataset))
    labels_frequency = dict(zip(label_names, list(labels_frequency.values())))
    print(labels_frequency)

    ax = plt.figure(figsize=(10, 10))
    ax.bar(*zip(*labels_frequency.items()))
    ax.set_xlabel('Types of Disease', fontdict={'fontsize': 14})
    ax.set_ylabel('Frequency', fontdict={'fontsize': 14})
    ax.set_title("Frequency of images per type of cassavas' disease", fontdict={'fontsize': 17})
    plt.show()
