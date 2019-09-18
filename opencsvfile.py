#initializes tkinter's filedialog and any wildcard things I need. Also opens up file explorer prompting for a file
from tkinter import filedialog
from tkinter import *
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = '/',
                                           title = 'Pick a file',
                                           filetypes=(("all files", ".*"),
                                                      ("text files", ".txt"),
                                                       ("csv files", ".csv")))

root.destroy() #kills the window

import csv #imports csv from python to work with csv files
with open(root.filename) as csv_file: #opens the file picked by user and renames it
    csv_reader = csv.reader(csv_file, delimiter=",") #Turns csv into a python readable list

    line_count = 0        #sets some varibles
    highestnumin2 = 0
    highestnumin3 = 0

    for x in csv_reader: #this script takes each row inside the file
        if line_count == 0: #reads if its the header
            print(f"You have the rows: {x[0]}, {x[1]}, and {x[2]})") #displays it
            line_count += 1 #advances to the next row
        else:
            print(f"Values are: {x[0]}, {x[1]}, and {x[2]}")#displays data
            if int(x[1]) > highestnumin2: #if the number is bigger than the previous biggest number
                highestnumin2 = int(x[1]) #saves it as the new biggest number
            else:
                pass #if the number isn't bigger than the previous number, it will do nothing
            if int(x[2]) > highestnumin3: #if the number is bigger than the previous biggest number
                highestnumin3 = int(x[2]) #saves it as the new biggest number
            else:
                pass #if the number isn't bigger than the previous number, it will do nothing
            line_count += 1 #adds one to the line count advancing it to the next row

    print(f"The highest number in the second column is {highestnumin2}")  #prints the highest number
    print(f"The highest number in the second column is {highestnumin3}")  #in each column
