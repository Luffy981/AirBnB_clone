#!/usr/bin/python3
"""modulo cmd"""
import cmd
from models import storage_obj
import json
from models.base_model import BaseModel
import sys


classes = ["BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review]
class HBNBCommand(cmd.Cmd):
    """Airbnb's command interpreter"""
    prompt = '(hbnb) '

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
            print(new_instance.id)

    def do_show(self, line_args_obj):
        """
        Prints the string representation of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line_args_obj.split()
        if line_args_obj == "" or line_args_obj is None:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instance = args[0] + "." + args[1]
        if instance in models.storage.all():
            print(models.storage.all()[instance])
        else:
            print("** no instance found **")

    def do_destroy(self, line_args_obj):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = line_args_obj.split()
        if line_args_obj == "" or line_args_obj is None:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = models.storage.all()
            for i in all_objects:
                if i == "{}.{}".format(args[0], args[1]):
                    # del models.storage.all()[args[0] + "." +args[1]]
                    all_objects.pop(i)
                    models.storage.save()
        print("** no instance found **")

    def do_all(self, line_args_obj):
        """
         Prints all string representation of all instances
         based or not on the class name.
         Ex: $ all BaseModel or $ all
        """
        args = line_args_obj.split()
        "COMMENT: impresion de un lista de cadena de los objetos almacenados"
        if len(args) == 0:
            print('["', end="")
            flag = 0
            all_objects = models.storage.all()
            for i in all_objects.keys():
                if flag == 1:
                    print('", "', end="")
                obj = all_objects[i]
                print(obj, end="")
                flag = 1
            print('"]')
        elif args[0] not in classes.keys():
            "COMMENT: si es nombre de la clase no esta"
            print("** class doesn't exist **")
        elif line_args_obj in classes:
            "COMMENT: imprimiremos la representacion en cadena de todos los objetos(incluido los que estan ingresando(comparando el valor inicial del objeto ingresado)) basados o no en el nombre de la clase"
            print('["', end="")
            flag = 0
            all_objects = models.storage.all()
            for i in all_objects.keys():
                if i.startswith(args[0]):
                    if flag == 1:
                        print('", "', end="")
                    obj = all_objects[i]
                    print(obj, end="")
                    flag = 1
            print('"]')

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
        sys.exit(1)

    def do_quit(self, args):
        "Quit command to exit the program"
        return True

    def help_quit(self):
        print("syntax: quit")
        print("--Terminates the application")

    def help_EOF(self):
        print("syntax: EOF")
        print("--Terminates the application")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
