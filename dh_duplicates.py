import csv
file = open('dh_dataset.csv', 'w')
file.write("EventID,Conflict,Title,EP,CharacterID,CharacterName\n")
def read_cell(x, y):
    with open('rectype-59.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

for i in range(1, 359):
    cid = read_cell(4,i)
    cid = cid.split("|")
    name = read_cell(5,i)
    name = name.split("|")
    for num in range(len(cid)):
        file.write(str(read_cell(0,i))+','+str(read_cell(1,i))+','+str(read_cell(3,i))+','+str(cid[num])+',"'+str(name[num])+'"\n')

file.close()