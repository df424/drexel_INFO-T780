
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
Let our actions consist of the four principal directions 

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

