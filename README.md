# Airport Challenge
-------------------

[![Maintainability](https://api.codeclimate.com/v1/badges/965c505fe16a74a952a4/maintainability)](https://codeclimate.com/github/CKKH/airport-challenge-py/maintainability)

Using Python and Unittest to TDD a a simple program inspired by the [airport
challenge](https://github.com/makersacademy/airport_challenge).

My aim with this project was to test drive the code, and ensure that each class
be tested in isolation.

## Requirements & Running
-------------------------

### Dependancies
----------------

Python3 is recommended to run this program. To check your python3 version run `python3 -V`. You will see the output `Python 3.7.x` if python3 is installed.

If you do not have `python 3.7`, please install it. The guides from DigitalOcean are recommended for this. The following are some examples but you may need to find the guide relavant to your computer's exact operating system:

- [Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-18-04)
- [macOS](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)
- [Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

### Virtual Environment
-----------------------

I recommend using a virtual environment when running this program. Please refer to the DigitalOcean links above for more information on virtual environments and why it is  good idea to use them.

To do this:

1. In your terminal navigate to the location you want your environments to be saved.
2. Create your virtual environment using venv `python3.7 -m venv name_of_your_env`
3. Activate your environment `source path_to_your_env/bin/activate`

### Clone & build dependancies
------------------------------

From your termainal, navigate to a suitable installation location (e.g. a project directory) and input the following commands:

1. Clone the repository `git@github.com:CKKH/airport-challenge-py.git`
2. Change directory `cd airport-challenge-py`
3. Activate your virtual environment if you haven't already `source path_to_your_env/bin/activate`
4. Install dependencies `pip install -r requirements.txt`

### Running project
-------------------

To run the project open `python` in the directory's root. The following are the
basic commands you will need.

1. `from src.airport import Airport` to import the Airport module.
2. `from src.plane import Plane` to import the Plane module.
3. `airport = Airport()` for creating airports.
4. `plane = Plane()` for creating planes.
5. `airport.land(plane)` for landing planes.
6. `airport.take_off(plane)` for taking planes off.
6. `quit()` when you want to exit.

### Tests
---------

To run the test suite, run `python -m unittest tests/*.py` from the directory's
root.

All classes are tested in isolation.

![Imgur](https://i.imgur.com/g77qmXJ.png?1)

### Deactivating virtual environment
------------------------------------

When you are done you can deactivate your virtual environment by entering: `deactivate`.


## Technologies used
--------------------

Tech | Description
------------- | -------------
[Python3](https://www.python.org/) | Main language
[Code Climate](https://codeclimate.com/) | Automated code review for code quality and complexity
[unittest](https://docs.python.org/3/library/unittest.html) | In built python testing module
[Pylint](https://www.pylint.org/) | Source-code, bug and quality checker for Python
[Autopep8](https://github.com/hhatto/autopep8) | A tool that automatically formats Python code to conform to the PEP 8 style guide


## User Stories
---------------

```
As an air traffic controller 
So I can get passengers to a destination 
I want to instruct a plane to land at an airport

As an air traffic controller 
So I can get passengers on the way to their destination 
I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport

As an air traffic controller 
To ensure safety 
I want to prevent landing when the airport is full 

As an air traffic controller 
To ensure safety 
Instructing a plane to land when its grounded will return an error

As an air traffic controller 
To ensure safety 
Instructing a plane to take off when it is flying will return an error

As an air traffic controller 
To ensure safety 
Instructing a plane to land when the weather is stormy will return an error

As an air traffic controller 
To ensure safety 
Instructing a plane to take off when the weather is stormy will return an error

As the system designer
So that the software can be used for many different airports
I would like a default airport capacity that can be overridden as appropriate
```
