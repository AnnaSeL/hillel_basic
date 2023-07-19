import json


with open('acdc.json') as file:
    info = json.load(file)

tracks = info['album']['tracks']['track']

total_duration = 0
for track in tracks:
    duration = int(track['duration'])
    total_duration += duration


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"

print("Загальна тривалість всіх треків у секундах:", total_duration)
print("Загальна тривалість всіх треків у форматі години:хвилини:секунди:", format_duration(total_duration))
