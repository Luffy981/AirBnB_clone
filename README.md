# AirBnB clone - The console

<p align="center">
<img src="https://user-images.githubusercontent.com/68792144/141602345-7b71c4ea-a4dd-42d9-b706-7fc2c7b85ca5.png">
</p>

## Description

This project is the first step towards building our first complete web application: an AirBnB clone. This first part consists of creating a custom python command line interface, for managing data and classes for storage. of the data.

### Representation

<p align="center"><img src="https://user-images.githubusercontent.com/68792144/141602516-90e36740-e66e-4edd-8baf-08f318b10a58.png" width="700"></p>

### Flowchart
<p align="center"><img src="https://user-images.githubusercontent.com/68792144/141603834-c71c3105-49e4-4dcd-b245-e07dacec0a78.jpg" width="700"></p>

## Instalación :key:
[git clone](https://github.com/Luffy981/AirBnB_clone) to install this repository

```
git clone https://github.com/Luffy981/AirBnB_clone
```

## Use :wrench:

The python console must work in interactive and non-interactive mode.
* interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```

* non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## On the console

Commands | Description | Example
--------- | ------- | -------
-- | Run the console | ```./console.py```
quit | Quit the console | ```(hbnb) quit```
help + command | Display the help for a command | ```(hbnb) help <command>```
create + class | Create an object (prints its id)| ```(hbnb) create <class>```
show + class + id | Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
destroy + class + id | Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
all | Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
update + class + id | Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```
class.count() | Count the number of instances of an object | ```(hbnb) <class>.count()```
class.update() | Update attributes of an object using an dictionary | ```(hbnb) <class>.update("<id>", {dictionary representation})```
help EOF | Show EOF command information | ```(hbnb) help EOF```
help quit | Show quit command information | ```(hbnb) help quit```
help all | Show all command information | ```(hbnb) help all```
help destroy | Show destroy command information | ```(hbnb) help destroy```

## Authors

* **Smith Flores** - [github](https://github.com/luffy981) - [linkedin](https://www.linkedin.com/in/smith-flores-chanta-176130214/) - 
* **Diana Carhuamanta** - [github](https://github.com/CarolinaDCode) - [linkedin](https://www.linkedin.com/in/diana-carhuamanta-824742165/)




