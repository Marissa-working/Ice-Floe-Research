# Ice-Floe-Research

```  5/22/23: ```  Uploaded ice_floe.ipynb, which is just practice trying to simulate the fracturing of ice floes based off of wavelength and wave period. <br>
```  5/23/23: ```  I am working on adding the features: get the size of each ice floe(Node) in quadtree and add wield function to quadtree。 <br>
```  5/24/23: ``` Got a model incorporating weld and fractur rates that we can maybe begin appplying to the mesh. <br>
```  5/26/23: ``` Refined the practice model in ice_floe.ipynb and fixed an error with the events. Also added the Probability of each event occuring. <br>
```  5/31/23: ``` Added a dataset that uses actual arctic data to better refine the results. <br>
```  5/31/23: ``` Add a random choice of weld, spilt or do nothing. Also, random choice according to the ice floe size. But low efficiency, needed to be improved. <br>
```  6/13/23: ``` Added "stochastic_model" ipynb which is an alteration of the "ice_floe" ipynb to make it a random stochastic process instead of relying on datasets. This was the model presented in the meeting on 6/9/2023. <br>
```  6/14/23: ``` Trying to add the power law visualizations and also added a function to simulate my model and give averages based on how many times we want to run it. Also added in the option for fractures to either be in 4 or 16 pieces with equal probabilty of either happening when there is a fracture event. <br>
```  6/14/23: ``` Three models added. Four models total<br>
- Simulation based on constant fracture and weld rate
  - Constant fracture and weld rate
  - randomly choose fracture weld node
- Simulation based on size dependency of fracture (constant fracture and weld rate)
  - Constant fracture and weld rate
  - choose fracture node based on size, randomly choose weld node
- Simulation based on the leaves number and parents' number
  - P(fracture) = 1 - P(weld), P(weld) = # of parents/ # of leaves
  - Random choice of the node to fracture and weld 
- Simulation based on the leaves' number and parent's number, and size
  - P(fracture) = 1 - P(weld), P(weld) = # of parents/ # of leaves
  - choose fracture node based on size, randomly choose weld node

