from datetime import datetime

# Create diary file if it doesn't exist
file = open("diary.txt", "a")
file.close()

# Get user input
entry = input("Write your diary entry: ")

# Append today's date and entry
with open("diary.txt", "a") as file:
    file.write(f"\n{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
    file.write(entry + "\n")

print("\nAll Diary Entries:\n")

# Read and display all entries
with open("diary.txt", "r") as file:
    print(file.read())