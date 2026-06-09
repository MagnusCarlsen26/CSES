def lengthOfLongestRepeatingSequence(dnaSequence: str) -> int:

    lengthOfDNASequence = len(dnaSequence)

    if lengthOfDNASequence <= 1:
        return lengthOfDNASequence

    longestRepeatingSequenceFound = 1
    currentRepeatingSequenceLength = 1

    for i in range(1, lengthOfDNASequence):
        if dnaSequence[i] == dnaSequence[i - 1]:
            currentRepeatingSequenceLength += 1
            if currentRepeatingSequenceLength > longestRepeatingSequenceFound:
                longestRepeatingSequenceFound = currentRepeatingSequenceLength
        else:
            currentRepeatingSequenceLength = 1

    return longestRepeatingSequenceFound


def main():
    dnaSequence = input()
    print(lengthOfLongestRepeatingSequence(dnaSequence))


main()

