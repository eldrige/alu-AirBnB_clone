#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def do_help(self, line):
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    def emptyline(self):
        """
        An empty line + ENTER shouldn't execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
