from . import config
from . import downloader
from . import json_parser
from . import batch_registry


def get():
    response = downloader.get(config.MONARCHS_URL)
    monarchs = json_parser.parse(response)
    registry = batch_registry.BatchRegistry(monarchs)
    return registry


