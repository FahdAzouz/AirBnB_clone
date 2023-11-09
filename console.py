#!/usr/bin/python3
"""
console
"""
import cmd



class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command"""
        return True

    def do_EOF(self, line):
        """handle end of file"""
        return True

    def emptyline(self):
        """an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
