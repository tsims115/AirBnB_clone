#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""


import cmd
import sys
import inspect
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """Creates new instance of BaseModel\n"""
        if arg == "":
            print('** class name missing **')
        elif arg == "BaseModel":
            obj = BaseModel()
            obj.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, *args):
        """Prints string representation of instance\n"""
        if args[0] == '':
            print("** class name missing **")
            return
        string = args[0]
        arg = string.split(' ')
        if arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        string = arg[0] + "." + arg[1]
        all_objs = storage.all()
        for key in all_objs.keys():
            if key == string:
                print(all_objs[key])
                return
        print("** no instance found **")


if __name__ == '__main__':
        HBNBCommand().cmdloop()
