from config import configuration


class SD:
    @staticmethod
    def headers():
        return {'Access-Token':  None,
                'Content-Type': 'application/json',
                'Reseller-Token': configuration.RESELLER_TOKEN
                }
