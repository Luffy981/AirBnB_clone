#!/usr/bin/python3
"""modulo cmd"""
import cmd
import models import storage_obj
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Airbnb's command interpreter"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_create(self, line_args_obj):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if line_args_obj == "" or line_args_obj is None:
            print('** class name missing **')
        elif line_args_obj not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = ("{}".format(line_args_obj))
            new_instance.save()
            print(new.id)
        
    def do_show(self, line_args_obj):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = line_args_obj.split(' ')
        if line_args_obj == "" or line_args_obj is None:
            print("** class name missing **")
        elif line_args_obj not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False     
        
        all_objects = storage_obj.all()
        for i in all_objects.keys():
            if i == "{}.{}".format(args[0], args[1]):
                print(all_objects[i])
        print("** no instance found **")
    
    def do_destroy(self, line_args_obj):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = line_args_obj.split(' ')
        if line_args_obj == "" or line_args_obj is None:
            print("** class name missing **")
        elif line_args_obj not in self.my_classes:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage_obj.all()
            for i in all_objects:
                if i == "{}.{}".format(args[0], args[1]):
                    all_objects.pop(i)
                    storage_obj.save()
        print("** no instance found **")
    
    def do_all(self, line_args_obj):
        """
         Prints all string representation of all instances
         based or not on the class name.
        """

    def do_update(self, line_args_obj):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        args_cut = line_args.split(' ')
        if len(line_args_obj) < 1:
            print("** class name missing **")
        elif ("no entiendo: Si el valor del nombre del atributo no existe, imprima"):
            print("** value missing **")           


    def emptyline(self, args):
        "method that is called when an empty line is entered"
        pass

    def do_help(self, args):
        """define help options"""
        cmd.Cmd.do_help(self, args)

    def do_EOF(self, args):
        "End-of-file command to exit the console"
        return true
    
    def do_quit(self, args):
        "Quit command to exit the program"
        return true

if __name__ == '__main__':
    HBNBCommand().cmdloop()