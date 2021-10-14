import os


while True:
    files = os.listdir()
    files.remove("main.py")

    for file in files:
        if file == ".git" or not file.endswith(".py"): 
            files.remove(file)
    os.system('cls' if os.name == 'nt' else 'clear')        
    print("Select an option (or type exit):")
    for file in files:
        index = files.index(file)
        print(f"({index + 1}) {file}")

    selection = input("\nSelection: ")

    if selection == "exit":
        break
    else:
        os.system(f"python3 {files[int(selection) - 1]}")


