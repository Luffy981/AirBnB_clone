#!/usr/bin/python3
"""modulo cmd"""
import cmd
import models
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Airbnb's command interpreter"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_create(self, args_nameclass):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if args_nameclass == "" or args_nameclass is None:
            print('** class name missing **')
        elif args_nameclass not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = ("{}".format(args_nameclass))
            new_instance.save()
            print(new.id)
        
    def do_show(self, args_nameclass):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        if args_nameclass == "" or args_nameclass is None:
            print("** class name missing **")
        else:
            if args_nameclass not in self.classes:
                print("** class doesn't exist **")
        "__id"
        
        "________Si la instancia del nombre de la clase no existe para la identificación,"
        "___________imprima ** no se encontró ninguna instancia **"
    
    def do_destroy(self, args_nameclass):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if args_nameclass is None:
            print("** class name missing **")
        elif args_cut not in self.my_classes:
            print("** class doesn't exist **")
        elif len(args_cut) < 2:
            print("** instance id missing **")
        else:
            "________Si la instancia del nombre de la clase no existe para la identificación,"
            "___________imprima ** no se encontró ninguna instancia **"
    
    def do_all(self, args_nameclass):
        """
         Prints all string representation of all instances
         based or not on the class name.
        """

    def do_update(self, args_nameclass):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        args_cut = line_args.split(' ')
        if len(args_nameclass) < 1:
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