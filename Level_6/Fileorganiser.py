import os

# Create two files
with open("file1.txt", "w") as f:
    f.write("Python is easy to learn.")

with open("file2.txt", "w") as f:
    f.write("File handling is important in Python.")

summary = open("summary.txt", "w")

# Read each file and count words
for filename in ["file1.txt", "file2.txt"]:
    with open(filename, "r") as f:
        text = f.read()
        count = len(text.split())
        summary.write(f"{filename} -> {count} words\n")

summary.close()

print("Summary Created!")

# Delete one file
os.remove("file2.txt")

print("file2.txt deleted.")