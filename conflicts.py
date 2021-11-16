import csv

def read_cell(x, y):
    with open('merged dataset.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

f = open('merged dataset.csv', 'r')
file = open('final merged dataset.csv', 'w')

for i in range(842):
    conflict = read_cell(1, i)
    if 'Interpersonal' in conflict and 'Religion' not in conflict:
        conflict = 'Interpersonal'
    elif 'Religion' in conflict and 'Interpersonal' not in conflict:
        conflict = 'Religion'
    else:
        conflict = 'Interpersonal and Religion'
    file.write(str(read_cell(0, i))+','+str(conflict)+','+str(read_cell(2, i))+','+str(read_cell(3, i))+',"'+str(read_cell(4, i))+'",'+str(read_cell(5, i))+','+str(read_cell(6, i))+'\n')

file.close()