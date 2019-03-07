from .context import monarchy
from monarchy import batch_registry_builder


# WARNING: it's an integration text testing whole functionality, including downloading a json file from the internet
# it's slow

def test_get_monarchs():
    reg = batch_registry_builder.get()
    ruled_in_925 = [monarch.name for monarch in reg if monarch.has_ruled_in(925)]
    assert sorted(ruled_in_925) == ['Athelstan', 'Edward the Elder']




