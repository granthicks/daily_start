import datetime
import os

# Current working directory for testing purposes
current_dir = os.getcwd()

# Get current date
today = datetime.datetime.today()

# Format for file name and current folders
file_name_date = str(today.strftime('%b%d')).upper()
current_year = (today.year)
current_month = str('{:02d}'.format(today.month))
formatted_date = today.strftime("%-m/%-d/%Y")

# Path to Obsidian notes folder
obsidian_notes_path = f'{current_dir}/test/{current_year}/{current_month}/'

# Check if monthly folder exists and create it if it does not
if not os.path.exists(obsidian_notes_path):
    os.makedirs(obsidian_notes_path)
    print(f"Created folder for {file_name_date[:3]}")

# Set new note path
new_note = os.path.join(obsidian_notes_path, file_name_date + '.md')

# Create daily note if it does not exist
if not os.path.exists(new_note):
    with open(new_note, 'w') as file:
        file.write(f'# Daily Notes - {formatted_date}')
    print(f"Created note for {file_name_date}")
else:
    print("Daily note already exists!")
