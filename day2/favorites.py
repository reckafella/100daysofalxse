import csv

with open('favorites.csv', 'r') as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row['problem']
        
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

favorite = input('What is your favorite problem? ')

if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
else:
    print(f"{favorite}: Not found in the list.")
