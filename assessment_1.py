"""
Replace the contents of this module docstring with your own details.
"""

song_file = open("songs.csv", "r")

MENU = ("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n\nPlease select your choices:\n>>> ")

def main():
    print("Songs To Learn 1.0 - by <Kokfong Hav>")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            print("This is your songs list:")
        elif choice == "A":
            print()
        elif choice == "C":
            print()
        else:
            print("Please enter the valid letter.")
            choice
    exit()
main()
song_file.close()
