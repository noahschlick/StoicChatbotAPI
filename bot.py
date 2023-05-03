import discord
import responses
import os

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    responses.connect_AI()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        # Create private chat option for users chatting with bot
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    # Run the discord bot
    while True:
        try:
            TOKEN = os.getenv('DISCORD_TOKEN')
            if TOKEN is None:
                print("Discord token is not set! If you have not set up a not visit https://discord.com/developers/docs/getting-started to create a bot.")
                TOKEN = input("Enter the a valid TOKEN to continue: ")
            TOKEN = client.run(TOKEN)
            break
        except Exception as e:
            print(f"An error occurred: {e}")

 