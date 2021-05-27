### Importance of timing when using Vue
[**Encountered problems**]
- using `store.dispatch` to trigger an action which then requests information from backend that takes time -> causes methods that require such requests to be finished for correct execution to fail. ex). action mutates store.state

[**Solutions**]
1. using `setTimeout()` 
    - easiest to implement but hard to time right
    - could cause problems later on
2. sending request directly not from store
    - chain `.then` to execute after fetch is complete
3. using promises [vue docs](https://vuex.vuejs.org/guide/actions.html#dispatching-actions)
    ```js
    // vuex
    actions: {
    actionA ({ commit }) {
        return new Promise((resolve, reject) => {
        setTimeout(() => {
            commit('someMutation')
            resolve()
        }, 1000)
        })
    },
    actionB ({ dispatch, commit }) {
        return dispatch('actionA').then(() => {
        commit('someOtherMutation')
        })
    }
    }

    //vue
    store.dispatch('actionA').then(() => {
    // ...
    })
    ```

4. using async/await
    ```js
    // assuming `getData()` and `getOtherData()` return Promises

    actions: {
    async actionA ({ commit }) {
        commit('gotData', await getData())
    },
    async actionB ({ dispatch, commit }) {
        await dispatch('actionA') // wait for `actionA` to finish
        commit('gotOtherData', await getOtherData())
    }
    }
    ```