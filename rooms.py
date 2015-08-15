# Rooms module
# Create, Store, find rooms in archive

import os

# Directory path to users database + name of file
# Later it will be changed with the help of os module
# On my desktop
ROOMS_DATABASE = '/Users/mikhail/Documents/Progs/chat/rooms_db'
# On my laptop 
EEE_ROOMS_DATABASE = '/home/mikhail/Karma/chat/rooms_db'

class Rooms:
    '''This class is for room operations - creation, management, etc.'''
    def __init__(self):
        # Container for rooms, 
        # {id:{'roomname':roomname, 'users':{user1_id, user2_id, ...}}, ...}
        self.room_bag = {}

        # Container for room Id's
        self.roomid_bag = set()

        # Container for room Names
        self.roomname_bag = set()

        # Fullfill containers
        with open(EEE_ROOMS_DATABASE, encoding='utf-8') as room_file:
            for line in room_file:
                split_line = line.split(sep=',')
                self.room_bag[int(split_line[0])] = {'roomname':split_line[1]}
                self.room_bag[int(split_line[0])]['users'] = \
                    set(split_line[2:]).difference('\n') # minus '\n' element included in split_line
                self.roomid_bag.add(int(split_line[0]))
                self.roomname_bag.add(split_line[1])

    def createRoom(self):
        '''Create room'''
        roomname = input('Input room name\n')

        if roomname not in self.roomname_bag and 'rooms_db.log' not in os.listdir():

            with open(EEE_ROOMS_DATABASE, mode='a', 
                      encoding='utf-8') as room_file:
                if self.roomid_bag:
                    new_id = max(self.roomid_bag) + 1
                elif not self.roomid_bag:
                    new_id = 1
                room_file.write(str(new_id) + ',' + str(roomname) + ',\n')

                self.room_bag[new_id] = {'roomname':roomname, 'users':set()}

                self.roomid_bag.add(new_id)
                self.roomname_bag.add(roomname)
                print('New good room created!')
        elif roomname in self.roomname_bag:
                print('Room name is in use, input another name')
        else:
            raise NameError('Bad name input')

    def addUser(self, room_id, user_id):
        """Add user <user_id> to room <room_id>, make note in rooms_db"""
        if 'rooms_db.log' not in os.listdir():
            # Creating .log file, 'x' mode means opening file
            # for exclusive creation
            with open('rooms_db.log', 'x') as logger:
                 pass
            # Update database class attributes
            self.room_bag[room_id]['users'].add(str(user_id))
            # Updating database file
            with open('rooms_db', 'w', encoding='utf-8') as rooms_db:
                for key in self.room_bag.keys():
                    rooms_db.write(str(key) + ',' + 
                                   self.room_bag[key]['roomname'] + ',')
                    for user in self.room_bag[room_id]['users']:
                        rooms_db.write(str(user) + ',')
                        
                    rooms_db.write('\n')
            # Delete .log file, free rooms_db for other process to write
            os.remove('rooms_db.log')


if __name__ == '__main__':
    print('Start testing')
    room1 = Rooms()
    room1.addUser(1,2)
