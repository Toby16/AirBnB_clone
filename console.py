#!/usr/bin/env python3
"""
Console
    contains the entry point of the command interpreter
"""
from models.base_model import BaseModel
from models import storage
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            # check if class name is missing
            print("** class name missing **")
        elif arg != BaseModel.__name__:
            # check if class name is missing
            print("** class doesn't exist **")
        else:
            # create new instance of BaseModel
            model_value = BaseModel()
            # save it to json file
            model_value.save()
            # print the id
            print(model_value.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if not args:
            # check if class name is missing
            print("** class name missing **")
        elif args[0] != BaseModel.__name__:
            # check if class name doesn't exist
            print("** class doesn't exist **")
        elif len(args) < 2:
            # check if instance id is missing
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]

            key = "{}.{}".format(class_name, instance_id)
            instance = storage.all()

            if key in instance:
                """
                Prints the string representation of an instance
                    based on the class name and id
                """
                print(instance[key])

                # print(instance[key].id)
                # print(instance[key].created_at)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance
        based on the class name and id
        and saves the change into the JSON file
        """
        args = arg.split()
        if not args:
            # check if class name is missing
            print("** class name missing **")
        elif args[0] != BaseModel.__name__:
            # check if class name doesn't exist
            print("** class doesn't exist **")
        elif len(args) < 2:
            # check if instance id is missing
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]

            key = "{}.{}".format(class_name, instance_id)
            instance = storage.all()

            if key in instance:
                # delete the instance from storage
                del instance[key]
                # save changes to json file
                storage.save()
            else:
                # check if instance is not found
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        instance = storage.all()
        # check if class name is missing
        if not args:
            lst = []
            for key in instance:
                lst.append(str(instance[key]))
            # print all instances as string in list
            print(lst)
        elif args[0] == BaseModel.__name__:
            lst = []
            for key in instance:
                class_name, id_val = key.split(".")
                # check if instance class is same as BaseModel class
                if class_name == BaseModel.__name__:
                    lst.append(str(instance[key]))
            # print all instances of BaseModel as string in list
            print(lst)
        else:
            """
            if class name doesn't exist
            """
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        args = arg.split()
        # check if class name is missing
        if not args:
            print("** class name missing **")
        elif args[0] != BaseModel.__name__:
            # check if the class name doesn't exist
            print("** class doesn't exist **")
        elif len(args) < 2:
            # check if instance id is missing
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instance = storage.all()

            if key not in instance:
                # check if instance is not found
                print("** no instance found **")
            elif len(args) < 3:
                # check if attribute name is missing
                print("** attribute name missing **")
            elif len(args) < 4:
                # check if value for the attribute name doesn't exist
                print("** value missing **")
            else:
                # get the attribute name and value
                attribute_name = args[2]
                attribute_value = args[3]

                # cast the value to the correct type
                try:
                    attribute_value = eval(attribute_value)
                except (NameError, SyntaxError, TypeError, ValueError):
                    # eval can raise a lot of error
                    #   but there are the common ones
                    pass

                # update the attribute value of the instance
                instance[key].__dict__[attribute_name] = attribute_value

                # save changes to json file
                instance[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()