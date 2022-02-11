# AirBnB_clone Project
This goal of this project is to create a clone of the AirBnB web application. The finished application will consist of: 

1. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
2. A website (the front-end) that shows the final product to everybody: static and dynamic
3. A database or files that store data (data = objects)
4. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Command Interpreter
### How to Start It
In order to run the command interpreter (console.py), you must first install the python package locally. 
ou can do this by cloning this repository: 
https://github.com/tsims115/AirBnB_clone.git
Once installed, you can start the program by inputing ./console.py into the commandline. This will start the console and you will be displayed this prompt: 
(hbnb) 

### How to Use It
Once within the interpreter, you can now use it to interact and manipulate data within the python package. If you type 'help' into the CLI, you will be given a list of commands available for use. These commands are:
EOF - Exits the program

all - Prints a string representation of all stored classes. Can be used with an argument to identify a specific class (ie. all BaseModel)

create - Creates a new instance of the indicated class and assigns it a unique id. It must be given an argument. (ie. create BaseModel)

destroy - Destroys and instance based on class name and id. Requires an argument consisting of classname.id (ie. destroy BaseModel.123456)

help - Displays the documented commands

quit - Exits the program

show - Prints string representation of singular instance. Requires an argument consisting of classname.id (ie. show BaseModel.123456)

update - Allows an update to be made to an instance. Requires 3 arguments: classname.id attribute value (ie. BaseModel.123456 name "Tom")
This updates or creates a new key/value pair within the instance.
### Examples
$ ./console
(hbtn) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

$ ./console
(hbtn) create BASEMODEL

e6fca61d-f937-427c-8b33-3f52cc10aba7
$ ./console
(hbtn) all
(Lists all objects. Can specify which model)
