# AirBnB Clone  Project
This project is ment for developping and putting into practice all we have learned till now in the ALX-SE program.
It is ment to be progressive and will cover a lot of the aspects we have comed through.
Additionnally, it is going to provide us with some technical skills and the required design pattern generally used in enterprise.

## Command Interpreter
The command interpreter, name the *console* is part of the AirBNB project to manage the objects which we will interact
with throughout the project, without bordering about anyother aspect other thn that.

### How to start the console
To start the console, open the terminal in the project directory an try the following command:

~~~cmd
    python3 console.py
~~~

### How to use it
After typing the previous command, a command line opens with the prefix **hbnb** *(can be changed in the future)*, then you interact with it as the usual terminals or command lines (cmd). The acceptable commands are:
- **all** : *all* or *all [model-name]*
- **create** : *create [model-name]*
- **destroy** : *destroy [model-name] [instance-id]*
- **help** : *help* or *help [commande-name]*
- **quit** : *quit*
- **show** : *show [model-name] [instance-id]*
- **update** : *update [model-name] [instance-id] [attribute] [value]*

### Examples
Some examples are:
~~~cmd
:: creating an instance of BaseModel
$ create BaseModel
49faff9a-6318-451f-87b6-910505c55907
$
~~~

~~~cmd
:: Listing all objects created
$ all
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
$
~~~

# Authors
Contirutors to the project are [here](AUTHORS).
