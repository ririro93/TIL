# Hooks
> hooks can solve some probs react class components had

## useEffect
> [fetching data](https://www.robinwieruch.de/react-hooks-fetch-data)
> [long guide](https://overreacted.io/a-complete-guide-to-useeffect/)
  - 진짜진짜 좋은 글 
  - **useEffect가 한 render과 관련 있다는 거 기억하자**
    - 그 순간의 state 와 prop 모두 고정 되어있는거
    - component 안에 있는 다른 모든 함수에도 해당되는 내용 
    - -> ex). event handlers, effects, timeouts, API calls, ...

```js
// class component
componentDidMount(
  doA();
  doB();
)

componentDidupdate(
  doA();
  doB();
)
```

- if many features were spread out in these methods it would be hard to debug
- -> useEffect groups related logic

```js
// useEffect
useEffect(
  doA();
)
useEffect(
  doB();
)
```

### Skipping
```js
useEffect(() => {
  document.title = `You clicked ${count} times`;
}, [count]); // Only re-run the effect if count changes
```
> tip: pass in an empty array [] if only the first render should proc useEffect## Hooks
> hooks can solve some probs react class components had

```js
// class component
componentDidMount(
  doA();
  doB();
)

componentDidupdate(
  doA();
  doB();
)
```

- if many features were spread out in these methods it would be hard to debug
- -> useEffect groups related logic

```js
// useEffect
useEffect(
  doA();
)
useEffect(
  doB();
)
```

### Skipping
```js
useEffect(() => {
  document.title = `You clicked ${count} times`;
}, [count]); // Only re-run the effect if count changes
```
> tip: pass in an empty array [] if only the first render should proc useEffect

<br>

## no direct async function in useEffect
```js
useEffect(async () => {
    const result = await axios(
      'https://hn.algolia.com/api/v1/search?query=redux',
    );
 
    setData(result.data);
  }, []);
  ```
  > all async functions return an implicit promise whereas the useEffect hook should not return anything except for a cleanup function

<br>

## useEffect() VS componentDidUpdate()
```js
// useEffect

function Counter() {
const [count, setCount] = useState(0);

useEffect(() => {
  setTimeout(() => {
    console.log(`You clicked ${count} times`);
  }, 3000);
});

return (
  <div>
    <p>You clicked {count} times</p>
    <button onClick={() => setCount(count + 1)}>
      Click me
    </button>
  </div>
);
}
```

```js
// componentDidUpdate

componentDidUpdate() {
  setTimeout(() => {
    console.log(`You clicked ${this.state.count} times`);
  }, 3000);
}
```

- `useEffect` belongs to a particular render
- -> 1, 2, 3, 4, 5
- `this.state.count` points at the latest count rather than of a particular render
- -> 5, 5, 5, 5, 5
- `useRef` can be used to replicate this behavior

<br>

## synchronization, not lifecycle
> React synchronizes the DOM according to our current props and state. There is no distinction between a “mount” or an “update” when rendering.
> You should think of effects in a similar way. useEffect lets you synchronize things outside of the React tree according to our props and state.

<br>

## don't lie to React about dependencies
> [bookmark](https://overreacted.io/a-complete-guide-to-useeffect/#dont-lie-to-react-about-dependencies)
1. add all values inside the effect 
2. use functional updates
3. useReducer

<br>

## functional updates
```js
function Counter({initialCount}) {
  const [count, setCount] = useState(initialCount);
  return (
    <>
      Count: {count}
      <button onClick={() => setCount(initialCount)}>Reset</button>
      <button onClick={() => setCount(prevCount => prevCount - 1)}>-</button>
      <button onClick={() => setCount(prevCount => prevCount + 1)}>+</button>
    </>
  );
}
```

## useReducer
> When setting a state variable depends on the current value of another state variable, you might want to try replacing them both with useReducer.
[bookmark](https://overreacted.io/a-complete-guide-to-useeffect/#decoupling-updates-from-actions)

## fetching data
> [blog](https://www.robinwieruch.de/react-hooks-fetch-data)