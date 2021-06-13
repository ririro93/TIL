# Vue Router
> when entering using url or refreshing -> 404 error

## History mode for deployment
- add a catch all route when unmatched urls are requested and redirect to index.html

- ex). netlify: _redirects file 
    ```
    /* /index.html 200
    ```