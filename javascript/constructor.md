# Constructor Functions
> [modern js](https://javascript.info/constructor-new)

## `new` operator

```js
function User(name) {
  this.name = name;
  this.isAdmin = false;
}

let user = new User("Jack");

alert(user.name); // Jack
alert(user.isAdmin); // false
```

1. a new empty object is created and assigned to `this`
2. usually function body modifiest properties on `this`
3. `this` is returned

<br>

## Return inside constructors
```js
function BigUser() {

  this.name = "John";

  return { name: "Godzilla" };  // <-- returns this object
}

alert( new BigUser().name );  // Godzilla, got that object
```