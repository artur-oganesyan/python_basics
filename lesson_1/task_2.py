original_seconds = int(input('Enter time in seconds: '))
h = original_seconds // 3600
m = (original_seconds - (3600 * h)) // 60
s = (original_seconds - (3600 * h) - (60 * m))
print(f'{h:02d}:{m:02d}:{s:02d}')
