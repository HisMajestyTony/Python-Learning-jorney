import os

#shows everything in current folder
#files = os.listdir()

#this is how we get a path ( ABSOLUTE PATH )
# path = "D:/Python/Repositories/python-learning-journey/image-playground"
#
# relative_path = "../image-playground"


#list files in specific folder ( currently not working like this since most likely path is wrong)
#os.listdir("python_learning_journey")


#check if file exists / Returns true of false
#os.path.exists("test.txt")

#creates new folder
#os.makedirs("new_folder")

#os.rename("old.txt", "new.txt")

#gets current working directory
# print(os.getcwd())
#
# for file in os.listdir():
#     if file.endswith(".txt"):
#         os.rename(file, f"new_{file}")


# ##Rule:
# . = current directory
# .. = one level up
# ../../ = two levels up

#BEST PRACTICE os.path.join()
base = os.path.dirname(os.getcwd())  # go one level up
target = os.path.join(base, "image-playground")

print(target)
os.listdir(target)


# Step 1: Go one level up
parent_dir = os.path.dirname(os.getcwd())

# Step 2: Build path to target folder
target_dir = os.path.join(parent_dir, "image-playground")

# Step 3: List files
files = os.listdir(target_dir)

#step 4: Build FULL file path
file_path = os.path.join(target_dir, "test2_txt")

#step 5: create the file
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("New file created safely")
else:
    print("File already exists")

file_path_notes = os.path.join(target_dir, "notes.txt")

if not os.path.exists(file_path_notes):
    with open(file_path_notes, "w") as f:
        f.write("First line\n")
        f.write("Second Line\n")
        f.write("Third line\n")

else:
    print("File already exists")

with open(file_path_notes, "a") as f:
    f.write("Last line")
counter = 0
with open(file_path_notes, "r") as f:
    for line in f:
        counter+=1
print(f"This file has {counter} lines")
print("--------------------------------------------")

files = os.listdir(target_dir)


for file in files:
    if file.endswith(".txt"):
        full_path = os.path.join(target_dir, file)

        new_counter = 0

        with open(full_path, "r") as f:
            for line in f:
                new_counter+=1
        print(f"{file} has {new_counter} lines")
