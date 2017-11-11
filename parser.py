import csv
import os.path

NO_PARTICIPATS = 8
NO_TASKS = 3

MOVE_FILE_TPL = "data/ID_{id}_{ver}_condition1_move.csv"
POINT_FILE_TPL = "data/ID_{id}_{ver}_condition1_pointing.csv"


for p in range(1, NO_PARTICIPATS + 1):
    for t in range(NO_TASKS):
        fname = MOVE_FILE_TPL.format(id=p, ver=t)
        if os.path.isfile(fname):
            with open(fname, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    [x, y, time] = row
        fname = POINT_FILE_TPL.format(id=p, ver=t)
        if os.path.isfile(fname):
            with open(fname, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    [x, y, time, target] = row
