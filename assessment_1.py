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
            list = []
            song_title = input("Please enter your song title: ")


            song_artist = input("Please enter the artist name: ")


            song_year = input("Please enter the year: ")
            while not yearcheck(song_year):
                print("You have entered an invalid year.")
                song_year = input("Please enter the year: ")
            list.append(song_year)
            choice = input(MENU).upper()
        elif choice == "C":
            print()
        else:
            print("Please enter the valid letter.")
            choice = input(MENU).upper()
    exit()


def yearcheck(song_year):
    yearlenght = len(song_year)
    if yearlenght != 4:
        return False
    return True




main()
song_file.close()
