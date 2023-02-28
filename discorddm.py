import discord
import asyncio

async def main():
    email = "leonardo.kulon@gmail.com"
    password = "leoisabear"

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    await client.login(email, password)
    print("Logged in as", client.user.name)

    # Your code here

    await client.logout()

asyncio.run(main())
