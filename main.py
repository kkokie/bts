import json
import statsapi
import os


# Function to load previous start and end dates from a file
def load_previous_dates(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get('start_date'), data.get('end_date')
    return None, None


# Function to save current start and end dates to a file
def save_current_dates(file_path, start_date, end_date):
    with open(file_path, 'w') as f:
        json.dump({'start_date': start_date, 'end_date': end_date}, f)


# Function to generate game information dictionary
def generate_game_info(sched):
    game_info = {}
    for game in sched:
        game_id = game['game_id']
        game_info[game_id] = {
            'away_id': game['away_id'],
            'home_id': game['home_id'],
            'home_probable_pitcher': game['home_probable_pitcher'],
            'away_probable_pitcher': game['away_probable_pitcher']
        }
    return game_info


# Function to save game information to a JSON file
def save_game_info(file_path, game_info):
    with open(file_path, 'w') as f:
        json.dump(game_info, f, indent=4)


# Function to retrieve schedule data and save it to a JSON file if dates have changed
def save_schedule_if_changed(start_date, end_date, file_path):
    # Retrieve schedule data
    sched = statsapi.schedule(start_date=start_date, end_date=end_date)

    # Check if schedule data has changed compared to previous run
    prev_start_date, prev_end_date = load_previous_dates(file_path + "_dates.json")
    if start_date != prev_start_date or end_date != prev_end_date:
        # Generate game information dictionary
        game_info = generate_game_info(sched)

        # Save game information to a separate JSON file
        save_game_info(file_path.replace('schedule_data.json', 'game_info.json'), game_info)

        # Save current start and end dates
        save_current_dates(file_path + "_dates.json", start_date, end_date)


# Define parameters
start_date = "05/02/2024"
end_date = "05/02/2024"
file_path = "schedule_data.json"

# Retrieve and save schedule data if dates have changed
save_schedule_if_changed(start_date, end_date, file_path)
