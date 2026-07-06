import csv

# Write contacts
with open("contacts.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Phone", "Email"])
    writer.writerow(["Sruthika", "9876543210", "sruthika@gmail.com"])
    writer.writerow(["Rahul", "9876501234", "rahul@gmail.com"])
    writer.writerow(["Priya", "9123456780", "priya@gmail.com"])

print("Contacts Saved!\n")

# Read contacts
with open("contacts.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    print("Contact List")
    print("----------------")
    for row in reader:
        print(f"Name: {row[0]}")
        print(f"Phone: {row[1]}")
        print(f"Email: {row[2]}")
        print()

# Search Contact
search = input("Enter name to search: ")

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    found = False
    for row in reader:
        if row["Name"].lower() == search.lower():
            print("\nContact Found")
            print(row)
            found = True
            break

    if not found:
        print("Contact Not Found")