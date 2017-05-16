from flask import g
from config import configuration


class SD:
    @staticmethod
    def headers():
        return {'Access-Token': getattr(g, 'access_token', None),
                'Content-Type': 'application/json',
                'Reseller-Token': configuration.RESELLER_TOKEN
                }
