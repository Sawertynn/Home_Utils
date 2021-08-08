from urllib.request import urlopen

# initial variables
adress = "http://192.168.1.10"
path = "gen.measurements.table.js"
category = "P DC"

# used constants
url = adress + '/' + path
leftDiv = category + "</td><td align='right'>"
rightDiv = "</td>"

# actual program
file = urlopen(url).readline()
data = str(file.strip(), encoding="utf-8")

temp = data.split(leftDiv)
temp = temp[1].split(rightDiv)
power = temp[0].strip()

try:
    float(power)
except ValueError:
    power = 0.0

print(power)
