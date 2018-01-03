import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file
from fsm import TocMachine

from transitions.extensions import GraphMachine

API_TOKEN = '504422187:AAGQIQRCP0tSscMbuwMN-_xqIWo0-UQobss'
WEBHOOK_URL = 'https://e9a64e31.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
	states=[
		'start',
		'find_song',
		'find_album',
		'introduction',
		'a_insignificant_Secret',
		'a_vast_and_hazy',
		's_waves',
		's_vast_and_hazy',
		's_eleanor',
		's_the_city_is_eating_me_live',
    ],
    transitions=[
        {	#mode
            'trigger': 'advance',
            'source': 'start',
            'dest': 'introduction',
            'conditions': 'go_introduction'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'find_album',
            'conditions': 'go_find_album'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'find_song',
            'conditions': 'go_find_song'
        },
        {
            'trigger': 'advance',
            'source': 'find_album',
            'dest': 'a_insignificant_Secret',
            'conditions': 'go_i'
        },
        {
            'trigger': 'advance',
            'source': 'find_album',
            'dest': 'a_vast_and_hazy',
            'conditions': 'go_v'
        },
        {	#song
            'trigger': 'advance',
            'source': 'find_song',
            'dest': 's_eleanor',
            'conditions': 'go_e'
        },
        {	#song
            'trigger': 'advance',
            'source': 'find_song',
            'dest': 's_the_city_is_eating_me_live',
            'conditions': 'go_t'
        },
        {	#song
            'trigger': 'advance',
            'source': 'find_song',
            'dest': 's_waves',
            'conditions': 'go_w'
        },
        {	#song
            'trigger': 'advance',
            'source': 'find_song',
            'dest': 's_vast_and_hazy',
            'conditions': 'go_v'
        },
        {
            'trigger': 'go_back',
            'source': [
				'find_song',
				'find_album',
				'introduction',
				'a_insignificant_Secret',
				'a_vast_and_hazy',
				's_vast_and_hazy',
				's_eleanor',
				's_the_city_is_eating_me_live',
				's_waves'
            ],
            'dest': 'start'
        }
    ],
    initial='start',
    auto_transitions=False,
    show_conditions=True,
)

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))

@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(update.message.text)
    machine.advance(update)
    return 'ok'

@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

if __name__ == "__main__":
    _set_webhook()
    app.run()

