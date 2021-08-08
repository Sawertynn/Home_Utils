from urllib.request import urlopen

def get_solar_power(adress = "http://192.168.1.10", category = "P DC"):
    path = "gen.measurements.table.js"
    url = adress + '/' + path
    leftDiv = category + "</td><td align='right'>"
    rightDiv = "</td>"

    file = urlopen(url).readline()
    data = str(file.strip(), encoding="utf-8")

    temp = data.split(leftDiv)
    temp = temp[1].split(rightDiv)
    power = temp[0].strip()

    try:
        power = float(power)
    except ValueError:
        power = 0.0

    return power


def print_power(power, limit = 1000):
    line = "Moc: {:.1f}W, {:.0f}% limitu"
    print(line.format(power, power / limit * 100))


def buffer_switch(value, lower, upper):
    if value > upper and not buffer_switch.state:
        buffer_switch.state = True
    if value < lower and buffer_switch.state:
        buffer_switch.state = False

    return buffer_switch.state

buffer_switch.state = False
