#!/usr/bin/python3
"""
    The console file
    This is the entry point of the program. it uses the cmd module
"""
from cmd import Cmd
from models import storage


class HBNBCommand(Cmd):
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

    def emptyline(self, line):
        """Executing the empty line"""

    def do_help(self, line):
        """The help mechanism parser"""
        if len(line) == 0:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit\n")
        else:
            if line == "quit":
                print("Quit command to exit the program\n")

    def do_create(self, line):
        """Create new instance of BaseModel"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
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
            new.save()
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
                result.append(objects[x].__str__())
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
            BaseModel.__setattr__(obj_inst, params[2], params[3])
            storage.delete(key=key)
            storage.new(obj=obj_inst)
            obj_inst.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
