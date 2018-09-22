import os

# Set the path variable to the path of the directory you want to operate on.
path = "_replace_the_path_to_the_dir_"
os.chdir(path)

for f in os.listdir():

    fileName, fileExtension = os.path.splitext(f)

    if fileName.startswith("0") or fileName.startswith("1"):
        fileName = fileName.split()
        if len(fileName[0]) <= 2:
            print("-------inside (' ')", fileName)
            del fileName[0]

        fileName = "{}".format(" ".join(fileName))
        print("-------inside (' ')", fileName)

    if fileName.startswith("0") or fileName.startswith("1"):
        fileName = fileName.split(".")
        if len(fileName[0]) <= 2:
            print("++++++ inside (.) ", fileName)
            del fileName[0]

        fileName = "{}".format(" ".join(fileName))
        print("++++++ inside (.) ", fileName)

    if fileName.startswith("0") or fileName.startswith("1"):
        fileName = fileName.split("-")
        if len(fileName[0]) <= 2:
            print("++++++ inside (-) ", fileName)
            del fileName[0]

        fileName = "{}".format(" ".join(fileName))
        print("++++++ inside (-) ", fileName)
    os.rename(f, "{}{}".format(fileName, fileExtension))
