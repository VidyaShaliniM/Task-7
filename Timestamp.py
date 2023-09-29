import datetime

# def create_timestamp_file():
current_timestamp = datetime.date.today()
date_str = current_timestamp.strftime('%Y-%m-%d')

# Create a text file with timestamp as filename

file_name = f"{date_str}.txt"

# Write timestamp to file
with open(file_name, "w") as file:
    pass

print(f'Created file: {file_name}')




