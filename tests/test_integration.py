from .context import monarchy
from monarchy import batch_registry_builder


# WARNING: it's an integration text testing whole functionality, including downloading a json file from the internet
# it's slow

def test_get_monarchs():
    reg = batch_registry_builder.get()

    assert reg is not None

