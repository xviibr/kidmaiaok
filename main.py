import discord
from discord import app_commands
from discord.ext import commands
from myserver import server_on 
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)



class MyClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

  
    @app_commands.command(name="payment", description="ส่งช่องทางชำระเงิน")
    async def payment(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="ช่องทางชำระ",
            description="โอนแล้วรบกวนส่งสลิปด้วยนะครับ <:IUT02:1342552678521110659>",
            color=0xf4a261
        )
        embed.set_image(url="https://media.discordapp.net/attachments/947365126451916851/1363561745372942408/51d6ecdfad062bed7a1f68656996e9a1.jpg?ex=685adb55&is=685989d5&hm=8f4210c56e28c4cf37a53336bc68805f40f0987a8754e4a28866eced2e9c229f&=&format=webp&width=920&height=920")
        await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    try:
        synced = await bot.tree.sync()
        print(f"✅ ซิงค์คำสั่งแล้ว {len(synced)} คำสั่ง")
    except Exception as e:
        print(f"❌ Sync ไม่สำเร็จ: {e}")
    print(f'🟢 เข้าสู่ระบบแล้ว: {bot.user.name}')

  
    activity = discord.Game(name="BOT v.2.1")
    await bot.change_presence(status=discord.Status.online, activity=activity)


bot.tree.add_command(MyClient(bot).payment)

server_on() 

bot.run(os.getenv('TOKEN'))
