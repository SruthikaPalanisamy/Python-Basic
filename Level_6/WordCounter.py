from collections import Counter

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    lines = text.split("\n")
    words = text.split()

    print("Total Lines:", len(lines))
    print("Total Words:", len(words))
    print("Total Characters:", len(text))

    counter = Counter(words)

    print("\nTop 3 Most Common Words:")
    for word, count in counter.most_common(3):
        print(word, ":", count)

except FileNotFoundError:
    print("File Not Found!")