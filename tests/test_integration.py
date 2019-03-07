from .context import monarchy
from monarchy import downloader
from monarchy import config
from monarchy import json_parser


# WARNING: it's an integration text testing whole functionality, including downloading a json file from the internet
# it's slow

def test_get_monarchs():
    r = downloader.get(config.MONARCHS_URL)
    monarchs = json_parser.parse(r)

    assert len(monarchs) > 10

