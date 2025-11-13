# practice act
from pyscript import display

b = {"erin", "matteo", "ramon", "antonio"} #band
v = {"oscar", "gur", "gino", "ramon", "matteo"} #volleyball


display( b & v, target='output') # these students belong to both clubs
display(b, target='output') # these students belong to only in the first club
display(v, target='output') # these students belong to the second club only
display(b ^ v, target='output') # these students belong to exactly one club

