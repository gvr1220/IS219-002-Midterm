# Advanced Python Calculator for Software Engineering Graduate Course

## Description

My calculator app provides a user-friendly interface for performing arithmetic operations on Decimal numbers. It utilizes various design patterns to ensure modularity, extensibility, and maintainability.

- Command Pattern: I use the Command pattern to encapsulate operations as objects, allowing for easy extension and customization. Each command, such as addition, subtraction, etc., is represented as a class, making it simple to add new operations or modify existing ones. [here](https://refactoring.guru/design-patterns/command)

- Factory Method Pattern: The app utilizes the Factory Method pattern to dynamically load plugin modules. This enables the addition of new functionalities without modifying existing code. [here](https://refactoring.guru/design-patterns/factory-method)

- Singleton Pattern: I employ the Singleton pattern for the Calculations class, ensuring that only one instance manages the calculation history throughout the app's lifecycle. This ensures consistency and avoids redundant instantiation. [here](https://refactoring.guru/design-patterns/singleton)

- Strategy Pattern: The Strategy pattern is utilized within the Calculator class to perform arithmetic operations. I achieve flexibility in selecting different algorithms for calculations while keeping the interface consistent. [here](https://refactoring.guru/design-patterns/strategy)

## Environment variables

I make use of environment variables to configure various settings. First, I load environment variables from a .env file using the dotenv library. Then, I set default values for certain variables if they are not provided. For instance, I ensure that the ENVIRONMENT variable is set to "PRODUCTION" by default if it's not defined in the environment.

This approach allows me to customize the behavior of the application based on the environment it's running in. Whether it's development, testing, or production, I can adjust settings accordingly without modifying the code directly. This enhances flexibility and maintainability, making it easier to manage the application's configuration across different environments.

You can check out how I implemented this in my code by taking a look at the load_environment_variables method in my App class in the [__init__.py file](https://github.com/gvr1220/IS219-002-Midterm/blob/main/app/__init__.py).

## Logging:

In my calculator application, I'm using logging to keep track of important events and errors that occur during its operation. Logging helps me understand what's happening inside the application. I've set up logging to record messages at different levels, such as INFO, ERROR, and WARNING. This allows me to log when the application starts, when commands are executed, and when errors occur. For example, when the application initializes, I log a message to indicate that logging has been configured. This helps me ensure that the logging system is set up correctly.

Throughout the application, I log messages to track the execution of commands, such as when a command is registered or when a calculation is performed. This gives me insight into how users interact with the application. Additionally, I log error messages when something unexpected happens, such as when a plugin fails to load or when an unknown command is entered. These error messages help me identify issues efficiently. If you want to see how I've implemented logging, you can check out the configure_logging method in my App class 
[__init__.py file](https://github.com/gvr1220/IS219-002-Midterm/blob/main/app/__init__.py) file.

## try/catch / exceptions


In my code, I use try/catch blocks to handle potential errors that might occur during the execution of certain operations.

For example, in the [execute_command method](https://github.com/gvr1220/IS219-002-Midterm/blob/main/app/commands/__init__.py) of the CommandHandler class, I'm employing the "Easier to Ask for Forgiveness than Permission" approach. Instead of checking beforehand whether a command exists, I simply attempt to execute it within a try block. If the command doesn't exist, a KeyError exception is raised, which I catch and handle appropriately by printing an error message. This approach assumes that executing the command is the common. 

Also, I apply "Look Before You Leap" by checking if certain directories or files exist before attempting to access or manipulate them. For instance, I create a 'logs' directory only if it doesn't already exist using os.makedirs('logs', exist_ok=True). Similarly, I verify if a logging configuration file exists before attempting to load it. [here](https://github.com/gvr1220/IS219-002-Midterm/blob/main/app/__init__.py)

[Link to video](https://drive.google.com/file/d/1ACcXsg1D96BmFDP5-THVxBoLN5201_/view?usp=sharing)

