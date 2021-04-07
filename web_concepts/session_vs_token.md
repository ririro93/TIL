# session vs token authentication
> [blog](https://betterprogramming.pub/json-web-tokens-vs-session-cookies-for-authentication-55a5ddafb435#:~:text=Token-based%20authentication%20using%20JWT,use%20the%20system%20at%20once.)

## Session-based
> server takes care of all the authentication

- when a user logs in, only a session is created and a session id is sent to the user to be stored in cookie.
- this session id is sent to the server on subsequent requests.
- session is deleted on logout
- more load on server because all user data is stored in server

## Token-based
> JWT(JSON Web Token) is most widely used

- server creates token and sends to client to be stored there in local storage
- sent as a header on subsequent requests.
- **stores user state** ex). banana in shopping cart
- bigger than session-id as it contains user info
- server does not know when user logs out because that info is in token