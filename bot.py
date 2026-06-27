import os
import asyncio
import aiohttp
from datetime import datetime
import pytz

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID", "5182737074")
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def get_message():
    now = datetime.now(pytz.utc)
    return f"""📊 *تحليل NAS100 - جلسة نيويورك*
📅 {now.strftime('%d/%m/%Y')} | ⏰ 14:30 GMT

🔍 *ما يجب مراقبته:*
• راقب High/Low جلسة لندن
• ابحث عن Fair Value Gaps
• اتجاه DXY عكسي مع NAS100

⏰ *أوقات السيولة:*
• 14:30 GMT افتتاح نيويورك 🔔
• 15:00-16:00 أقوى حركة
• 20:00-21:00 نهاية الجلسة

⚠️ تحقق من الشارت قبل الدخول!"""

async def send(session, msg):
    await session.post(TELEGRAM_URL, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

async def main():
    async with aiohttp.ClientSession() as session:
        await send(session, "🚀 *البوت يعمل!* سيرسل تحليل يومي 14:30 GMT ✅")
        while True:
            now = datetime.now(pytz.utc)
            if now.hour == 14 and now.minute == 30 and now.weekday() < 5:
                await send(session, get_message())
                await asyncio.sleep(61)
            await asyncio.sleep(30)

asyncio.run(main())
