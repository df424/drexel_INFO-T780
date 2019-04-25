<h1>Assignment1 Search</h1>

To run this program the following python packages are required:
numpy, argparse.  They can be installed into your python environment with:
pip install numpy
pip install argparse

To run the two problems use:
python assignment1.py puzzle 
python assignemtn1.py means-end

An example of the output is given at the bottom of this page for both problems.

Problem 1:
Considering this as the initial state,

[4 3 6]

[8 2 7]

[5 1  ]

and this as the goal state,

[8 1 2]

[7   3]

[6 5 4]

apply the 3 steps of search for problem  solving (as described in Week 2 slides)  
and indicate the solution path in the  search space.

Let our word consist of a vector of 9 numbers where 0 is reserved for the empty space.

Let our actions consist of moving the empty space (0) in the four principal directions
where a movement that would take the empthy space outside of the game world has no effect.

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
(area1, area2):state={open, closed} where open and closed is
a discrete option and area1 and area2 or two of our defined areas.

Define the concept of holds for each entity such that:
entity1:holds={entity2, None} where entity2 is another entity or None.

Define the action open for each entity and door such that:
open(entity, door) will set the state of the door to opened if and only if
the entity is in one of the locations the door connects and the door is closed.

Define the action close for each entity and door such that:
close(entity, door) will set the state of the door to closed if and only if
the entity is in one of the locations the door connects and the door is open.

Define the action move for each entity and each set of adjacent locations such that:
move(entity, from_loc, to_loc) will set the location state of the entity and any entity that entity holds to the to_location iff there is not a door inbetween the locations, or the door is opened.

Define the action take for each set of entitys such that:
take(taker, target) will set the holds property of taker to target iff the entities
are in the same locations.

Define the action give for each set of entitys such that:
give(giver, reciever) will set the holds property of receiver to the holds property of giver and set the holds property of giver to None iff the reciever does not hold an item, the giver does hold an item and the giver and receiver are in the same location.

PROBLEM 1 OUTPUT:</br>
[[4 3 6]</br>
 [8 2 7]</br>
 [5 1 0]]</br>
ACTION:  (8, 5)</br>
[[4 3 6]</br>
 [8 2 0]</br>
 [5 1 7]]</br>
ACTION:  (5, 2)</br>
[[4 3 0]</br>
 [8 2 6]</br>
 [5 1 7]]</br>
ACTION:  (2, 1)</br>
[[4 0 3]</br>
 [8 2 6]</br>
 [5 1 7]]</br>
ACTION:  (1, 4)</br>
[[4 2 3]</br>
 [8 0 6]</br>
 [5 1 7]]</br>
ACTION:  (4, 5)</br>
[[4 2 3]</br>
 [8 6 0]</br>
 [5 1 7]]</br>
ACTION:  (5, 2)</br>
[[4 2 0]</br>
 [8 6 3]</br>
 [5 1 7]]</br>
ACTION:  (2, 1)</br>
[[4 0 2]</br>
 [8 6 3]</br>
 [5 1 7]]</br>
ACTION:  (1, 0)</br>
[[0 4 2]</br>
 [8 6 3]</br>
 [5 1 7]]</br>
ACTION:  (0, 3)</br>
[[8 4 2]</br>
 [0 6 3]</br>
 [5 1 7]]</br>
ACTION:  (3, 4)</br>
[[8 4 2]</br>
 [6 0 3]</br>
 [5 1 7]]</br>
ACTION:  (4, 1)</br>
[[8 0 2]</br>
 [6 4 3]</br>
 [5 1 7]]</br>
ACTION:  (1, 2)</br>
[[8 2 0]</br>
 [6 4 3]</br>
 [5 1 7]]</br>
ACTION:  (2, 5)</br>
[[8 2 3]</br>
 [6 4 0]</br>
 [5 1 7]]</br>
ACTION:  (5, 4)</br>
[[8 2 3]</br>
 [6 0 4]</br>
 [5 1 7]]</br>
ACTION:  (4, 7)</br>
[[8 2 3]</br>
 [6 1 4]</br>
 [5 0 7]]</br>
ACTION:  (7, 8)</br>
[[8 2 3]</br>
 [6 1 4]</br>
 [5 7 0]]</br>
ACTION:  (8, 5)</br>
[[8 2 3]</br>
 [6 1 0]</br>
 [5 7 4]]</br>
ACTION:  (5, 2)</br>
[[8 2 0]</br>
 [6 1 3]</br>
 [5 7 4]]</br>
ACTION:  (2, 1)</br>
[[8 0 2]</br>
 [6 1 3]</br>
 [5 7 4]]</br>
ACTION:  (1, 4)</br>
[[8 1 2]</br>
 [6 0 3]</br>
 [5 7 4]]</br>
ACTION:  (4, 7)</br>
[[8 1 2]</br>
 [6 7 3]</br>
 [5 0 4]]</br>
ACTION:  (7, 6)</br>
[[8 1 2]</br>
 [6 7 3]</br>
 [0 5 4]]</br>
ACTION:  (6, 3)</br>
[[8 1 2]</br>
 [0 7 3]</br>
 [6 5 4]]</br>
ACTION:  (3, 4)</br>
[[8 1 2]</br>
 [7 0 3]</br>
 [6 5 4]]</br>

PROBLEM 2 OUTPUT </br>
robot changes kitchen door to opened</br>
robot moves from living room to kitchen</br>
robot changes fridge door to opened</br>
robot changes cupboard door to opened</br>
robot moves from kitchen to cupboard</br>
robot takes the glass</br>
robot moves from cupboard to kitchen</br>
robot moves from kitchen to living room</br>
robot gives his object to person</br>
robot moves from living room to kitchen</br>
robot moves from kitchen to fridge</br>
robot takes the soda</br>
robot moves from fridge to kitchen</br>
robot changes fridge door to closed</br>
robot changes cupboard door to closed</br>
robot moves from kitchen to living room</br>
robot changes kitchen door to closed</br>
robot gives his object to glass</br>
