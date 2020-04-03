original_seconds = int(input('Enter time in seconds: '))
h = original_seconds // 3600
m = (original_seconds % 3600) // 60
s = (original_seconds % 3600) % 60
print(f'{h:02d}:{m:02d}:{s:02d}')
