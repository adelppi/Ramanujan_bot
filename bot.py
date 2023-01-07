import discord
import DONT_README
import random
import time
import glob
import os
import subprocess
import emoji
from Expressions.mathExpressions import *
from Expressions.latexConverter import latex2png
from Expressions.voiceExpressions import statement2mp3
from Expressions.graphExpressions import graphDisplay
from Expressions.primeGuess import primeCheck, primeDisplay
from Expressions.imageCrawling import imageCrawler
from Expressions.URLImageSaver import URLSave
from Expressions.AIChat import chat
from Expressions.qrCode import qrGen
from Expressions.emoji import emojiReact

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("LOGGED IN")
    channel = client.get_channel(1047422842276425789)
    await channel.send("おはよう")

@client.event
async def on_message(message):
    print(f"{message.author}")
    if message.attachments != [] and "ラマヌジャン、" in message.content:
        print(message.attachments[0])
    if message.author.bot:
        return

    # terms = emojiReact(message.content)
    # terms = ["spaghetti", "sushi"]
    # for term in terms:
    #     await message.add_reaction(emoji.emojize(":" + term + ":"))

    if "!式 " in message.content:
        cmdInput = message.content.replace("!式 ", "").replace(" ", "{}").replace("=", "{=}")
        latexURL = "https://latex.codecogs.com/png.image?\dpi{1000}" + cmdInput
        try:
            latex2png(latexURL)
            await message.channel.send(file = discord.File("./Expressions/images/formula.png"))
        except Exception as e:
            await message.channel.send("エラー")
            print("ERROR OCCURED", e)

    if "!積分 " in message.content:
        cmdInput = message.content.replace("!積分 ", "")
        latexURL = "https://latex.codecogs.com/png.image?\dpi{1000}" + integrate(cmdInput).replace(" ", "{}").replace("=", "{=}")
        try:
            latex2png(latexURL)
            await message.channel.send(file = discord.File("./Expressions/images/formula.png"))
        except Exception as e:
            print("ERROR OCCURED", e)
            await message.channel.send("")
    
    if "!微分 " in message.content:
        cmdInput = message.content.replace("!微分 ", "")
        latexURL = "https://latex.codecogs.com/png.image?\dpi{1000}" + differential(cmdInput).replace(" ", "{}").replace("=", "{=}")
        try:
            latex2png(latexURL)
            await message.channel.send(file = discord.File("./Expressions/images/formula.png"))
        except Exception as e:
            print("ERROR OCCURED", e)
            await message.channel.send("")

    if "!行列式" in message.content:
        cmdInput = message.content.replace("!行列式", "").splitlines()
        del cmdInput[0]
        try:
            latexURL = "https://latex.codecogs.com/png.image?\dpi{1000}" + determinant(cmdInput).replace(" ", "{}").replace("=", "{=}")
            latex2png(latexURL)
            await message.channel.send(file = discord.File("./Expressions/images/formula.png"))
        except Exception as e:
            print("ERROR OCCURED", e)
            await message.channel.send("")
    
    if "!固有値" in message.content:
        cmdInput = message.content.replace("!固有値", "").splitlines()
        del cmdInput[0]
        try:
            latexURL = "https://latex.codecogs.com/png.image?\dpi{1000}" + eigenvalue(cmdInput).replace(" ", "{}").replace("=", "{=}")
            latex2png(latexURL)
            await message.channel.send(file = discord.File("./Expressions/images/formula.png"))
        except Exception as e:
            print("ERROR OCCURED", e)
            await message.channel.send("")

    if "!QR" in message.content:
        cmdInput = message.content.replace("!QR ", "")
        qrGen(cmdInput, emoji = False)
        await message.channel.send(file = discord.File("./Expressions/images/qr.png"))

    if "!画像" in message.content:
        cmdInput = message.content.replace("!画像 ", "")
        filename = max(glob.glob("./Expressions/images/000001.*"))
        os.remove(filename)
        imageCrawler(cmdInput)
        filename = max(glob.glob("./Expressions/images/000001.*"))
        await message.channel.send(file = discord.File(filename))

    if message.attachments != [] and "ラマヌジャン、" in message.content:
        cmdInput = "画像を加工するプログラムをPythonとOpenCVで作ってください。解説等はいりません。条件は以下です。" + message.content.replace("ラマヌジャン、", "") + "。" + "入力画像のパスは'./Expressions/images/img_edit_input.png'としてください。出力画像のパスを'./Expressions/images/img_edit_output.png'としてください。.pyの形式の実行可能なソースコードのみを示してください。必要であれば他のライブラリも使ってよい。また、学習済みモデルを使用する場合、モデルのパスは'./models'を参照すること。"
        result = chat(cmdInput).replace("python", "").replace("Python", "").replace("`", "")
        f = open("./Expressions/imgEdit.py", "w")
        f.write("import numpy as np")
        f.write(result)
        f.close()
        URLSave(message.attachments[0], "./Expressions/images/img_edit_input.png")
        subprocess.run(["python", "./Expressions/imgEdit.py"])
        await message.channel.send(file = discord.File("./Expressions/images/img_edit_output.png"))
        os.remove(max(glob.glob('./Expressions/images/img_edit_input.*')))

    if "!グラフ " in message.content:
        cmdInput = message.content.replace("!グラフ ", "")
        graphDisplay(cmdInput)
        await message.channel.send(file = discord.File("./Expressions/images/graph.png"))

    if "!乱数 " in message.content:
        cmdInput = message.content.replace("!乱数 ", "").replace("整数", "0 ").replace("小数", "1 ").replace("から", " ").replace("まで", "")
        await message.channel.send(f"{randNum(cmdInput)}")

    if "!MAKE10" in message.content:
        await message.channel.send(" ".join([str(random.randint(0, 9)) for _ in range(0, 4)]))

    if "!素因数分解ゲーム" in message.content:
        question = randNum("0 100 10000")
        realAnswer = primeDisplay(question)
        statement = str(question) + "を素因数分解せよ。"
        statement2mp3(statement)
        await message.author.voice.channel.connect()
        await message.channel.send(f"{question}を素因数分解せよ。")
        await message.channel.send(f"答えは||     {realAnswer}     ||")
        await message.guild.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("./Expressions/voices/voice.mp3"), volume=0.5))
        # await message.guild.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("/home/pi/Saves/bot/voices/den.mp3"), volume=0.5))
        # await message.guild.voice_client.disconnect()
        # userAnswer = primeCheck(message.content)

    if "!素因数分解 " in message.content:
        cmdInput = message.content.replace("!素因数分解 ", "")
        latexURL = "https://latex.codecogs.com/png.image?\dpi{1000}" + primeDisplay(int(cmdInput)).strip().replace(" ", " \\times ").replace(" ", "{}").replace("=", "{=}")
        latex2png(latexURL)
        await message.channel.send(file = discord.File("./Expressions/images/formula.png"))

    if "ラマヌジャン、" in message.content and message.attachments == []:
        cmdInput = message.content.replace("ラマヌジャン、", "")
        await message.channel.send(chat(cmdInput))

    if "!join" in message.content:
        await message.author.voice.channel.connect()

    if "!read " in message.content:
        statement = message.content.replace("!read ", "")
        statement2mp3(statement)
        await message.guild.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("./Expressions/voices/voice.mp3"), volume=0.5))

client.run(DONT_README.TOKEN)