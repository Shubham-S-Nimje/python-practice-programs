# Defining set inside set is called nested set. Set is a mutable 
# collection after creating set changes can be done. Set allows only 
# immutable object or items.

# >>> A={10,20,30,40}
# >>> print(A)
# {40, 10, 20, 30}
# >>> B={[10,20]}
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     B={[10,20]}
# TypeError: unhashable type: 'list'
# >>> C={(10,20)}
# >>> print(C)
# {(10, 20)}
# >>> D={{10,20}}
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     D={{10,20}}
# TypeError: unhashable type: 'set'
