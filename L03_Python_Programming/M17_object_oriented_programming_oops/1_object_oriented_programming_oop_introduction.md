Module 17, Lesson 01 introduces **Object-Oriented Programming (OOP)**, a fundamental paradigm for structuring Python programs.

**What is Object-Oriented Programming?**
OOP is recognised as one of the most effective approaches to software development. In Python, which is an object-oriented language, OOP involves writing **classes that act as blueprints for real-world entities or situations**. From these classes, you then create **objects**, also known as **instances**, which are individual realisations of those blueprints.

**Core Concepts of OOP:**

*   **Classes**:
    *   A class defines the **general behaviour and attributes** (data or state) that a whole category of objects will possess.
    *   For example, a `Dog` class might define that all dogs have a `name` and `age`, and can perform actions like `sit()` and `roll_over()`.
    *   Class definitions in Python begin with the `class` keyword.
    *   By convention, Python class names are **capitalised** (e.g., `Dog`, `Car`).
    *   It is standard practice for every class to have a **docstring** immediately following its definition, providing a brief description of its purpose. Modules containing classes should also have docstrings.

*   **Objects (Instances)**:
    *   An object is a specific item created from a class. The process of creating an object is called **instantiation**.
    *   When an object is created, it automatically inherits the general behaviours and attributes defined by its class, and you can also assign it unique characteristics.
    *   Objects store their data in **attributes** (variables associated with the object or its class).
    *   Their functionality is provided through **methods**, which are functions attached to the object or class.
    *   To access an object's attributes or call its methods, you use **dot syntax** (e.g., `my_dog.name`, `my_dog.roll_over()`).
    *   Instance names are typically written in lowercase with underscores (e.g., `my_dog`).

**Key Aspects and Functions in Python OOP:**

*   **`__init__()` Method**: This is a special method automatically invoked when a class is instantiated. It's primarily used to **initialise the object's attributes** with values provided during creation. Methods within a class receive `self` as their first parameter, which refers to the instance itself.
*   **Special Methods (Data Model)**: Python's "data model" defines a set of special methods (e.g., `__repr__`, `__str__`, `__len__`, `__getitem__`). By implementing these, your custom objects can mimic the behaviour of built-in types, facilitating a more "Pythonic" coding style. The Python interpreter frequently calls these methods behind the scenes. For instance, the built-in `len()` function works with your custom objects if you implement the `__len__` special method.
*   **Attributes and Methods**: Beyond `__init__`, you can define other methods to encapsulate an object's actions. You can set default values for attributes and modify them directly or through methods. Python also provides decorators like `@classmethod` for alternative constructors and `@property` for managed attributes.
*   **Inheritance**: A cornerstone of OOP, inheritance allows new classes (child classes) to **derive and extend functionality from existing classes** (parent classes). This promotes efficient code reuse. The `super()` function is vital for properly initialising parent classes in class hierarchies, and Python's Method Resolution Order (MRO) manages the order of initialisation in complex inheritance scenarios.
*   **Encapsulation, Abstraction, and Polymorphism**: Python supports these OOP principles. Encapsulation involves bundling data and the methods that operate on that data into a single unit (the object). Abstraction focuses on showing only essential information while hiding complex details. Polymorphism allows objects of different classes to be treated as objects of a common type, leveraging their shared interface.
*   **Modules**: To maintain clean and organised codebases, classes can be **stored in separate modules** and then imported into other files as needed. This enhances reusability and simplifies program structure.
*   **Duck Typing and Protocols**: Python often adheres to "duck typing" where an object's suitability for a particular purpose is determined by its methods rather than its explicit inheritance. "Protocols" are the informal interfaces (sets of methods) that an object must implement to behave in a certain way. Abstract Base Classes (ABCs), introduced in Python 2.6, offer a more formal way to define and enforce interfaces.

**Benefits of OOP:**

*   **Organisation**: OOP provides an effective way to organise complex programs.
*   **Maintainability**: It makes code easier to troubleshoot and maintain.
*   **Reusability and Modularity**: OOP principles enable the design and implementation of reusable and modular code, improving software architecture.
*   **Logical Thinking**: Understanding OOP helps developers think logically, which is crucial for solving diverse programming problems.
*   **Collaboration**: It establishes a common logic that facilitates collaboration among multiple programmers on a project.

This "Introduction" (Module 17, Lesson 01) serves as the foundation for applying OOP principles to design and implement reusable and modular Python code. It builds upon earlier concepts like variables, lists, and functions, setting the stage for deeper dives into specific OOP elements like Class, Object, Encapsulation, Inheritance, Abstraction, and Polymorphism in subsequent lessons.