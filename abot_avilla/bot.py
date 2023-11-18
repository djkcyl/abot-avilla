from graia.saya import Saya
from creart import it
from avilla.core import Avilla
from avilla.qqapi.protocol import QQAPIProtocol, QQAPIConfig, Intents


qqapi_config = QQAPIConfig(
    "",
    "",
    "",
    intent=Intents(c2c_group_at_messages=True),
    # is_sandbox=True,
)
avilla = Avilla(message_cache_size=0)
avilla.apply_protocols(QQAPIProtocol().configure(qqapi_config))


saya = it(Saya)
with saya.module_context():
    saya.require("abot_avilla.plugin.http_cat")
