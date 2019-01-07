# multiprocessing

## GIL (global interpreter lock)
In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe.



https://wiki.python.org/moin/GlobalInterpreterLock



* multiprocessing is a package that supports spawning processes using an API similar to the threading module. 
* The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. 
* the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.




* threads vs. processes
* GIL (global interpreter lock)

In `multiprocessing`, processes are spawned by creating a `Process` object and then calling its `start()` method. Process follows the API of threading.Thread. A trivial example of a multiprocess program is

The simplest way to spawn a second is to instantiate a Process object with a target function and call start() to let it begin working.
```{python}

```





## resources
https://docs.python.org/3.5/library/multiprocessing.html
https://pymotw.com/3/multiprocessing/basics.html
https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/




