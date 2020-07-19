# Rubik cube solver
This projects solve a rubik's cube using different graph search strategies:

* Depth First Search
* Breadth First Search 
* Depth Limited Search
* Uniform Cost Search
* Greedy
* A* Search

The project show how efficient are the different search strategies and how those strategies can improve using heuristics.

For simplicity, an entropy measure is used as the heuristic. It favours those cube configurations near a solved cube.

Json format is used to represent a cube.

## Execution instructions
First clone the git repository to your machine and then execute this command in terminal: 

_pip install -r requirements.txt_

To execute the cube solver run in the root directory this command:

_python3 -m src.Search.Search_

To try the performed tests, run in the root directory this command:

_python3 -m pytest_

If matplotlib doesn't show the solution visually, please install tkinter executing this command:

_sudo apt-get install python3-tk_

### Group formed by:
Elena Hervás Martín
Enrique Cepeda Villamayor
Sergio Jimenez Del Coso

Project done for Intelligent systems practices.
