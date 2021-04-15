# Is axios better than fetch?
> [blog](https://blog.logrocket.com/axios-or-fetch-api/)

## Basic syntax
- axios
    - no need to JSON.stringify data
    ```js
    // axios

    const options = {
        url: 'http://localhost/test.htm',
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=UTF-8'
        },
        data: {
            a: 10,
            b: 20
        }
    };

    axios(options)
    .then(response => {
    console.log(response.status);
    });
    ```
- fetch
    - the url is outside options
    ```js
    // fetch()

    const url = 'http://localhost/test.htm';
    const options = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=UTF-8'
        },
        body: JSON.stringify({
            a: 10,
            b: 20
        })
    };

    fetch(url, options)
    .then(response => {
        console.log(response.status);
    });
    ```

## Response Timeout
- `timeout` property in axios is simpler than `AbortController` in fetch

## http interceptors
- can be used to log messages before http requests are sent
    ```js
    axios.interceptors.request.use(config => {
    // log a message before any HTTP request is sent
    console.log('Request was sent');

    return config;
    });

    // sent a GET request
    axios.get('https://api.github.com/users/sideshowbarker')
    .then(response => {
        console.log(response.data);
    });
    ```

## Download progress
- Axios Progress Bar