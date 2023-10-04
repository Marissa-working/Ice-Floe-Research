# Ice Floe Research API of all the files
## quardTree.py
### Classes
* **Node(x0, y0, width, children, parent, id)**
    the basic element(the square in the quardTree)
    | parameters| meaning |
    | --------- | ------------------------------------------------------- |
    |     x0    | int *(the x coordinate of the center of the square)*    |
    |     y0    | int *(the y coordinate of the center of the square)*    |
    |   width   | int *(the width of the square)*    |
    | children  | list *(the children list of the node, len(children) always equal to 4)*    |
    |  parent   | list *(the parent list of the node, len(parent) always equal to 1)*   |
    |     id    | int *(unique id helped for debugging, usually use uuid.uuid4())*     |
   
    
    ```
    # Initialization example
    from quardTree import Node
    Node(0, 0, 1000, [], None, uuid.uuid4().hex[:4])
    ```
    
* **QTree()**
    can be divided, weld, plot the size distribution and graph the quardTree
    | methods| meaning |
    | ---------------------------| ------------------------------------------------------- |
    | **__init__(self)**  |  *(initialize the whole ice floe size is 1000 x 10000, root as the initial whole ice floe, leave_list, parent_list, size_distribution)*    |
    | **subdivide(self, node)**  | node picked from leave_list *(divide the given node(must be a leave node) into four parts)* |
    | **weld(self, node)**  | node picked from parent_list *(weld the four children of given node(must be a parent node) into one part)* |
    | **get_leaves(self)**  | *(return the leave list)* |
    | **get_parent(self)**  | *(return the parent list)* |
    | **plot_size_distribution(self):**  | *(plot the size distribution of the all the leave nodes)* |
    | **graph(self):**  | *(graph the quardTree)* |
    
    ```
    # Initialization example
    from quardTree import QTree
    quard = QTree()
    quard.subdivide(quard.root)  # divide the whole ice floe into four parts
    quard.plot_size_distribution()  # plot the size distribution
    quard.weld(quard.root) # weld the four children of whole ice floe into one part
    quard.plot_size_distribution() # plot the size distribution
    ```

## test.ipynb

## simulation.ipynb
- Simulation based on constant fracture and weld rate
  - Constant fracture and weld rate
  - randomly choose fracture weld node
- Simulation based on size dependency of fracture (constant fracture and weld rate)
  - constant fracture and weld rate
  - choose fracture node based on size, random choose weld node
  - fracture weights = [i.width for i in children]
- Simulation based on size dependency of fracture (constant fracture and weld rate)
  - constant fracture and weld rate
  - choose fracture node based on size, random choose weld node
  - fracture weights = [i.size/children's total size for i in children]
- Simulation based on size dependency of fracture and # of ice floes (constant fracture and weld rate)
  - constant fracture and weld rate
  - choose fracture node based on size and number, random choose weld node
  - fracture layer weights = [size * # of size's ice floe/children's total size * # of size's ice floe  for i in children]
  - Then randomly select the node from the layer
- Simulation based on the leaves number and parents' number
  - P(fracture) = 1 - P(weld), P(weld) = # of parents/ # of leaves
  - Random choice of the node to fracture and weld 
- Simulation based on the leaves' number and parent's number, and size
  - P(fracture) = 1 - P(weld), P(weld) = # of parents/ # of leaves
  - choose fracture node based on size, randomly choose weld node <br>
