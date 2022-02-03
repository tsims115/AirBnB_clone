#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
import sys
import inspect


class HBNBCommand(cmd.Cmd):
    """
    This class inherits from cmd and is a command line
    interpreter for AirBnb clone
    """

    intro = 'Welcome to the HBNB shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    do_EOF = do_quit

    def do_create(self, cls):
        """Creates new instance of BaseModel\n"""
        if cls is None:
            print('** class name missing **')
        if inspect.isclass(cls) is False:
            print("** class doesn't exist **")

    def do_show(self, *args):
        """Prints string representation of instance\n"""
        print(args)



if __name__ == '__main__':
        HBNBCommand().cmdloop()
