import random
import matplotlib.pyplot as plt

def visualizeLionBehavior(lions_seen_1, lions_seen_2, name, index):
    # Count the occurrences of 't' (tagged) and 'n' (non-tagged) lions for each enclosure section
    lion_counts_1 = {'t': 0, 'n': 0}
    lion_counts_2 = {'t': 0, 'n': 0}
    for lion in lions_seen_1:
        lion_counts_1[lion] += 1
    for lion in lions_seen_2:
        lion_counts_2[lion] += 1

    plt.subplot(3, 2, index)
    # Create a bar plot to visualize the lion behaviour for both enclosures
    labels = ['Enclosure 1', 'Enclosure 2']
    tagged_counts = [lion_counts_1['t'], lion_counts_2['t']]
    non_tagged_counts = [lion_counts_1['n'], lion_counts_2['n']]

    plt.bar(labels, tagged_counts, label='Tagged')
    plt.bar(labels, non_tagged_counts,
            bottom=tagged_counts, label='Non-Tagged')

    plt.xlabel('Enclosure')
    plt.ylabel('Count')
    plt.title(name)
    plt.legend()


def getLionsSeen(enableVisual):
    # TODO: Allow this to be configurable
    # Create a list with 10 't' (tagged) and 8 'n' (non-tagged) lions
    lions = ['t'] * 10 + ['n'] * 8
    lionsSeen = []
    if enableVisual:
        visualizeLionBehavior(lions, lionsSeen, 'Initial Situation', 1)
    for i in range(4):
        # Randomly select an element from the 'lions' list
        index = random.randint(0, len(lions) - 1)
        # Note that in this case the lion CANNOT be reselected
        # If reselection was allowed then the following line would be lion = lions[index] instead
        lion = lions.pop(index)
        # Add the selected lion to the 'lionsSeen' list
        lionsSeen += lion
        if enableVisual:
            visualizeLionBehavior(
                lions, lionsSeen, f'After {i + 1} lion(s) move(s) to end of enclosure', i + 2)
    return lionsSeen


def getNoTagBatches(attempts, enableVisual):
    noTagCount = 0
    for i in range(attempts):
        # Simulate observing lion groups and count batches with no tagged lions
        lionsSeen = getLionsSeen(enableVisual)
        if ('t' not in lionsSeen):
            # Increment the count if no tagged lions are observed in a batch
            noTagCount += 1
    # Return the count of batches with no tagged lions
    return noTagCount


def runSimulation(simulatationAttempts, batchAttempts, enableVisual):
    probabilitiesList = []
    for i in range(simulatationAttempts):
        # Simulate multiple attempts of observing lion groups and calculate probabilities
        noTagBatches = getNoTagBatches(batchAttempts, enableVisual)
        probability = noTagBatches / batchAttempts
        probabilitiesList += [probability]
    return probabilitiesList


def main():
    userInput = input(
        'V for visualise or S for simulation (to get probability): ')
    if userInput.lower() == 'v':
        plt.figure(figsize=(12, 10))
        runSimulation(1, 1, True)
        plt.tight_layout()
        plt.show()
    elif userInput.lower() == 's':
        probabilitiesList = runSimulation(1000, 1000, False)
        print(
            f"The probability of observing batches without tagged lions is: {(1 - sum(probabilitiesList) / len(probabilitiesList)) * 100}%")
    else:
        print('Invalid option. Laterz')


main()


# Assuming that the selection group does not change - (1 - 8/18 * 8/18 * 8/18 * 8/18) * 100
# Assuming that the selection group does change (The lion is no longer available for selection if it has already been selected) - (1 - (8/18 * 7/17 * 6/16 * 5/15)) * 100
