from .context import monarchy
from monarchy import downloader
from monarchy import config


# WARNING: it's an integration text testing whole functionality, including downloading a json file from the internet
# it's slow

def test_get_monarchs():
    r = downloader.get(config.MONARCHS_URL)
    assert len(r) > 10
