# Using this in js
> [blog](https://yehudakatz.com/2011/08/11/understanding-javascript-function-invocation-and-this/)

```js
function hello(thing) {
  console.log(this + " says hello " + thing);
}
```

- calling a function with brackets is in its primitive form `hello.call(<this>, <args>)`
- -> hello("people") = hello.call(undefined, "people") (this is ommited for convenience)

## anonymous function vs arrow function
- using anonymous function calls -> this = window
- -> **must bind** instance outside the function to use the instance as this
- -> ex). `onClick={function(){console.log(this)}.bind(this)}`
- using arrow function calls -> this refers to the instance function is called on (no binding needed)
- -> ex) `.onClick={() => console.log(this)}`

