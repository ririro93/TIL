# WSGI vs ASGI
> [medium](https://medium.com/analytics-vidhya/difference-between-wsgi-and-asgi-807158ed1d4c)
## WSGI (Web Server Gateway Interface)
- takes a single request and returns response at a time. 
    - can't deal with websockets
## ASGI (Asynchronous Server Gateway Interface)
- successor of WSGI
    - recieve and send are both asynchronous callables
    - allows background coroutine so event listening with external trigger(redis) is possible