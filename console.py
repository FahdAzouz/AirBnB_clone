#!/usr/bin/python3
"""
console
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """

    prompt = "(hbnb) "

    def custom_all(self, match):
        """Custom all() commander."""
        print("ALL()", match)

    def precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search("^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        cl_name = match.group(1)
        meth = match.group(2)
        var = match.group(3)
        cmmd = meth + " " + cl_name + " " + var
        self.onecmd(cmmd)
        return ""

    def do_quit(self, line):
        """Quit command"""
        return True

    def do_EOF(self, line):
        """handle end of file"""
        return True

    def emptyline(self):
        """an empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line is None or line == "":
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            var = line.split(' ')
            if var[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(var) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(var[0], var[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        if line != "":
            var = line.split(' ')
            if var[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                l = [str(obj) for key, obj in storage.all().items()
                     if type(obj).__name__ == var[0]]
                print(l)
        else:
            l = [str(obj) for key, obj in storage.all().items()]
            print(l)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            var = line.split(' ')
            if var[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(var) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(var[0], var[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_update(self, line):
        """Updates an instance based on the class\
        name and id by adding or updating attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = '^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
        elif match.group(1) not in storage.classes():
            print("** class doesn't exist **")
        elif match.group(2) is None:
            print("** instance id missing **")
        elif match.group(3) is None:
            print("** attribute name missing **")
        elif match.group(4) is None:
            print("** value missing **")
        else:
            value = match.group(4).replace('"', '')
            key = "{}.{}".format(match.group(1), match.group(2))
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[match.group(1)]
                if match.group(3) in attributes:
                    value = attributes[match.group(3)](value)
                setattr(storage.all()[key], match.group(3), value)
                storage.all()[key].save()

    def do_count(self, line):
         """retrieve the number of instances of a class"""
        var = line.split(' ')
        if not var[0]:
            print("** class name missing **")
        elif var[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [k for k in storage.all() if k.startswith(var[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
