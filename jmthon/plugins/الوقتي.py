import asyncio
import base64
import os
import logging
import time
from datetime import datetime
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl import functions
from jmthon import jmthon
from config import BIO

DEL_TIME_OUT = 60
normzltext = "1234567890"
namerzfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"

LOGS = logging.getLogger(__name__)

Raze = False

@jmthon.on(events.NewMessage(outgoing=True, pattern="^.اسم وقتي$"))
async def _(event):
    global Raze

    Raze = True
    while True:
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{HM}"
        LOGS.info(name)
        try:
            await jmthon(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)


@jmthon.on(events.NewMessage(outgoing=True, pattern="^.انهاء اسم وقتي$"))
async def _(event):
        global Raze
        Raze = False
        idk = await event.edit(f"**- تم ايقاف الاسم الوقتي**")

@jmthon.on(events.NewMessage(outgoing=True, pattern="^.بايو وقتي$"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%H:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = f"{BIO} |️ {HM}"
        LOGS.info(bio)
        try:
            await jmthon(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
