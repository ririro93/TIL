# Functions

## function declaration
- functions declarations are processed before the code block is executed
- -> the below situation is possible

```js
welcome();

function welcome() {
    alert("greetings!");
}                         // this is a suntax contruct -> no ; needed 
```

## function expression
- are created when the execution flow reaches them

```js
welcome(); // -> error

let welcome = function() {
    alert("greetings");
};                       // ; is added because this is an expression just like let a = 3;
```

## arrow functions
- returns the evaluated expression according to the passed arguments
```js
let func = (arg1, arg2, arg3) => expression
```

- but! if curly brackets are used, an explicit return is needed
```js
let sum = (a, b) => {
    return a + b
};
```