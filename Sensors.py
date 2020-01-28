import math

filename=input("Filename: ")
# filename = 'sensors_data.txt'
f = open(filename, 'r')

sen_text = ''
for line in f:
    sen_text += line

sensors = []
sensors = sen_text.split('\n')
sens = []
sensors2 = []
for i in range(len(sensors)):
    sens = sensors[i].split(',')
    sensors2.append(sens)

sensors = [[float(elem) for elem in s] for s in sensors2]

del sensors2

neighbours_distance = float(input("Neighbours distance: "))
max_err = float(input("Max error: "))

sensors_to_check = []
# find neighbours of a sensors
for p in sensors:
    neighbours = sensors[:]
    for t in sensors:
        if math.hypot(math.fabs(p[0] - t[0]), math.fabs(p[1] - t[1])) > neighbours_distance:
            neighbours.remove(t)
    if len(neighbours)>1:
        for k in neighbours:
            if p[2] - k[2] > max_err:
                sensors_to_check.append(p)

s2=[]
for i in sensors_to_check:
    if i not in s2:
        s2.append(i)
sensors_to_check=s2
del s2

if len(sensors_to_check):
    print("Please check sensors at: ", end='')
    for i in sensors_to_check:
        if i == sensors_to_check[len(sensors_to_check) - 1]:
            print(f"({i[0]},{i[1]})")
        else:
            print(f"({i[0]},{i[1]}), ")
