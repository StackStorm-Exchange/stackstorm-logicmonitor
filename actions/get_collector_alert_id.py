import re
from st2common.runners.base_action import Action

__all__ = [
    'GetCollectorAlertId'
]

class GetCollectorAlertId(Action):
    def run(self, alert_url):
        collector_id = re.search(r'collectors/ack-(\d+)', alert_url)
        if collector_id != None:
            return collector_id.group(1)
        return None
