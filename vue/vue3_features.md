# Vue3 Features

## Composition API
> logic was spread out in Vue2 -> logic related to one feature can be grouped using Composition API

- **composables** can be used by importing (external functions)
- use `ref` or `reactive` to make variables reactive
    - `ref`: have to use the `value` property go get the value of ref object
    - `reactive`: can't handle primitives
- `watch` vs `watchEffect`
    - `watch`: need to be explicit about which variable to `watch` 
    - `watchEffect`: invoked during setup -> good for getting data
        - automatic proc when related variables are changed

## Teleport
```html
<teleport to="<selector>"></teleport>
```
-

## Logger plugin for vuex
```js
import { createLogger } from 'vuex'

const store = createStore({
  plugins: [createLogger()]
})
```