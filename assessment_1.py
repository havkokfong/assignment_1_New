"""
Replace the contents of this module docstring with your own details.
"""
import csv


MENU = (">>> Menu:\n'L' - List songs\n'A'- Add new song\n'C' - Complete a song\n"
        "'Q' - Quit\n\nPlease select your choices:\n>>> ")

song_list = []


with open('songs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        song_list.append(line)
csv_file.close()

for j in range(len(song_list)):
    if song_list[j][3] == "y":
        song_list[j][3] = "*"
    else:
        song_list[j][3] = " "


def main():
    print("Songs To Learn 1.0 - by <Kokfong Hav>")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            learned = 0
            unlearn = 0
            print("This is your songs list:")
            for index, element in enumerate(song_list):
                print("{:>1}.".format(index),
                      "{:<1s} {:<30s}- {:<25s}({:^4s})".format(element[3], element[0], element[1], element[2]))
            for i in range(len(song_list)):
                if song_list[i][3] == "*":
                    learned += 1
                else:
                    unlearn += 1
            print(unlearn, "is learned", learned, "songs still need to learn")
            print("\n")
            choice = input(MENU).upper()

        elif choice == "A":
            new_song_lists = []
            song_title = input("Please enter your song title: ")
            while not titlecheck(song_title):
                print("You have entered an invalid title.")
                song_title = input("Please enter your song title: ")
            new_song_lists.append(song_title)
            song_artist = input("Please enter the artist name: ")
            while not artistcheck(song_artist):
                print("You have entered an invalid title.")
                song_artist = input("Please enter the artist name: ")
            new_song_lists.append(song_artist)
            song_year = input("Please enter the year: ")
            while not yearcheck(song_year):
                print("You have entered an invalid year.")
                song_year = input("Please enter the year: ")
            new_song_lists.append(song_year)
            require = "*"
            new_song_lists.append(require)
            song_list.append(new_song_lists)
            choice = input(MENU).upper()

        elif choice == "C":
            complete = int(input("Enter the number of a song to mark as learned \n>>>"))
            song_list[complete][3] = " "
            print(song_list[complete][0])
            choice = input(MENU).upper()

        else:
            print("Please enter the valid letter.")
            choice = input(MENU).upper()
    print(len(song_list), "songs saved to songs.csv")
    print("Have a nice day.")
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

