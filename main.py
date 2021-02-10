import csv
import os.path
from os import path
import sys

def ConsolidateCSVs(path):
    gas_files = []
    with open('consolidated-tracks.csv', mode='w', newline='') as tracks_file:
        tracks_writer = csv.writer(tracks_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tracks_writer.writerow(['Title', 'Album', 'Artist',	'Duration (ms)', 'Rating', 'Play Count', 'Removed'])

        for filename in os.listdir(path):
            if filename[-3:] != 'csv':
                continue

            with open(path + "/" + filename, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                try:
                    for row in csv_reader:
                        tracks_writer.writerow([row['Title'], row['Album'], row['Artist'], row['Duration (ms)'], row['Rating'], row['Play Count'], row['Removed']])

                except Exception as e:
                    gas_files.append(filename)
    
    print("Congrats! All your tracks have been consolidated into one CSV file, which you will find will be called consolidated-tracks.csv")
    gas_num = len(gas_files)
    if gas_num != 0:
        print("There was/were ", gas_num, " file(s) that were unable to be added to the CSV:")
        for gas in gas_files:
            print(gas)

        print()
            

if __name__ == "__main__":
    while(True):
        print("Enter the number that you would like to select.")
        mode = input("  1 : Consolidate GPM library to one CSV\n  2 : Convert 1 CSV to playlist\n   3 : Quit")
        print()

        if mode == "1":
            mode_1 = True
            while(mode_1):
                path = input("Enter the file path to the folder that contains the CSVs: \n")
                print()
                
                if '\\' in path:
                    path = path.replace('\\', '/')
                
                if (os.path.isdir(path)):
                    ConsolidateCSVs(path)
                    mode_1 = False
                else:
                    print("Invalid directory provided. Please try again.")

        elif mode == "2":
            print("TODO")
        
        elif mode == "3":
            print("Closing program...")
            sys.exit()
        else:
            print("Invalid number provided.")