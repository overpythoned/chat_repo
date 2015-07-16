# Messages operations module

import os
import time

# Path to pipes directory
PIPES = '/home/mikhail/Karma/chat/pipes/'

def create_hello_pipe():
    """Create "hello" pipe to user-server interactions"""
    # Create hello pipe if it doesn't exist
    if not 'hello' in os.listdir() : os.mkfifo('hello')
    
    with open('hello', 'r') as pipeout:
        return pipeout.readline()

def create_user_pipe(user_id):
    """
    Create user pipes pair - one for receiving instructions
    the other for sending information
    """
    os.chdir(PIPES)
    if not str(user_id) in os.listdir() :
        # Create pipe for receiving instructions from user
        os.mkfifo(str(user_id) + '-server')
        # Create pipe for sending information to user
        os.mkfifo('server-' + str(user_id))    


class Instructions:
    """Class for parsing and performing received instructions"""
    def __init__(self, user_id, user_bag):
        # Check for user in user_bag
        if not user_id in user_bag.keys(): 
            print('Error: user_id doesnt exist')
        else:
            # Create attributes
            self.user_id = user_id
            self.user_bag = user_bag

    def parse(self, instruction):
        """Instruction parser, return parsed instruction"""
        self.parsed = instruction.split(sep=',')
        self.tag = self.parsed[0]
        return self.parsed
