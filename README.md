Simple Key Column Value Store
=============================

A few notes:

Style
-----
Used underscores inside the kcvstore class because they are implementation details

Confusion Points
----------------
The tests assume that the get function is overloaded
and can take 1 or 2 args, I've handled this by default argument values
it crossed my mind that this could be a mistake in the test
or just testing that I know how to use default argument values in python 
to essentially overload the function 

This is the reason why get_key and get with only one argument case are exactly the same

Seeing the parallel in delete with delete and delete_key I assume that the test writer
has maken the mistake of including get with only one argument in the test cases.

Effeciency
----------

Note that the disk persistence is fairly ineffecient as it dumps the entire kv store 
to disk upon every change (set,del) 

Also note that the slice operator searches through a key in O(n) time which may not be desired.
I was thinking the most ideal case to handle the slices would probably be a binary tree under the 
key hash table as opposed to another hash table.  This would speed the lookup time to O(log n).

Choice of data structures
--------------------------
Since the store is primarily supposed to work like a hash table, with keys occuring only once
and reads being much more common than writes.  I used python's dictionary data structure
for both the keys and the columns.  Python's dictionary is internally itself a hash table
so it inherits some of the requested attributes:

    * like a hash table, a key can only occur once
    * within a given key, a column cannot appear more than once, like a hash table
    * when querying the contents of a key, a list of column/value tuples are returned, sorted by column
    * all keys, columns, and values will be strings of variable length
    * errors shouldn't be raised if a nonexistent key/column is accessed,
        empty lists / None values should be returned
