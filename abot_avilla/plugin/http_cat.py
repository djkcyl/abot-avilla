import httpx

from loguru import logger
from graia.saya import Channel

from graiax.shortcut.saya import listen, dispatch
from avilla.twilight.twilight import Twilight, ElementMatch, FullMatch, RegexMatch, RegexResult
from avilla.core import Context, MessageReceived, MessageChain, Notice, RawResource, Picture

channel = Channel.current()


@listen(MessageReceived)
@dispatch(Twilight(ElementMatch(Notice, optional=True), FullMatch("/httpcat"), "code" @ RegexMatch(r"\d+")))
async def hello(cx: Context, code: RegexResult):
    async with httpx.AsyncClient() as client:
        image_req = await client.get(f"https://http.cat/{code}")
    await cx.scene.send_message(f"Hello, world! {code.result}")
    await cx.scene.send_message([f"Hello, world! {code.result}", Picture(RawResource(image_req.content))])


@listen(MessageReceived)
async def printa(cx: Context, message: MessageChain):
    logger.info(str(message))
    await cx.scene.send_message(f"Hello, world! {message}")
