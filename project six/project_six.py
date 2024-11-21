"""
  ITSC 1212 - Putting the pieces together! #2
"""
######################################################
#            |\
#     -------|-\\-----
#     ------0---\|----
#     -----------|----
#     -----------0-----
######################################################

'''
    Reads a CSV file containing information about songs and returns a list of songs,
     where each song is a sublist in the format [title, artist, duration].

    filename (string): The name of the CSV file to read.
    header (boolean): Indicates whether the file has a header row that should be skipped.
'''
def load_data(filename, header):
    playlist = [ ]  # Initialize an empty list to store song data
    file_ref = open(filename.csv, "r")  # Open the file for reading

    # If there is a header row, skip it
    if header:
        file_ref.readline()  # Skip the header line by reading it and doing nothing with it

    # Read each line (song) in the file
    for info in file_ref:
        row = info.strip().split(",")  # Remove any surrounding whitespace and split by comma
        title = row[0]                 # First column is the song title
        artist = row[1]                # Second column is the artist name
        rank = int(row[2])             # Third column is the rank, converted to integer
        playlist.append([title, artist, rank])  # Append song data as a sublist

    file_ref.close()  # Close the file after reading
    return playlist   # Return the list of songs


def display_menu():
    print("****************************")
    print("Welcome to the Song Management Application!\nManage and explore songs from out collection.")
    print("****************************")
    print("\nMenu:\n1. Show song by rank\n2. Show top 10 songs\n3. Show top 20 songs\n4. Quit")

def get_user_choice():
    print("****************************")
    user_choice = input("\nEnter your input here (1-4): ")
    while not user_choice.isdigit() or not (1 <= int(user_choice) <= 4):
        print("****************************")
        print("Invalid input. Please enter a number between 1 and 4.")
        print("****************************")
        user_choice = input("Enter your input here (1-4): ")
    return int(user_choice)

def show_song_by_rank(songs):
    print("****************************")
    user_input = input("\nEnter a rank to see which song has that rank: ")
    if user_input.isdigit():
        user_rank = int(user_input)
        found_song = None
        
        # Find the song with the specified rank
        for song in songs:
            if song[2] == user_rank:
                found_song = song
                break
        if found_song:
            print("****************************")
            print(f"Rank {user_rank}: Title: {found_song[0]}, Artist: {found_song[1]}, Duration: {found_song[2]} mins")
        else:
            print(f"No song found with rank {user_rank}.")
    else:
        print("Invalid input. Please enter a valid number.")

def show_top_songs(songs, top_n):
    top_n_valid = []
    for digit in str(top_n):
        if digit.isdigit():
            top_n_valid.append(digit)

    if len(top_n_valid) > 0 and top_n > 0:
        ranked_songs = []
        # filter songs with rank <= top_n
        for song in songs:
            if song[2] <= top_n:
                ranked_songs.append(song)
        
        # sorts the filtered songs by rank
        for i in range(len(ranked_songs) - 1):
            for j in range(len(ranked_songs) - i - 1):
                if ranked_songs[j][2] > ranked_songs[j + 1][2]:
                    ranked_songs[j], ranked_songs[j + 1] = ranked_songs[j + 1], ranked_songs[j]
        
        if ranked_songs:
            print(f"\nTop {top_n} Songs:")
            for song in ranked_songs:
                print(f"Rank {song[2]}: Title: {song[0]}, Artist: {song[1]}")
        else:
            print(f"No songs found for the top {top_n} ranks.")
    else:
        print("Invalid input. Please provide a positive integer for top_n.")


"""
Main logic to run the Song Management Application.

The logic should:
1. Load the songs from the CSV file.
2. Display the menu and prompt the user to select an option.
3. Call the appropriate function based on the user’s choice.
4. Keep displaying the menu until the user chooses to quit.
"""
def main():
    # load the songs from the CSV file
    filename = "top_100_songs.csv"
    header = True
    songs = load_data(filename, header)

    print("Songs loaded successfully\n")
    
    # keep displaying the menu until the user chooses to quit
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            # shows song by rank
            show_song_by_rank(songs)
        elif choice == 2:
            # shows top 10 songs
            show_top_songs(songs, 10)
        elif choice == 3:
            # shows top 20 songs
            show_top_songs(songs, 20)
        elif choice == 4:
            print("****************************")
            print("\nThank you for using the Song Management Application. Goodbye!")
            print("****************************")
            break
main()