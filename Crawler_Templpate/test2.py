import csv

with open('Harvard_Dataset.csv','w', newline='') as fp:
    thewriter = csv.writer(fp)
    thewriter.writerow(["3","3"])