API_URL = 'https://rag-service-855077868686.europe-west10.run.app'

# FIXME move to utils.py
from datetime import date
def date2str(d: date) -> str:
    return d.strftime("%Y-%m-%d")
