import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv

from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# 🔹 ボタン付きの処理用ビュー
class MyButtonView(discord.ui.View):
    @discord.ui.button(label="挨拶", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("# ドカーン💥", ephemeral=True)

# 🔹 コマンドごとの処理を関数で用意しておく
async def hello_command(ctx):
    await ctx.send("ハロー")

async def ping_command(ctx):
    await ctx.send("🏓 Pong!")

async def button_command(ctx):
    view = MyButtonView()
    await ctx.send("おはようございます！", view=view)

# 🔹 コマンド名 → 関数 の辞書（ループで登録）
command_map = {
    "hello": hello_command,
    "ping": ping_command,
    "おはよう": button_command
}

# 🔁 登録ループ（方法②スタイル）
for name, handler in command_map.items():
    bot.command(name=name)(handler)


@client.event
async def on_ready():
    print('ログインしました')

keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    client.run(TOKEN)
else:
    print("Tokenが見つかりませんでした")
