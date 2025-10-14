# python_workspace

This Branch has all the python pracice codes and interview Q&A's

FILE 1:

Q1. What are Python’s key features? Why is it called an interpreted language?

Ans: Python is simple, high-level, dynamically typed, portable, and supports OOP and libraries. It is called interpreted because code runs line by line using the Python interpreter, without compilation.

Q2. Difference between **Python 2 and Python 3**?

Ans: Python 2 is legacy, uses print as a statement, and stores strings as ASCII by default. Python 3 is the present/future, uses print() as a function, and stores strings as Unicode by default.

Q3. Explain **indentation** in Python. What happens if indentation is incorrect?

Ans: Indentation defines code blocks (loops, functions, classes). Incorrect indentation raises an IndentationError or unexpected behavior.

Q4. What are Python **keywords**? Can you use them as variable names?

Ans: Keywords are reserved words like if, for, class, def. They cannot be used as variable names since they have predefined meaning.

Q5. Difference between **list, tuple, set, and dictionary**. Give examples.

Ans:  List → Ordered, mutable [1,2,3]

    Tuple → Ordered, immutable (1,2,3)

    Set → Unordered, unique {1,2,3}

    Dictionary → Key-value pairs {"a":1, "b":2}

Q6. What is the difference between **mutable and immutable** data types?

Ans: Mutable types (list, dict, set) can be changed after creation. Immutable types (int, float, str, tuple) cannot be modified once created.

Q7. Explain **== vs is** operator in Python with examples.

Ans:  == checks values 
        example: [1,2]==[1,2] = True.
    is checks identity (memory location) 
        example: [1,2] is [1,2] → False.

Q8. What is the difference between **append() vs extend()** in lists?

Ans:  append(x) adds the whole element as a single item
        example: [1,2].append([3,4]) = [1,2,[3,4]]
    extend(x) adds elements one by one
        example: [1,2].extend([3,4]) = [1,2,3,4]
Q9. Explain **shallow copy vs deep copy** in Python.

Ans:  Shallow Copy → Creates a new object but only copies references of nested objects (changes in nested objects affect both).

    Deep Copy → Creates a completely independent copy of the object and all nested objects (changes don’t affect each other).

Q10. How does Python handle **memory management** (Garbage collection)?

Ans:  Python uses automatic garbage collection via reference counting and a cyclic garbage collector to free unused objects.



FILE-2:

1. What are Python’s key features?
Python is simple, interpreted, dynamically typed, object-oriented, portable, and has a large standard library.

2. Why is Python called an interpreted language?
Because Python executes code line by line using an interpreter, without requiring prior compilation.

3. What happens if indentation is incorrect in Python?
Python raises an IndentationError, as indentation defines code blocks instead of braces.

4. What are Python keywords? Can you use them as variable names?
Keywords are reserved words (e.g., if, for, class) with predefined meaning. They cannot be used as variable names.

5. What are the differences between Python 2 and Python 3?
Python 2 uses print as a statement and has ASCII default strings, while Python 3 uses print() as a function and Unicode by default.

6. What are mutable and immutable data types in Python?
Mutable types (list, dict, set) can be changed after creation; immutable types (str, tuple, int) cannot.

7. Explain the difference between list, tuple, set, and dict.

list: ordered, mutable, allows duplicates

tuple: ordered, immutable

set: unordered, unique elements

dict: key-value pairs, mutable

8. What are Python’s built-in data types?
Numbers, strings, lists, tuples, sets, dictionaries, booleans, NoneType, and complex numbers.

9. What is the difference between is and == operators?
is checks identity (memory address), while == checks value equality.

10. How are integers and floats stored in memory in Python?
Integers are stored as arbitrary-precision objects; floats follow IEEE 754 double precision.

11. What is the difference between append() and extend() in lists?
append() adds a single element, while extend() adds elements from another iterable.

12. What is the difference between shallow copy and deep copy?
Shallow copy copies references (changes in nested objects reflect), deep copy creates a full independent copy.

13. How do you remove duplicates from a list?
Convert it to a set: list(set(mylist)).

14. How do slicing operations work on lists and strings?
Slicing uses [start:end:step], where start is inclusive and end is exclusive.

15. How do you reverse a string in Python?
Using slicing: s[::-1].

