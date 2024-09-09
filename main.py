import discord 
import time
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
TOKEH = ''
bot = commands.Bot(command_prefix='/',intents=intents)
@bot.event
async def on_ready(ctx):
    await ctx.send(f'Привет! Я здесь чтобы рассказать тебе об ГП(глобальном потеплении) и показать как можно улучшить положение,напиши /tellmemore чтобы узнать подробнее об моих возможностях')
@bot.command()
async def tellmemore(ctx):
    await ctx.send(f'Мои команды-/info,/minigame,/howcanihelp')
@bot.command()
async def info(ctx):
    await ctx.send(f'Глобальное потепление - долгосрочное повышение средней температуры климатической земли, основная прична проявления данного фактора - человек')
@bot.command()
async def minigame(ctx,message, member: discord.Member = None, amount:int = None):
    await ctx.send(f'О,как я вижу ты тоже любишь миниигры ;) у меня есть парочка для тебя,выбирай 1 или 2?Даю 5 сек')
    time.sleep(5)
    ansver = message.content
    if ansver == 2:
        score = 0
        await ctx.send('Тебе выпала выбирашка!Выбирай правильные ответы и получай баллы!На каждый вопрос по 5 секунд')
        time.sleep(5)
        await ctx.send('Погнали!Выбери 1 или 2:  Глобальное потепление - не зависит от человека или Глобальное потепление- в основном вина человека')
        ansver1 = message.content
        time.sleep(5)
        if ansver1 == 2:
            await ctx.send('Ииииии!Правильно идем дальше!')
            score += 1
        elif ansver1 == 1:
            await ctx.send('Ииииии!Неудача идем дальше')
        else:
            await ctx.send('Ииии!Ты ничего не выбрал!МОЛОДЕЦ!')
            return
        time.sleep(5)
        await ctx.send('Выбери 1 или 2:  Глобальное потепление не требует внимания обычных граждан или оно требует внимание всех')
        ansver2 = message.content
        time.sleep(5)
        if ansver2 == 2:
            await ctx.send('Ииииии!Правильно идем дальше!')
            score += 1
        elif ansver2 == 1:
            await ctx.send('Ииииии!Неудача идем дальше')
        else:
            await ctx.send('Ииии!Ты ничего не выбрал!МОЛОДЕЦ!')
            return
        await ctx.send('Выбери 1 или 2:  Чтобы помочь ситуации надо уменьшить выброс угле-кислого газа в атмосферу земли или наоборот увеличить')
        ansver3 = message.content
        time.sleep(5)
        if ansver3 == 1:
            await ctx.send('Ииииии!Правильно идем дальше!')
            score += 1
        elif ansver3 == 2:
            await ctx.send('Ииииии!Неудача идем дальше')
        else:
            await ctx.send('Ииии!Ты ничего не выбрал!МОЛОДЕЦ!')
            return
        time.sleep(5)
        await ctx.send('Выбери 1 или 2:  Лучше передвигатся на машине меньше или больше')
        ansver4 = message.content
        time.sleep(5)
        if ansver4 == 1:
            await ctx.send('Ииииии!Правильно идем дальше!')
            score += 1
        elif ansver4 == 2:
            await ctx.send('Ииииии!Неудача идем дальше')
        else:
            await ctx.send('Ииии!Ты ничего не выбрал!МОЛОДЕЦ!')
            return
        await ctx.send('Итааак ты набрал {score} очков на этом закончим')
    elif ansver == 1:
        await ctx.send('Ок выбрал ты выбрал..... такс погоди-ка....а вот ты выбрал казино,угадай номер факта и побеждай!')
        time.sleep(3) 
        ansv = random.randint(1,6)
        await ctx.send('Выбирай от 1 до 6 а я пока расскажу тебе кое-что...')
        choice = message.content
        time.sleep(5)
        await ctx.send('Что такое глобальное потепление Средние климатические показатели постоянно изменяются. Считается, что Земля уже потеплела на 1,2 градуса из-за промышленных выхлопов, которые еще называют парниковыми газами (с этим разберемся отдельно). Отсчет идет с 1880 года, то есть до промышленной революции. И хоть кажется, что 1,2 градуса - это немного, но ученые еще четыре года назад говорили, что повышение температуры на 1,1 градуса по дополнительному теплу и энергии равно четырем взрывам бомбы Хиросимы в секунду.Причины глобального потепления Парниковые газы были и до промышленности. Это извержения вулканов, лесные пожары и даже дыхание живых организмов, то есть это нормальный процесс. С другой стороны - сейчас воздействие промышленности настолько велико, что процесс пошел быстрее в десятки раз.')
        time.sleep(0.5)
        if ansv !=  choice:
            await ctx.send('Ой... как я устал писать.. ой забыл про тебя такс у тебя получилось {choice} а должно быть {ansv}')
        if ansv == choice: 
            await ctx.send('Ой... как я устал писать.. ой забыл про тебя такс у тебя совпало с ответом повезло')
bot.run(TOKEH)
