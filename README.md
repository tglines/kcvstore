Used underscores inside the kcvstore class because they are implementation details

The tests assume that the get function is overloaded
-> and can take 1 or 2 args, I've handled this by default argument values
-> it crossed my mind that this could be a mistake in the test
-> or just testing that I know how to use default argument values in python 
-> to essentially overload the function 
-> This is the reason why get_key and get with only one argument case are exactly the same
-> Seeing the parallel in delete with delete and delete_key I assume that the test writer
-> has maken the mistake of including get with only one argument in the test cases.

note that the disk persistence is fairly ineffecient as it dumps the entire kv store
-> to disk upon every change (set,del) 
