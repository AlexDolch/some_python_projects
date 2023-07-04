
from discord import Intents, Client
import responses


def run_bot(token: str):
    # Basic Setup:
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = responses.load_knowledge("knowledge.json")
    
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content:
            print(f"({message.channel}) {message.author}: '{message.content}'")
            response: str = responses.get_response(message.content, knowledge=knowledge)
            await message.channel.send(response)
        else:
            print("Could not read the message, make sure u have intents enabled!")
    
    
    client.run(token=token)

# Enter token from http://discord.com/developers/applications
if __name__ == "__main__":
    run_bot(token="token")

