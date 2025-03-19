# List
# Author: Jin Kaifeng

studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

for name in studentNames:
    print(f"{name} Evans")

new_name = input("Enter a new name: ")
studentNames.append(new_name)

print("update list:")
for name in studentNames:
    print(f"{name} Evans")
