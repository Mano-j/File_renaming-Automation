import os

# Set the path variable to the path of the directory you want to operate on.
path = "_replace_the_path_to_the_dir_"
os.chdir(path)

for file in os.listdir():

    fileName, fileExtension = os.path.splitext(file)

    if fileName.startswith("0") or fileName.startswith("1"):
        fileName = fileName.split(".")
        if len(fileName[0]) <= 2:
            print("Changing the numbers separated by '.' ", fileName)
            del fileName[0]
            fileName[0] = fileName[0].strip()

        fileName = " ".join(fileName)

    if fileName.startswith("0") or fileName.startswith("1"):
        fileName = fileName.split("-")
        if len(fileName[0]) <= 2:
            print("Changing the numbers separated by '-' ", fileName)
            del fileName[0]
            fileName[0] = fileName[0].strip()

        fileName = " ".join(fileName)

    if fileName.startswith("0") or fileName.startswith("1"):
        fileName = fileName.split()
        if len(fileName[0]) <= 2:
            print("Changing the numbers separated by ' ' ", fileName)
            del fileName[0]

            fileName = " ".join(fileName)
    os.rename(file, "{}{}".format(fileName, fileExtension))
