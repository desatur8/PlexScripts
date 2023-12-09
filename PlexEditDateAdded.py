import os
from plexapi.server import PlexServer
import configparser
import datetime

# Read configuration
plex_config = configparser.ConfigParser()
plex_config.read("plex_config.ini")
baseurl = plex_config.get('plex_config', 'PLEX_URL')
token = plex_config.get('plex_config', 'PLEX_TOKEN')

# Establish connection to Plex server
plex = PlexServer(baseurl, token)

# Check if the connection was successful
if plex:
    print("Connection to Plex server successful!")
    
    # Prompt for a movie name
    movie_name = input("Enter the name of the movie: ")

    # Find all movies matching the entered name in the Plex library
    matched_movies = plex.library.search(movie_name)
    if matched_movies:
        movies_list = [movie for movie in matched_movies if movie.type == 'movie']
        if movies_list:
            print(f"Found Movies:")
            for index, movie in enumerate(movies_list, start=1):
                print(f"{index}. {movie.title}")

            # Prompt for a number to select the movie
            selected_number = int(input("Enter the number of the movie you want to select: "))
            selected_movie = movies_list[selected_number - 1]  # Adjust index since it starts from 1

            # Display details of the selected movie
            print(f"Selected Movie: {selected_movie.title}")
            print(f"Plot: {selected_movie.summary}")
            
            # Get and display the 'addedAt' value for the selected movie
            added_at = selected_movie.addedAt
            print(f"Date Added: {added_at}")

            # Ask if the user wants to edit the addedAt date
            edit_choice = input("Do you want to edit the 'addedAt' date? (Y/N): ")
            if edit_choice.upper() == 'Y':
                # Prompt for a date and time to update the addedAt value
                datetime_str = input("Enter the new date and time (YYYY-MM-DD HH:MM:SS) for 'addedAt' value: ")
                try:
                    # Parse the user-input date and time
                    updated_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
                    # Create the updates dictionary for 'addedAt' value
                    updates = {"addedAt.value": updated_datetime}
                    # Update the 'addedAt' value of the selected movie
                    selected_movie.edit(**updates)
                    # Fetch the updated addedAt value and display it
                    updated_added_at = selected_movie.addedAt
                    print(f"Updated 'addedAt' value for {selected_movie.title}")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
            elif edit_choice.upper() == 'N':
                print("Exiting script.")
            else:
                print("Invalid choice. Exiting script.")
        else:
            print("No movies found.")
    else:
        print("No movies found.")
else:
    print("Failed to connect to Plex server.")
