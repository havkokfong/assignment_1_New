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
            #song_title = input("Please enter your song title: ")
            #song_artist = input("Please enter the artist name: ")
            while not yearcheck():
                print("You have entered an invalid year.")
        elif choice == "C":
            print()
        else:
            print("Please enter the valid letter.")
            choice
    exit()


def yearcheck():
    song_year = input("Please enter the year: ")
    yearlenght = len(song_year)
    if yearlenght < 1 or yearlenght > 4:
        return True
        song_year = input("Please enter the year: ")



main()
song_file.close()
