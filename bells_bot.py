"""
responds to /bell with bell emoji
and /bell [number] with that many bell emojis
"""
from flask import Flask, request
from pymessenger.bot import Bot
import os
import re

app = Flask(__name__)

ACCESS_TOKEN = "EAADkEbOZAh5gBAEdycyGTD1Ysa4xYwXo8jHj5erZCb05QZBPBKf0udXjsaDNFvOt595FtXXq0n5SNlQVZAxZCYZCRcTzATqN5sTq0q8PtysGIEIpri9u60TFL0zGDa1z5Hap3TIQwdoyviWh7mUJYw7WuKdtVXD1Eu2WymSJuntAZDZD"
VERIFY_TOKEN = "aihfieah3ou1n332o48vn2-11-ud83h13"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        matchObj = re.match(r'\/bell ?([0-9]+)?', message)
                        if matchObj:
                          for i in range(0, max(10, int(matchObj.group(1) if matchObj.group(1) is not None else 1))):
                            bot.send_text_message(recipient_id, "🔔")
        return "Success"


if __name__ == "__main__":
    app.run(debug=True)
