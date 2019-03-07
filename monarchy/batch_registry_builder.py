from . import config
from . import downloader
from . import json_parser
from . import batch_registry
from . import monarch_factory


def get():
    response = downloader.get(config.MONARCHS_URL)
    monarch_dicts = json_parser.parse(response)
    monarchs = [monarch_factory.from_dict(d) for d in monarch_dicts]
    registry = batch_registry.BatchRegistry(monarchs)
    return registry


