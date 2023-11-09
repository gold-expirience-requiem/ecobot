import discord, os, requests
from discord.ext import commands
from random import choice
from time import sleep

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

bot_info = [
    "1. advice - даёт случайный совет",
    "2. img - выдаёт случайную картинку",
    "3. web - советует экологический сайт",
]

advice_info = [
    "Экономь электроэнергию",
    "Экономь воду",
    "Уменьшай потребление пластика",
    "ИСПОЛЬЗУЙ ПОВТОРНО",
    "ПЕРЕРАБАТЫВАЙ",
    "Принимайте душ вместо ванны – это позволит вам сэкономить в 3 раза больше воды",
    "Реже пользуйтесь принтером. Когда это возможно, используйте для печати обе стороны листа",
    "Регулярно размораживайте холодильник – большой слой льда ухудшает качество заморозки, что в итоге приводит к перерасходу энергии. Никогда не ставьте в холодильник горячие блюда – сначала остудите их до комнатной температуры",
    "Старайтесь покупать продукты местного производства и – желательно – сезонные",
    "Не покупайте продукты в индивидуальной пластиковой упаковке. По возможности отдавайте предпочтение нефасованным продуктам"
]

img_info = [
    "https://www.missoffice.org/upload/medialibrary/076/076b8c9e3ea4062d9d708325621ab9f7.gif",
    "https://cojo.ru/wp-content/uploads/2022/12/znak-ekologii-1.webp",
    "https://i.pinimg.com/474x/a8/2b/e0/a82be0b402378ac5201c006559363bfc.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL9otlgwJ-pC7qo_9plHkBkigFYFBP363zIaT1M-qgQvIz8_g6M2DWk5JeJaIs4T9dCsE&usqp=CAU",
    "https://tiroz.org/wp-content/uploads/2018/04/9-768x768.png",
    "https://tiroz.org/wp-content/uploads/2018/04/3-1-768x768.png",
    "https://cf2.ppt-online.org/files2/slide/w/WA6ZJIYEsGmH7NOwXuDfgUVa3CRFtM1b0QTziqhSy8/slide-7.jpg",
    "https://cf2.ppt-online.org/files2/slide/w/WA6ZJIYEsGmH7NOwXuDfgUVa3CRFtM1b0QTziqhSy8/slide-14.jpg"
]

web_info = [
    "https://ecocom.at/ru/",
    "https://ecostandardgroup.ru/",
    "https://sobirator.ru/2016/03/21/47-ecoprivychek-na-kazhdyj-den/",
    "https://dzen.ru/suite/b0633c25-5016-4757-b678-1bf1e86a29ce"
]

@bot.command()
async def img(ctx):
    await ctx.send(f"Ваша картинка: {choice(img_info)}")

@bot.command()
async def advice(ctx):
    await ctx.send(f"Ваш совет: {choice(advice_info)}")

@bot.command()
async def web(ctx):
    await ctx.send(f"Ваш сайт: {choice(web_info)}")

@bot.command()
async def info(ctx):
    await ctx.send("Список комманд")
    for i in bot_info:
        await ctx.send(i)
        sleep(0.1)


bot.run("")