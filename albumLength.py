import re, math

file = open('TrailsOST.txt')

timeRegex = re.compile(r'''(\d?\d)?:
                           (\d?\d)''', re.VERBOSE)
totalMinutes = 0
totalSeconds = 0
             
for line in file.readlines():
    mo = timeRegex.search(line)
    if mo == None:
        continue
    minutes = int(mo.group(1))
    seconds = int(mo.group(2))
    
    totalMinutes += minutes
    totalSeconds += seconds
    
seconds = totalSeconds % 60
tempMinutes = totalMinutes + math.floor(totalSeconds/60)
minutes = tempMinutes % 60
hours = math.floor(tempMinutes/60)

if len(str(minutes)) != 2:
    minutes = '0' + str(minutes)
if len(str(seconds)) != 2:
    seconds = '0' + str(seconds)
    
print(f'Album length: {hours}:{minutes}:{seconds}')

file.close()