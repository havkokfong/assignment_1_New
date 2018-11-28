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
            song_lists = []
            song_title = input("Please enter your song title: ")
            while not titlecheck(song_title):
                print("You have entered an invalid title.")
                song_title = input("Please enter your song title: ")
            song_lists.append(song_title)
            song_artist = input("Please enter the artist name: ")


            song_year = input("Please enter the year: ")
            while not yearcheck(song_year):
                print("You have entered an invalid year.")
                song_year = input("Please enter the year: ")
            song_lists.append(song_year)
            choice = input(MENU).upper()
        elif choice == "C":
            print()
        else:
            print("Please enter the valid letter.")
            choice = input(MENU).upper()
    exit()


def titlecheck(song_title):
    titlelenght = len(song_title)
    if titlelenght < 1 and titlelenght > 30:
        return True
    return True


def yearcheck(song_year):
    yearlenght = len(song_year)
    if yearlenght != 4:
        return True
    return False



main()
song_file.close()