16. What is the difference between break, continue, and pass?
break exits the loop, continue skips the current iteration, pass does nothing (placeholder).

17. What is the purpose of the else clause in loops?
The else block runs if the loop completes normally (without break).

18. How does enumerate() work in Python?
It adds an index to an iterable, returning pairs (index, value).

19. How do you iterate through a dictionary?
Use .items() for key-value pairs:

for k, v in mydict.items(): ...


20. How do you use list comprehension in Python?
It creates a list in one line: [x**2 for x in range(5)].

21. What are default arguments in Python functions?
They provide default values if no argument is passed.

22. What is the difference between *args and **kwargs?
*args collects positional arguments, **kwargs collects keyword arguments as a dictionary.

23. Explain pass-by-value vs pass-by-reference in Python.
Python uses pass-by-object-reference: mutable objects can change inside functions, immutable cannot.

24. Can functions be assigned to variables in Python?
Yes, functions are first-class objects and can be assigned or passed as arguments.

25. What are lambda functions?
Anonymous one-line functions defined using lambda keyword.

26. What are classes and objects in Python?
Classes are blueprints; objects are instances of classes.

27. What are instance methods, class methods, and static methods?

Instance: operates on object (self)

Class: operates on class (cls)

Static: no access to instance/class

28. What are dunder (magic) methods in Python?
Special methods with __, e.g., __init__, __str__, __len__, that customize behavior.

29. What is the purpose of the __init__ method?
It initializes object attributes when an object is created.

30. What is polymorphism in Python?
It allows objects of different types to be accessed through a common interface.

31. What is the difference between an iterable and an iterator?
Iterable is a collection (list, str) that can be looped; iterator is an object returned by iter() with __next__().

32. What is the difference between iter() and next()?
iter() returns an iterator, next() retrieves the next element.

33. What are generators in Python?
Generators are iterators created using yield, producing values lazily.

34. What is the purpose of the yield keyword?
yield returns a value and pauses the function, resuming later.

35. How do dictionary comprehensions work?
They create dicts in one line: {x: x**2 for x in range(5)}.

36. What is the difference between Exception and BaseException?
BaseException is the root of all exceptions; Exception is its subclass for normal errors.

37. Explain try, except, finally, and else.

try: test block

except: handles errors

else: runs if no error

finally: always runs

38. What are custom exceptions? How do you create them?
User-defined errors created by subclassing Exception.

39. Can one except block handle multiple exceptions?
Yes, using a tuple: except (ValueError, TypeError):.

40. What happens if there is no matching except block for an error?
The program crashes and prints a traceback.

41. What are decorators in Python?
Functions that modify another function’s behavior using @decorator.

42. Can a function return another function in Python?
Yes, functions are first-class objects and can return functions.

43. What is a higher-order function?
A function that takes another function as input or returns one.

44. What is a context manager in Python?
It manages resources using with, handling setup and cleanup.

45. What is the difference between with and try-finally?
with automatically handles cleanup, while try-finally requires manual handling.

46. What is the difference between a module and a package?
A module is a single .py file; a package is a collection with __init__.py.

47. What does __name__ == "__main__" mean in Python?
It checks if the file is run directly or imported.

48. What is the difference between import and from-import?
import loads the whole module; from-import imports specific names.

49. How do relative imports work in Python?
They use . or .. to import from the current or parent package.

50. How does Python search for modules when importing?
It checks built-in modules, current directory, and paths in sys.path.

51. What is the LEGB rule in Python?
Lookup order: Local → Enclosing → Global → Built-in.

52. What is the difference between global and local variables?
Local exist inside functions; global exist throughout the program.

53. How do you use the global keyword in Python?
It declares a variable inside a function as global.

54. How do you use the nonlocal keyword?
It refers to variables in the nearest enclosing scope (not global).

55. What happens when two variables with the same name exist in different scopes?
The innermost scope variable is used, shadowing the outer one.

56. How do you read and write files in Python?
Using open(), then read()/write(), and close() or with.

57. What is the difference between text mode and binary mode in file handling?
Text mode handles strings, binary mode handles raw bytes.

58. How do you handle CSV files in Python?
Using the csv module (csv.reader, csv.writer).

59. How do you serialize and deserialize JSON in Python?
Using json.dump()/load() for files, json.dumps()/loads() for strings.

