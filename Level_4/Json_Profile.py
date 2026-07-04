import json

# Step 1: Create a dictionary
profile = {
    "name": "Sruthika",
    "skills": ["Python", "Java", "Frappe", "ERPNext"],
    "level": "Beginner"
}

# Step 2: Save dictionary to profile.json
with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

print("Profile saved successfully!")

# Step 3: Read the JSON file
with open("profile.json", "r") as file:
    data = json.load(file)

# Step 4: Print each field
print("\n----- Profile Details -----")
print("Name   :", data["name"])
print("Skills :", ", ".join(data["skills"]))
print("Level  :", data["level"])