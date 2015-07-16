# Users module
# Contains all routins on users - creation, deletion,
# getting information about users

import os

# Directory path to users database + name of file
# Later it will be changed with the help of os module
# On my desktop
USERS_DATABASE = '/Users/mikhail/Documents/Progs/chat/users_db'
# On my laptop
EEE_USERS_DATABASE = '/home/mikhail/Karma/chat/users_db'

class Users():
    '''A declaration of class represents operations on users'''
    
    # Constructor read the users data and fullfill attributes
    def __init__(self):

        # Container for user Identities, 
        # structure is {id:{'username':username, ...}, ...}
        self.user_bag = {}
        
        # Container for user id numbers
        self.userid_bag = set()
        
        # Container for usernames
        self.username_bag = set()
        
        # Fullfill containers
        with open(EEE_USERS_DATABASE, encoding='utf-8') as user_file:
            for line in user_file:
                split_line = line.split(sep=',')
                self.user_bag[int(split_line[0])] = {'username':split_line[1]}
                self.userid_bag.add(int(split_line[0]))
                self.username_bag.add(split_line[1])

    def createUser(self):
        '''User creation routine'''
        username = input('Input Username\n')
        # Check if usernameusername already exists
        if username not in self.username_bag:
            with open(EEE_USERS_DATABASE,
                      mode='a', encoding='utf-8') as user_file:
                if self.userid_bag:
                    new_id = max(self.userid_bag) + 1
                elif not self.userid_bag:
                    new_id = 1
                user_file.write(str(new_id) + ',' + str(username) + ',\n')
                self.user_bag[new_id] = {'username':username}
                self.userid_bag.add(new_id)
                self.username_bag.add(username)
                print('Welcome, you are registered')
        elif username in self.username_bag:
            print('Username occupied')


class User:
    ''' 
    Authorize user, "hello" to MessagesHandler , Receiving information about the rooms, Enter the room, Send Message
    '''
    # Check for other users talking to server, hello if not
    def __init__(self, userid):
        while True:
            if not 'hello.log' in os.listdir():
                os.chdir('/home/mikhail/Karma/chat/pipes')
                pipein = open('hello', 'w')
                pipein.write('hello\n')
                pipein.close()
                print('Hello sent!')
                break
       


if __name__ == '__main__':
    print('Start testing')
    user1 = Users()
    user1.createUser
