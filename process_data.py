raw_data = []

with open('mydata.dat') as fp:
    for line in fp:
        line = line.rstrip()
        raw_data.append(line)

for item in raw_data:
    print (item)

# Just added some comment