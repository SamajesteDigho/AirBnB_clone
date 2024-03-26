#!/usr/bin/python3
"""
    The console file
    This is the entry point of the program. it uses the cmd module
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


func_line_regex = r"[A-Z][a-zA-Z]*\.[a-zA-Z]+\(.*\)"
parameter_1 = r'"[a-zA-Z0-9\-]+"'
param_1_regex = r"\({}\)".format(parameter_1)
param_2_regex = r'\(({}(\, ?)?)*\)'.format(parameter_1)


class HBNBCommand(cmd.Cmd):
    """The class controlling the console action"""
    intro = ""
    prompt = "(hbnb) "
    file = None

    def do_quit(self, line):
        """Define the quiting mechanism"""
        return True

    def do_EOF(self, line):
        """Defining the end of file mechanism"""
        return True

    def emptyline(self):
        """Executing the empty line"""

    def do_help(self, line):
        """The help mechanism parser"""
        if len(line) == 0:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit")
        else:
            if line == "quit":
                print("Quit command to exit the program")
            else:
                print("help {}".format(line))
        print()

    def do_create(self, line):
        """Create new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "Place", "State", "City",
                          "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                new = BaseModel()
            elif line == "User":
                new = User()
            elif line == "Place":
                new = Place()
            elif line == "State":
                new = State()
            elif line == "City":
                new = City()
            elif line == "Amenity":
                new = Amenity()
            elif line == "Review":
                new = Review()
            storage.new(obj=new)
            storage.save()
            print("{}".format(new.id))

    def do_show(self, line):
        """Show instance based on model name and id"""
        params = line.split(" ")
        if len(params[0]) == 0:
            print("** class name missing **")
        elif params[0] not in ["BaseModel", "User", "Place", "State", "City",
                               "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(params) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(params[0], params[1])
            objects = storage.all()
            if key not in objects.keys():
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, line):
        """Destroy an instance of an object"""
        params = line.split(" ")
        if len(params[0]) == 0:
            print("** class name missing **")
        elif params[0] not in ["BaseModel", "User", "Place", "State", "City",
                               "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(params) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(params[0], params[1])
            objects = storage.all()
            if key not in objects.keys():
                print("** no instance found **")
            else:
                storage.delete(key=key)
                storage.save()

    def do_all(self, line):
        """Print string repre of all instances"""
        if line not in ["", "BaseModel", "User", "Place", "State", "City",
                        "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            result = []
            for x in objects:
                result.append("{}".format(objects[x]))
            print(result)

    def do_update(self, line):
        """Update and instance"""
        params = line.split(" ")
        if len(params[0]) == 0:
            print("** class name missing **")
            return
        if params[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(params) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(params[0], params[1])
        objects = storage.all()
        if key not in objects.keys():
            print("** no instance found **")
            return
        obj_inst = objects[key]
        if len(params) < 3:
            print("** attribute name missing **")
            return
        if len(params) < 4:
            print("** value missing **")
            return
        else:
            from models.base_model import BaseModel
            value = params[3].replace('"', "")
            BaseModel.__setattr__(obj_inst, params[2], value)
            storage.delete(key=key)
            storage.new(obj=obj_inst)
            obj_inst.save()

    def precmd(self, line):
        """Analysing the command and processing it accordingly"""
        if re.match(func_line_regex, line):
            self.process_object_methods(line)
            return ""
        else:
            return super().precmd(line)

    def process_object_methods(self, line):
        """Processing object methods"""
        parts = line.split(".")
        object_name = parts[0]
        if object_name not in ["BaseModel", "User", "Place", "State", "City",
                               "Amenity", "Review"]:
            print("** object {} does not exist **".format(object_name))
            return
        else:
            func = parts[1].split("(")[0]
            if func == "all":
                result = storage.all_class(class_name=object_name)
                string = ""
                for i, x in enumerate(result):
                    string += x.__str__()
                    if i < len(result) - 1:
                        string += ","
                string = "[{}]".format(string)
                print(string)
            elif func == "count":
                counter = storage.count_class(class_name=object_name)
                print(counter)
            elif func == "show":
                pattern = re.findall(param_1_regex, line)
                if len(pattern) == 0 or len(pattern[0]) == 0:
                    print("** instance id not defined **")
                    return
                id = pattern[0][1:-1].replace('"', "")
                result = storage.show_class(class_name=object_name, id=id)
                if result is None:
                    print("** no instance found **")
                else:
                    print(result.__str__())
            elif func == "destroy":
                pattern = re.findall(param_1_regex, line)
                if len(pattern) == 0:
                    print("** instance id not defined **")
                    return
                id = pattern[0][1:-1].replace('"', "")
                result = storage.destroy_class(class_name=object_name, id=id)
                if not result:
                    print("** no instance found **")
            elif func == "update":
                print(param_2_regex)
                pattern = re.search(param_2_regex, line)
                print(pattern.groups)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
