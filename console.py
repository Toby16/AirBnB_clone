#!/usr/bin/env python3
"""Defines the class"""
import cmd
from models import storage
from models.base_model import BaseModel
import re

def split_my_string(arg):
    if len(arg) > 1:
        split_string = []
        split_string = re.split(' ', arg)
        return(split_string)
    else:
        return(None)



class HBNBCommand(cmd.Cmd):
    """Defined the class methods for AirBnB clone"""

    prompt = '(hbnb)'

    doc_header = 'Documented commands (type help commands)'
    undoc_header = 'Undocumented commands (type help commands)'
    #misc_header = 'misc_header'

    ruler = '-'
    print("|---------------------------------------------|")
    print("|-------   welcome to AirBnB clone    --------|")
    print("|-------   version 1                  --------|")
    print("|-------   for help type help         --------|")
    print("|-------   To quit/exit type quit     --------|")
    print("|---------------------------------------------|")
    print("\n\n\n\n")

    def main():
        pass

    __MyClass = {"BaseModel", "User", "State",
                 "City", "Place", "Amenity", "Review"}



    def do_create(self, line):
        """Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id. 
        Ex: $ create BaseModel"""

        arg = split_my_string(line)
        if arg is None or len(arg) == 0 :
            print("** class name missing ** (ex: $ create)")
        elif arg[0] not in HBNBCommand.__MyClass:
            print("** class doesn't exist ** (ex: $ create MyModel)")
        else:
            # print(arg[0]().id)
            storage.save()



    def do_prompt(self, line):
        "To change the prompt, type prompt <new prompt>. Eg prompt >>>"
        self.prompt = line + ': '

    def emptyline(self):
        """emptyline should not return or run the previous command"""
        pass
        # return cmd.Cmd.emptyline(self)

    def do_quit(self, line):
        """Type EOF or quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Type EOF or quit command to exit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
