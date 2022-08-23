# Write your solution here
editor = input("Editor:").lower()
string = "visual studio code"
while True:
    if editor == "emacs" or editor == "vim" or editor == "atom":
        print("not good")
    elif editor == "word" or editor == "notepad":
        print("awful")
    elif editor == string:
        print("an excellent choice!")
        break
    editor = input("Editor: ").lower()
