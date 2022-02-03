#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
import sys


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

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    if str == 'EOF':
        do_EOF()


if __name__ == '__main__':
        HBNBCommand().cmdloop()
