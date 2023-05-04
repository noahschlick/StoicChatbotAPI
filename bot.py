import discord
import responses
import os

"""
send_message
The function is designed to send a message in response to a user;s input message.
The function takes three parameters: message, user_message, and is_private. 
The message parameter represents the Discord message object that triggered the function call
The user_message parameter repesents the user's input message.
The is_private parameter is a boolean value indicating whether the message should be private.
"""
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        error_response = "I am currently not connected to the AI that helps me answer your question."
        await message.author.send(error_response) if is_private else await message.channel.send(error_response)

"""
run_discord_bot
This function is the main function for running a Discord bot that responds to user messages.
If a token is passed as a parameter to the function, it will use that token instead of the 
token stored in the DISCORD_TOKEN environment variable. If no token is passed as a parameter, 
the function attempts to retrieve the token from the environment variable.
"""
def run_discord_bot(p_token=None):
    responses.connect_AI()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Get environment token, or use your own token to make your own bot
    if p_token is None:
        l_token = os.getenv('DISCORD_TOKEN')
    else:
        l_token = p_token

    # Send message to console when called
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # Wait for a message.
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

    # Run the discord bot whenever a valid token is recieved
    while True:
        try:
            if l_token is None:
                print("Discord token is not set! If you have not set up a not visit https://discord.com/developers/docs/getting-started to create a bot.")
                l_token = input("Enter the a valid TOKEN to continue: ")
            l_token = client.run(l_token)
            break
        except Exception as e:
            print(f"An error occurred: {e}")
