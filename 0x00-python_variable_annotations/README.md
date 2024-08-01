# Python Project

## General Requirements

- **Allowed editors**: `vi`, `vim`, `emacs`
- **Interpreter**: Python 3.7 on Ubuntu 18.04 LTS
- **File format**: 
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/env python3`
- **Coding style**: Use `pycodestyle` (version 2.5)
- **File permissions**: All files must be executable
- **Documentation**:
  - All modules should have documentation
  - All classes should have documentation
  - All functions (inside and outside a class) should have documentation
  - Documentation should be a real sentence explaining the purpose of the module, class, or method

## Specific Requirements

1. Create a `README.md` file at the root of the project folder.
2. Ensure all code follows the `pycodestyle` style guide (version 2.5).
3. Make all files executable.
4. File length will be tested using `wc`.

## Documentation Guidelines

To check documentation:

- For modules: `python3 -c 'print(__import__("my_module").__doc__)'`
- For classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- For functions outside classes: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- For methods inside classes: `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

Remember, documentation should be meaningful and explain the purpose of the module, class, or method. The length of the documentation will be verified.

## Getting Started

1. Clone this repository to your local machine.
2. Ensure you have Python 3.7 installed on Ubuntu 18.04 LTS.
3. Start coding your project following the above requirements.

## Running the Code

To run any Python file in this project:

```
./your_file_name.py
```

or

```
python3 your_file_name.py
```

## Code Style Checking

To check your code style:

```
pycodestyle your_file_name.py
```

Ensure all files pass the style check before submitting your project.
