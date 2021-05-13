# plugins

## vuex-persistedstate
```js
import Vue from 'vue'
import Vuex from 'vuex'
import createdPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createdPersistedState()
  ],

...
```
- this adds all states from vuex to localStorage