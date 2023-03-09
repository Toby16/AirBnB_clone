#!/usr/bin/env python3
"""
Console
    contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - class containing functions and attributes of the console
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered in the console
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
