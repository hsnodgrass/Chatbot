from __future__ import print_function

import sys
import re

from slackbot import settings
from slackbot.bot import Bot
from slackbot.bot import listen_to
from slackbot.bot import respond_to

#Place the name of the Chatbot you are testing here. 
bot_name = '@'

'''
-----------
   TEST 1
-----------
This section will test the ability of the chatbot to recocgnise that it is being adddressed. This initial test has no expectation of specific conversational retort. 

SUCCESS: The test will be considered successful if the chatbot responds to each of the 10 querries/statements directed at it in any way. 

FAILURE: The test will be considered a failure if the chatbot declines to respond to any of the querries/statements directed at it. 
'''
@respond_to('Initiate Test 1', re.IGNORECASE)
def response_test(message):
    message.send('Initiating Test 1...')
    message.send(f'{bot_name} Hello.')
    message.send(f'{bot_name} Hi.')
    message.send(f'{bot_name} How are you?')
    message.send(f'{bot_name} Hey.')
    message.send(f'{bot_name} Good Morning.')
    message.send(f'{bot_name} Good Afternoon.')
    message.send(f'{bot_name} Good Evening.')
    message.send(f'{bot_name} Greetings.')
    message.send(f'{bot_name} Top O the morning.')

'''
--------------
   Test 2
--------------
'''

@respond_to('Initiate Test 2', re.IGNORECASE)
def conversational_test(message):
    message.send('Initiating Test 2 ...')
    message.send(f'{bot_name} What time is it?')
    message.send(f'{bot_name} Is that too early for lunch?')
    message.send(f'{bot_name} Do you have plans')
    message.send(f'{bot_name} What kind of toast  do you like')
    message.send(f'{bot_name} Are you on the Atkins diet')
    message.send(f'{bot_name} So why can\'t you eat toast?')
    message.send(f'{bot_name} Can you eat ketchup as a fruittarian?')
    message.send(f'{bot_name} What about durian?')
    message.send(f'{bot_name} Is that why you smell like that?')
   
'''
--------------
   Test 3
--------------
'''   

@respond_to('Initiate Test 3', re.IGNORECASE)
def conversational_test(message):
    message.send('Initiating Test 3 ...')
    message.send(f'{bot_name} Would you like to have a coversation with me?')
    message.send(f'{bot_name} Who does number two work for?')
    message.send(f'{bot_name} What is your name?')
    message.send(f'{bot_name} How old are you?')
    message.send(f'{bot_name} How much wood would a woodchuck chuck if a woodchuck could chuck wood? ')
    message.send(f'{bot_name} Do you have any enemies?')
    message.send(f'{bot_name} Do you know what love is?')
    message.send(f'{bot_name} Who is the first president of the United States of America?')
    message.send(f'{bot_name} What is your favorite word?')
   
   
'''
--------------
   Test 4
--------------
'''  


@respond_to('Initiate Test 4', re.IGNORECASE)
def conversational_test(message):
    message.send('Initiating Test 4 ...')
    message.send(f'{bot_name} Where do you live?')
    message.send(f'{bot_name} What direction does the sun set?')
    message.send(f'{bot_name} Can you fix a watch?')
    message.send(f'{bot_name} Why humans made an iPhone?')
    message.send(f'{bot_name} Who will win the superbowl this year')
    message.send(f'{bot_name} Who is your best friend')
    message.send(f'{bot_name} Who created you')
    message.send(f'{bot_name} How many continents are there on earth')
    message.send(f'{bot_name} What is the temperature outside')
   

#Place the chatbot API token that you created here
settings.API_TOKEN = ""
settings.DEFAULT_REPLY =  "Online"
settings.PLUGINS = [
    'slackbot.plugins',
]

def main():

    print("Starting TEST bot...")
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
