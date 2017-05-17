import requests
import json
from app.helpers.static import SD
from config import configuration


class ApiUser(object):
    def __init__(self):
        self.headers = SD.headers()

    def post_panel_login(self, email, phone, password):
        data = {'email': email, 'phone': phone, 'password': password}
        res = requests.post(''.join([configuration.API_URL, 'user/panel-login']), headers=self.headers, data=json.dumps(data))
        return res
