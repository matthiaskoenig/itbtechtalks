# multiprocessing
## Amdahls law
In computer architecture, Amdahl's law (or Amdahl's argument[1]) is a formula which gives the theoretical speedup in latency of the execution of a task at fixed workload that can be expected of a system whose resources are improved.

1/(1-p)

https://en.wikipedia.org/wiki/Amdahl%27s_law#/media/File:AmdahlsLaw.svg



## Threads vs. Processes
**A process is an instance of program** (e.g. Jupyter notebook, Python interpreter). Processes spawn threads (sub-processes) to handle subtasks like reading keystrokes, loading HTML pages, saving files. Threads live inside processes and share the same memory space.

**Process (`multiprocessing`)**
- Created by the operating system to run programs
- Processes can have multiple threads
- Two processes can execute code simultaneously in the same python program
- Processes have more overhead than threads as opening and closing processes takes more time
- Sharing information between processes is slower than sharing between threads as processes do not share memory space. In python they share information by pickling data structures like arrays which requires IO time.

Pros
- Separate memory space
- Code is usually straightforward
- Takes advantage of multiple CPUs & cores
- Avoids GIL limitations for cPython
- Eliminates most needs for synchronization primitives unless if you use shared memory (instead, it's more of a communication model for IPC)
- Child processes are interruptible/killable
- Python multiprocessing module includes useful abstractions with an interface much like `threading.Thread`
- A must with cPython for CPU-bound processing

Cons
- IPC a little more complicated with more overhead (communication model vs. shared memory/objects)
- Larger memory footprint


**Thread (`threading`)**
- Threads are like mini-processes that live inside a process
- They share memory space and efficiently read and write to the same variables
- Two threads cannot execute code simultaneously in the same python program (although there are workarounds*)

Pros
- Lightweight - low memory footprint
- Shared memory - makes access to state from another context easier
- Allows you to easily make responsive UIs
- cPython C extension modules that properly release the GIL will run in parallel
- Great option for I/O-bound applications

Cons
- cPython - subject to the GIL
- Not interruptible/killable
- If not following a command queue/message pump model (using the Queue module), then manual use of synchronization primitives become a necessity (decisions are needed for the granularity of locking)
- Code is usually harder to understand and to get right - the potential for race conditions increases dramatically


The threading module uses threads, the multiprocessing module uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. This is what the global interpreter lock is for.

Spawning processes is a bit slower than spawning threads. Once they are running, there is not much difference.

Threading's job is to enable applications to be responsive.


https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b
https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing


**GIL (global interpreter lock)**
CPython (the standard python implementation) has something called the GIL (Global Interpreter Lock), which prevent two threads from executing simultaneously in the same program.

In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe.

https://wiki.python.org/moin/GlobalInterpreterLock

### When to use threads vs processes?

- Processes speed up Python operations that are CPU intensive because they benefit from multiple cores and avoid the GIL.
- Threads are best for IO tasks or tasks involving external systems because threads can combine their work more efficiently. Processes need to pickle their results to combine them which takes time.
- Threads provide no benefit in python for CPU intensive tasks because of the GIL.




## multiprocessing
* multiprocessing is a package that supports spawning processes using an API similar to the threading module. 
* The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. 
* the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.

In `multiprocessing`, processes are spawned by creating a `Process` object and then calling its `start()` method. Process follows the API of threading.Thread. A trivial example of a multiprocess program is

The simplest way to spawn a second is to instantiate a Process object with a target function and call start() to let it begin working.
```{python}

```





## resources
https://docs.python.org/3.5/library/multiprocessing.html
https://pymotw.com/3/multiprocessing/basics.html
https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/




