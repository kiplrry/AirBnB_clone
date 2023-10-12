#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    models = {"BaseModel": BaseModel}

    def do_EOF(self):
        """End of File"""
        return True
    
    def do_quit(self):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            newmod = HBNBCommand.models[line]()
            newmod.save()
            print(newmod.id)
    
    def do_show(self, line):
        """Prints the string representation
        of an instance based on the class name and id"""
        args = self.lineparser(line)
        dic = self.instancedict(args)
        if not dic: return
        newMod = HBNBCommand.models[args[0]](**dic)
        print(newMod)
        del newMod

    def do_destroy(self, line):
        """ Deletes an instance based on
        the class name and id (save the 
        change into the JSON file)"""
        args = self.lineparser(line)
        dictionary = self.instancedict(args)
        if not dictionary: return
        key = f"{args[0]}.{args[1]}"
        del storage.all()[key]
        storage.save()
    
    def do_all(self, line):
        """
        Prints all string representation of 
        all instances based or not on the class name. 
        Ex: $ all BaseModel or $ all
        """
        print(type(line))
        all_list = []
        if not line:
            print("for all")
            storage.reload()
            objects = storage.all()
            for key, dic in objects.items():
                classname = key.split(".")[0]
                if classname in HBNBCommand.models:
                    newmodel = HBNBCommand.models[classname](**dic)
                    all_list.append(str(newmodel))
                    del newmodel
        elif line not in HBNBCommand.models:
            print("** class doesn't exist **")
            return
        else:
            storage.reload()
            objects = storage.all()
            dictlist = [objects[key] for key in objects\
                        if key.startswith(line)]
            for dic in dictlist:
                newmodel = HBNBCommand.models[line](**dic)
                all_list.append(str(newmodel))
                del newmodel

        print(all_list)


    def do_update(self, line):
        """
        Updates an instance based on the class name and id by 
        adding or updating attribute (save the change into the JSON file). 
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = self.lineparser(line)
        dictionary = self.instancedict(args)
        if not dictionary: return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        key, insId, attr, val = args
        if attr not in ["id", "created_at", "updated_at"]\
            and isinstance(attr, (int, str, float)):
            dictionary[attr] = val
            newmodel = BaseModel(**dictionary)
            newmodel.save()
            del newmodel


    @staticmethod
    def instancedict(args):
        """validates args and returns the dictionary"""
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        dic = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in dic:
            print("** no instance found **")
            return
        else:
            return dic[key]

    @staticmethod
    def lineparser(line):
        """Splits the line args and returns a list of them"""
        if line:
            return line.split(" ")
        return None
'''
    @staticmethod
    def attrvalparser(arg: str):
        """Parses the attr value to appropriate type"""
        pattern = re.compile(r"^(\d+\.\d+|\d+|([\"'].*[\"']))$",\
                             re.MULTILINE)

        match'''

if __name__ == "__main__":
    HBNBCommand().cmdloop()


"""
1. destroy isnt workig. check on **dictionary** well. What it returns
2. all is supposed to return an array of 
strings, not print everything in a forloop. Store in an 
array first

"""