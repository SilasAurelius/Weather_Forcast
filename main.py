""""
1. Refactoring a Weather Forecast Application into Classes and Modules
Objective: The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.
"""
from user_interface import UserInterface

def main():
    ui = UserInterface()
    ui.run()

if __name__ == "__main__":
    main()
