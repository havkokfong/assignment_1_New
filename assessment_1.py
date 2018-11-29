"""
Replace the contents of this module docstring with your own details.
"""
import csv


MENU = (">>> Menu:\n'L' - List songs\n'A'- Add new song\n'C' - Complete a song\n'Q' - Quit\n\nPlease select your choices:\n>>> ")


def main():
    print("Songs To Learn 1.0 - by <Kokfong Hav>")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            print("This is your songs list:")
            with open('songs.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                count = 0
                for line in csv_reader:
                    count += 1
                    print("{:<1}.".format(count), "{:<35s}- {:<25s} ({:^4s})".format(line[0], line[1], line[2]))
            print("\n")
            choice = input(MENU).upper()
        elif choice == "A":
            song_lists = []
            song_title = input("Please enter your song title: ")
            while not titlecheck(song_title):
                print("You have entered an invalid title.")
                song_title = input("Please enter your song title: ")
            song_lists.append(song_title)
            song_artist = input("Please enter the artist name: ")
            while not artistcheck(song_artist):
                print("You have entered an invalid title.")
                song_artist = input("Please enter the artist name: ")
            song_lists.append(song_artist)
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
    if titlelenght > 0 and titlelenght < 30:
        return True
    return False


def artistcheck(song_artist):
    artistlength = len(song_artist)
    if artistlength > 0 and artistlength < 20:
        return True
    return False


def yearcheck(song_year):
    yearlenght = len(song_year)
    if yearlenght != 4:
        return False
    return True


main()

