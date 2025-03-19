# List
# Author: Jin Kaifeng


def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    # print name + "Evans"
    for name in studentNames:
        print(f"{name} Evans")
    return studentNames

def addToList(studentNames):
    new_name = input("Enter a new name: ")
    studentNames.append(new_name)
    
    print("Update list：")
    for name in studentNames:
        print(f"{name} Evans")

# main
if __name__ == "__main__":
    studentNames = studList()
    addToList(studentNames)


