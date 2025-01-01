from datetime import datetime


def add_event_to_calendar(event_name, start_time, end_time):
    with open("calendar.txt", "a") as file:
        file.write(f"{event_name}: {start_time} - {end_time}\n")
