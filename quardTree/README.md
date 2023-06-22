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
    | **subdivide(self, node)**  | node picked from leave_list*(divide the given node(must be a leave node) into four parts)* |
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
