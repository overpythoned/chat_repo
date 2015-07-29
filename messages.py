# Messages operations module
# Prepare message delivering infrustructure

import os
import time

# Path to pipes directory
PIPES = '/home/mikhail/Karma/chat/pipes/'

def create_hello_pipe():
    """Create "hello" pipe to user-server interactions"""
    # Create hello pipe if it doesn't exist
    os.chdir(PIPES)
    if not 'hello' in os.listdir() : os.mkfifo(PIPES + 'hello')

def get_hello():
    """
    Listen for hello in hello_pipe, return tuple (True, user_id) or
    (False, user_id)
    """
    with open(PIPES + 'hello', 'r') as pipeout:
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

def read_from_pipe(user_id):
    """ Read and return one message from user-server pipe"""
    os.chdir(PIPES)
    with open(str(user_id) + '-server', 'r') as pipeout:
        return pipeout.readline()
