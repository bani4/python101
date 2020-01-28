kaseta = input("Enter the size of the box: ")
l = kaseta.split('x')
n = int(l[0])
m = int(l[1])
garden = [['X' for i in range(m)] for j in range(n)]

rotten_data = input("Еnter the coordinates of the rotten apples: ")
rotten_list = rotten_data.split(' ')
# print(rotten_list)
# print(len(rotten_list))

rotten_coord = []
for i in range(len(rotten_list)):
    data = rotten_list[i].strip("()")
    rotten_coord.append(data.split(','))
    for j in range(2):
        rotten_coord[i][j] = int(rotten_coord[i][j])
# print(rotten_coord)

days_away = int(input("After how many days will you come back: "))


def garden_order(gard):
    for i in range(n):
        for j in range(m):
            print(gard[i][j], end=' ')
        print()


def rotten_apples(gard, r_c):
    # r_c list change
    n_r_c = r_c
    for i in range(len(r_c)):
        x = r_c[i][0]
        y = r_c[i][1]
        n_r_c.append([x - 1, y - 1])
        n_r_c.append([x - 1, y])
        n_r_c.append([x - 1, y + 1])
        n_r_c.append([x, y - 1])
        n_r_c.append([x, y + 1])
        n_r_c.append([x + 1, y - 1])
        n_r_c.append([x + 1, y])
        n_r_c.append([x + 1, y + 1])
    r_c = n_r_c

    # gard change
    for i in range(len(r_c)):
        if r_c[i][0]-1 in range(n) and r_c[i][1]-1 in range(m):
            gard[r_c[i][0]-1][r_c[i][1]-1]= 'O'


for i in range(1, days_away + 1):
    if i % 3 == 0:
        rotten_apples(garden, rotten_coord)

garden_order(garden)
