import os
import json

import requests


class SlackBot:
    def __init__(self, token):
        self.token = token
    
        self.urls = {
            'send_msg': 'https://slack.com/api/chat.postMessage',
            'channel_list': 'https://slack.com/api/conversations.list'
        }
        
        self.headers = {
            # 'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ self.token
        }

    def send_msg(self, channel, msg):
        url = self.urls['send_msg']
        channel = channel

        params = {
            'channel':channel,
            'text':msg
        }

        res = requests.post(url, data=json.dumps(params), headers=self.headers)

        print(res.json())
        return res.json()

        """sample for attachment
        params = {
            'channel':'C01LMTER118',
            'text':'hello world',
            "attachments": [{
                "text":"Who wins the lifetime supply of chocolate?",
                "fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.",
                "color":"#3AA3E3","attachment_type":"default",
                "callback_id":"select_simple_1234",
                "actions":[
                    {
                        "name":"winners_list",
                        "text":"Who should win?",
                        "type":"select",
                        "data_source":"users"
                        }
                        ]
                }]
        }
        """



