# this program is to play around with files
count = 0
fhand = open('R@1n.txt', mode = 'r')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('I'):
        print(line)
