# Parallel Computing (multiprocessing vs multithreading)

## Process
instance of a computer program being executed.
- each process has own memory space
- chrome and firefox use multiprocessing
- easier to implement
- overhead : memory and time

## Thread
components of a process
- can run parallely
- share memory space -> sharing object is easier
- lower overhead
- spawning is faster
- overhead : have to think more about design -> for synchronization

## Pitfalls
- race condition
  - when 2 threads try to change 1 var -> use mutual exclusion(mutex) lock -> only 1 thread can change var at a time
- starvation
  - when 1 thread has no work due to poor design-> slower overall
- deadlock
  - when 1 thread is waiting for deadlock -> other thread needs resource from first thread -> both halt
- livelock
  - keep running in loop

## Python
> GIL(Global Interpreter Lock) <br>
: a mutex that prevents multiple threads from executing python at once.
-> multiple CPU core can't be used

<br>

## Usage
### multithreading
> IO, user interaction
- web-scraping
- web servers
- tensorflow -> transform data in parallel

### multiprocessing
> anything CPU intensive, computation, no IO or user interaction
- pytorch -> load data to GPU

[reference](https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/)