import json
import glob
import csv

# Get a list of all JSON files in the current directory
json_files = glob.glob('*.json')

# Loop through each JSON file
for file in json_files:
    with open(file, 'r') as json_file:
        data = json.load(json_file)

        # Extracting data for conversion
        energies = data['Total Dos']['energies']
        densities = data['Total Dos']['densities']['1']

        # Combining energies and densities into a list of tuples
        combined_data = list(zip(energies, densities))

        # Writing to CSV
        with open(f'{file[:-5]}.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Energy', 'Density'])
            writer.writerows(combined_data)
