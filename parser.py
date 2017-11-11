import csv
import os.path

NO_PARTICIPATS = 8
NO_TASKS = 3

MOVE_FILE_TPL = "data/ID_{id}_{ver}_condition1_move.csv"
POINT_FILE_TPL = "data/ID_{id}_{ver}_condition1_pointing.csv"


def finish_time(reader):
    return int(list(reader)[-2][2])  # last line is empty list


for p in range(1, NO_PARTICIPATS + 1):
    for t in range(NO_TASKS):
        move_times_sum = 0
        move_files_parsed = 0
        fname = MOVE_FILE_TPL.format(id=p, ver=t)
        if os.path.isfile(fname):
            with open(fname, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                move_times_sum += finish_time(reader)
                move_files_parsed += 1
                for row in reader:
                    [x, y, time] = row
        point_times_sum = 0
        point_files_parsed = 0
        fname = POINT_FILE_TPL.format(id=p, ver=t)
        if os.path.isfile(fname):
            with open(fname, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                point_times_sum += finish_time(reader)
                point_files_parsed += 1
                for row in reader:
                    [x, y, time, target] = row
print('Average move finish time: {move_time}\tAverage point finish time: {point_time}'.format(move_time=move_times_sum / move_files_parsed, point_time=point_times_sum / point_files_parsed))
