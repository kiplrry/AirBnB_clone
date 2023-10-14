#!/usr/bin/python3
"""AirBnB Console"""
import re
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBComand class that inherits from Cmd class"""
    prompt = "(hbnb) "
    classes = storage.classes()

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
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            newmod = HBNBCommand.classes[line]()
            newmod.save()
            print(newmod.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class\
        name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        args = self.lineparser(line)
        key = self.validate(args)
        if not key:
            return
        objdict = storage.all()
        print(objdict[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the
        change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = self.lineparser(line)
        key = self.validate(args)
        if not key:
            return
        del storage.all()[key]

    def do_all(self, line):
        """Prints all occurences of an object class"""
        if not line:
            all_list = [str(obj) for obj in storage.all().values()]
            if all_list:
                print(all_list)
            return

        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        wantedlist = [str(obj) for key, obj in storage.all().items()
                      if key.startswith(line)]

        if wantedlist:
            print(wantedlist)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding\
        or updating attribute (save the change into the JSON file).\
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = self.lineparser(line)
        key = self.validate(args)
        if not key:
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if args[2] in ["id", "create_at", "updated_at"]:
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if args[3] is None:
            print("** invalid value **")
            return
        attr = args[2]
        val = args[3]
        objdict = storage.all()[key].to_dict()
        objdict[attr] = val
        inst = HBNBCommand.classes[args[0]](**objdict)
        storage.new(inst)
        storage.save()

    @staticmethod
    def validate(args):
        """validates args and returns the key"""
        if not args:
            print("** class name missing **")
            return None
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return None
        if len(args) < 2:
            print("** instance id missing **")
            return None
        key = f"{args[0]}.{args[1]}"

        if key not in storage.all():
            print("** no instance found **")
            return None

        return key

    @staticmethod
    def lineparser(line, num=-1):
        """Splits the line args and returns a list of them"""
        pattern = re.compile(r"(\d+\.\d+|\d+|\"[^'\"]+?\"|'[^'\"]+?')$")
        if line:
            args = line.split(" ", num)
            if len(args) > 3:
                if re.match(pattern, args[3]):
                    val = args[3].strip("\'\"")
                    if val.isdigit():
                        args[3] = int(val)
                    else:
                        try:
                            args[3] = float(val)
                        except ValueError:
                            args[3] = str(val)
                else:
                    args[3] = None
            return args
        return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