60. How do you handle command-line arguments in Python?
Using sys.argv or argparse for advanced parsing.

FILE-3:

1. How does Python manage memory internally?
Python uses a private heap, memory manager, garbage collector, and interning for small objects.

2. What is the difference between id(), hash(), and is?
id() gives object identity, hash() gives hash value, is checks object identity.

3. How does Python’s garbage collector work?
Uses reference counting and cyclic garbage collector.

4. What are reference cycles, and how does Python handle them?
Objects reference each other; GC detects and breaks cycles.

5. What is the difference between deepcopy and pickle?
deepcopy copies objects fully, pickle serializes and deserializes objects.

6. What is the difference between shallow copy, deep copy, and assignment?
Assignment = same reference, Shallow = copy container only, Deep = full recursive copy.

7. How are Python’s lists implemented internally?
As dynamic arrays with overallocation.

8. How does Python implement dictionaries?
As hash tables with open addressing.

9. What is the difference between OrderedDict and dict in Python 3.7+?
Dicts preserve insertion order; OrderedDict adds extra methods.

10. How do you profile Python code?
Use cProfile, timeit, line_profiler, memory_profiler.

11. What is the Global Interpreter Lock (GIL)? Why does it exist?
A lock allowing only one thread at a time; ensures memory safety in CPython.

12. Difference between multithreading and multiprocessing?
Threads share memory (I/O-bound), processes have separate memory (CPU-bound).

13. When should you use threading vs multiprocessing?
Threading for I/O tasks, multiprocessing for CPU tasks.

14. What is asyncio in Python? How does it differ from threads?
Asyncio uses an event loop and coroutines, lighter than threads.

15. How do coroutines differ from generators?
Generators yield values, coroutines can also consume values.

16. Difference between ThreadPoolExecutor and ProcessPoolExecutor?
ThreadPool = I/O-bound, ProcessPool = CPU-bound.

17. What is the difference between cooperative multitasking and preemptive multitasking?
Cooperative = tasks yield voluntarily, Preemptive = OS interrupts tasks.

18. Write an example of an async function that fetches data from multiple URLs concurrently.
Use asyncio with aiohttp.

19. What are race conditions and deadlocks? How can Python handle them?
Race = unsafe shared access, Deadlock = circular wait; solved with locks and design.

20. How does Python handle inter-process communication?
Using multiprocessing.Queue, Pipe, Manager, sockets, shared memory.

21. What are Python memory views?
Objects that allow zero-copy access to buffers.

22. What is the difference between bytes, bytearray, and memoryview?
Bytes = immutable, Bytearray = mutable, Memoryview = view without copy.

23. How do you reduce memory usage for large datasets?
Use generators, iterators, numpy/pandas, __slots__.

24. What are slots (__slots__) in Python classes, and why are they useful?
Fixed attributes save memory and make access faster.

25. How do you implement an LRU cache manually?
Use OrderedDict.

26. How does Python’s functools.lru_cache work internally?
Uses a dictionary with a doubly linked list for LRU eviction.

27. What are weak references (weakref) in Python?
References that do not increase reference count.

28. How do you debug a memory leak in Python?
Use gc, objgraph, tracemalloc.

29. What are the trade-offs between generators and lists for memory efficiency?
Generators are lazy and memory-efficient, lists store all values in memory.

30. How do you handle huge data efficiently in Python?
Use generators, chunking, numpy memory mapping.

31. What are metaclasses in Python?
Classes of classes that control creation.

32. Difference between type() and class in Python?
class defines, type() inspects or creates classes dynamically.

33. How do you create a Singleton class in Python?
Override __new__ to return the same instance.

34. How do you implement the Factory design pattern in Python?
Use a function or class to return objects based on input.

35. What is monkey patching in Python?
Modifying code at runtime.

36. How do you implement mixins in Python?
Use small classes with reusable methods.

37. What is duck typing? Give an example.
Type determined by behavior, not inheritance.

38. How is multiple inheritance handled in Python (MRO)?
Using C3 linearization (MRO).

39. How do abstract base classes (abc module) work in Python?
Define abstract methods that subclasses must implement.

40. Explain dependency injection in Python with an example.
Pass dependencies instead of hardcoding them.
