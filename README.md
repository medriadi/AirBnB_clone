# AirBnB Clone Console - ALX Software Engineering Project

## Project Overview

This collaborative project is an integral part of the [ALX Software Engineering program](https://www.alxafrica.com/). The objective is to lay the foundation for our upcoming full-fledged web application, an AirBnB clone. The initial phase involves crafting a custom command-line interface (CLI) for effective data management and establishing the core classes for data storage.

## Usage

The AirBnB clone console operates in both interactive and non-interactive modes, akin to a Unix shell. It awaits user input after displaying the prompt **(hbnb)**.

### Commands and Examples

| Command                                            | Example                                                                                                                                   |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Run the console                                    | `./console.py`                                                                                                                            |
| Quit the console                                   | `(hbnb) quit`                                                                                                                             |
| Display command help                              | `(hbnb) help <command>`                                                                                                                   |
| Create an object (prints its id)                   | `(hbnb) create <class>`                                                                                                                   |
| Show an object                                     | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)`                                                                                 |
| Destroy an object                                  | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)`                                                                           |
| Show all objects, or all instances of a class      | `(hbnb) all` or `(hbnb) all <class>`                                                                                                      |
| Update an attribute of an object                   | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |
| Count the number of instances of an object         | `(hbnb) <class>.count()`                                                                                                                  |
| Update attributes of an object using a dictionary | `(hbnb) <class>.update("<id>", {dictionary representation})`                                                                              |

### Note on Dictionary Representation

When updating attributes using a dictionary representation:

- Enclose the class ID in double quotes for correct parsing.
- For string attribute values, use the format: `'key': "value"`.
- For numeric attribute values, use the format: `"key": value`.

### Non-interactive Mode Example

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```

## Project Models

The [models](./models/) folder encompasses all classes vital to this project.

| File                                    | Description                                          | Attributes                                                                                                                       |
| --------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [base_model.py](./models/base_model.py) | BaseModel class for all the other classes            | id, created_at, updated_at                                                                                                       |
| [user.py](./models/user.py)             | User class for future user information               | email, password, first_name, last_name                                                                                           |
| [amenity.py](./models/amenity.py)       | Amenity class for future amenity information         | name                                                                                                                             |
| [city.py](./models/city.py)             | City class for future location information           | state_id, name                                                                                                                   |
| [state.py](./models/state.py)           | State class for future location information          | name                                                                                                                             |
| [place.py](./models/place.py)           | Place class for future accommodation information     | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| [review.py](./models/review.py)         | Review class for future user/host review information | place_id, user_id, text                                                                                                          |

## File Storage

The [engine](./models/engine/) directory manages serialization and de-serialization in JSON format.

- The [file_storage.py](./models/engine/file_storage.py) defines a FileStorage class with methods: `<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>`

- The [**init**.py](./models/__init__.py) file initializes the FileStorage class as **storage** and automatically reloads serialized data.

## Testing

The code undergoes thorough testing with the **unittest** module:

- Class tests reside in [test_models](./tests/test_models/).
- File storage tests are in [test_engine](./tests/test_models/test_engine).
- Console tests can be found in [tests](./tests/).