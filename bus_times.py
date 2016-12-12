import logging
import urllib2
import json
import datetime

from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

API_BASE="https://api.tfl.gov.uk/StopPoint"
BUS_STOP = "490012875W" # St Paul's Road / Ramsey Walk

@ask.intent("GetBusTimes", convert={'bus_number': int})
def get_bus_time(bus_number):
    if bus_number == None:
        return render_template('repeat_bus_number')

    print bus_number
    response = urllib2.urlopen(API_BASE + "/" + BUS_STOP + "/Arrivals?mode=bus&line=" + str(bus_number))
    times = json.load(response)
    round_msg = render_template('no_bus', bus_number=bus_number)
    bus_arriving = list()
    for t in times:
        if str(t[u'lineName']) == str(bus_number):
            minutes = datetime.datetime.fromtimestamp(t[u'timeToStation']).strftime('%M')
            bus_arriving.append(minutes)

    if bus_arriving:
        bus_arriving.sort()
        round_msg = render_template('bus_schedule', bus_number=str(bus_number), minutes=(", ".join(bus_arriving)))

    return statement(round_msg).standard_card(title='TFL', text=round_msg, large_image_url='https://s3-eu-west-1.amazonaws.com/mtanzi-alexa-bustimes/london-bus.png')

if __name__ == '__main__':
    app.run(debug=True)
