# in-line event and addEventListener
> [stackoverflow](https://stackoverflow.com/questions/6348494/addeventlistener-vs-onclick)

- they are basically the same but `addEventListener` comes with an option where you can choose to handle the event during the capture phase or the bubbling phase(default) [w3c](https://www.w3.org/TR/DOM-Level-3-Events/#capture-phase)

## keyup
> wait for user to finish typing to fire an event

```js
let timeout = null;
searchInput.addEventListener("keyup", e => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    console.log(e.target.value);
  }, 500);
})
```