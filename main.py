import discord
import random
import setting
import config

# Botのアクセストークン
TOKEN = config.DISCORD_BOT_TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# ランダム画像送信用のcsv読み出し
data_num, data_list = setting.get_picture_id(setting.csv_file)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    # 「/nya」と発言したら「にゃーん」が返る処理
    if message.content == '/nyan':
        await message.channel.send('にゃーん:feet::paw_prints:')
        return
    
    # 無理
    if message.content == '/muri':
        await message.channel.send('進捗ダメです')
        return
    
    # 画像リンクが送信できるかの確認
    if message.content == '/gaoo':
        await message.channel.send(setting.filelink)
        return
    
    # googleドライブにある画像からランダムで写真を送信
    if message.content == '/iyashi':
        select_num = random.randint(0, data_num)
        pic_path =  'https://lh3.googleusercontent.com/d/' + data_list[select_num]
        await message.channel.send(pic_path)
        return
    
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)