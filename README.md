# AirBnB Clone: The Consloe

## Project Overview
This project involves the development of an AirBnb clone, with a primary focus on creating a powerful Storage Engine. The goal is to build a robust foundation for the AirBnb clone by implementing a comprehensive and efficient storage solution.

## Command Interpreter Overview

### How to Start the Command Interpreter
To initiate the command interpreter, follow these steps:
1. Open your terminal.
2. Run the following command:
    ```bash
    ./console.py
    ```

### How to Use the Command Interpreter
The command interpreter supports various functionalities for managing instances within the system. Here are the main operations:

- **Creating Instances:**
  To create an instance, use the following syntax:
  ```bash
  create (Class_Name)
  ```
  Example:
  ```bash
  create BaseModel
  ```

- **Destroying Instances:**
  Delete an instance by specifying the class name and the instance ID:
  ```bash
  destroy (Class_Name) (Instance_ID)
  ```
  Example:
  ```bash
  destroy BaseModel 1234
  ```

- **Updating Instances:**
  Update instance attributes by providing the class name, instance ID, and key-value pairs of attributes to be modified:
  ```bash
  update (Class_Name) (Instance_ID) (Attribute_Name) "(Attribute_Value)"
  ```
  Example:
  ```bash
  update BaseModel 1234 name "New Name"
  ```

- **Displaying Instances:**
  - Show a specific instance:
    ```bash
    show (Class_Name) (Instance_ID)
    ```
    Example:
    ```bash
    show BaseModel 1234
    ```

  - Show all instances of a specific class:
    ```bash
    all (Class_Name)
    ```
    Example:
    ```bash
    all BaseModel
    ```

## Examples
Here are some examples to illustrate the usage of the command interpreter:

- Creating an instance:
  ```bash
  create BaseModel
  ```

- Updating an instance:
  ```bash
  update BaseModel 1234 name "New Name"
  ```

- Showing a specific instance:
  ```bash
  show BaseModel 1234
  ```

- Showing all instances of a class:
  ```bash
  all BaseModel
  ```

These examples showcase the versatility of the command interpreter in managing instances within the system. Feel free to explore and leverage these commands for efficient instance management.