# using mapState, mapGetters in Vue 3

## Make a file with these helper functions
```js
// helpers.js

import { computed } from 'vue'
import { useStore } from 'vuex'

export function useState(arr) {
  const store = useStore()
  const keypair = arr.map(s => [s, computed(() => store.state[s])])
  return Object.fromEntries(keypair)
}

export function useGetters(arr) {
  const store = useStore()
  const keypair = arr.map(g => [g, computed(() => store.getters[g])])
  return Object.fromEntries(keypair)
}

export function useMutations(arr) {
  const store = useStore()
  const keypair = arr.map(m => [m, input => store.commit(m, input)])
  return Object.fromEntries(keypair)
}
```

```js
// <file-name>.vue

import { useState, useGetters, useMutations } from '@/helpers'

export default {
    setup() {
        const { counter } = useState(['counter'])
        const { mult2 } = useGetter(['mult2'])
        const { setCounter } = useMutations(['setCounter'])
        const inc = () => setCounter(counter.value + 1)

        return { counter, mult2, inc }
    }
}
```