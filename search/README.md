
Problem 2:

You live in a studio with your robot that can move and do 
chores for you such as bringing you dates from the 
cupboard and juice from the fridge. Formulate plans with 
operations that have preconditions such as cabinet’s or 
fridge’ door being open and Add and Delete effects. 
Exemplify one plan using both Means‐End analysis and 
the three steps of search for problem solving. 

State Space Formulation

Let our world consist of four discrete areas mainly:
1. The fridge
2. The cupboard
3. The kitchen
4. The living room

Let our discrete areas be joined by the following doors:
1. door1=(living room, kitchen)
2. door2=(kitchen, fridge)
3. door3=(kitchen, cupboard)

Let our world contain the following entities: 
1. A glass
2. A soda
3. A robot
4. A person

Define the concept of location for each entity such that:
entity:location=area where area is one of our defined areas and
entity is one of our defined entities.

Define the concept of open/closed for each door such that:
(area1, area2):location={open, closed} where open and closed is
a discrete option and area1 and area2 or two of our defined areas.

Define the concept of holds for each entity such that:
entity1:holds={entity2, None} where entity2 is another entity or None.

Define the action open for each entity and door such that:
open()
