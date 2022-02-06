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
        if string in all_objs.keys():
            print(all_objs[string])
            return
        print("** no instance found **")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id"""
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
        if string in all_objs.keys():
            del all_objs[string]
            storage.save()
            return

    def do_all(self, *args):
        """Prints all string representation of
        all instances based or not on the class name"""
        all_objs = storage.all()
        list_objs = []
        if args[0] == '':
            for k, v in all_objs.items():
                list_objs.append(str(v))
            print(list_objs)
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        for k, v in all_objs.items():
            if args[0] == type(v).__name__:
                list_objs.append(str(v))
        print(list_objs)

    def do_update(self, *args):
        """Updates an instance based on the class
        name and id"""
        all_objs = storage.all()
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
        if string not in all_objs.keys():
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        obj = all_objs[string]
        try:
            a = float(arg[3])
            if a.is_integer():
                a = int(a)
        except (TypeError, ValueError):
            """setattr(obj, arg[2], str(arg[3]))"""
            setattr(all_objs[string], arg[2], str(arg[3]))
            storage.save()
            return
        """setattr(obj, arg[2], a)"""
        setattr(all_objs[string], arg[2], a)
        storage.save()
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
