from click import ClickException
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def session(backoff=1):
    session = Session()
    retries = Retry(total=float('inf'), backoff_factor=backoff)
    adapter = HTTPAdapter(max_retries=retries)

    session.mount('https://', adapter)

    return session


def metadata(session=session()):
    response = session.get('https://metadata.packet.net/metadata')
    metadata = response.json()

    if not response:
        raise ClickException(metadata['error'])

    return metadata
