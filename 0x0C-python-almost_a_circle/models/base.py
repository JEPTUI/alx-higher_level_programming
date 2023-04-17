#!/usr/bin/python3
"""
Defines a module that contains a class Base
"""


import json
import csv
import turtle

class Base:
    """
    Defines a class Base that represents base for all the other classes
    private class attribute:
        __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the new Base
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_instances = Base.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_instances]
        except IOError:
            pass
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in CSV
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        deserialize in csv
        """
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                            }
                if cls.__name__ == "Square":
                    dic = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }
                o = cls.create(**dic)
                objs.append(o)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares
        """
        tutle = turtle.Turtle()
        tutle.screen.bgcolor("#b7312c")
        tutle.pensize(3)
        tutle.shape("turtle")

        tutle.color("#ffffff")
        for rec in list_rectangles:
            tutle.showturtle()
            tutle.up()
            tutle.goto(rec.x, rec.y)
            tutle.down()
            for i in range(2):
                tutle.forward(rec.width)
                tutle.left(90)
                tutle.forward(rec.height)
                tutle.left(90)
            tutle.hideturtle()

        tutle.color("#b5e3d8")
        for sq in list_squares:
            tutle.showturtle()
            tutle.up()
            tutle.goto(sq.x, sq.y)
            tutle.down()
            for i in range(2):
                tutle.forward(sq.width)
                tutle.left(90)
                tutle.forward(sq.height)
                tutle.left(90)
            tutle.hideturtle()

        turtle.exitonclick()
