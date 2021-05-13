# reactivity
> [stackoverflow](https://stackoverflow.com/questions/49354607/vue-js-data-is-not-updating-with-state-change-so-the-re-render-does-not-happen) <br>
> [reactivity in depth](http://man.hubwiz.com/docset/VueJS.docset/Contents/Resources/Documents/vuejs.org/guide/reactivity.html) <br>
> [list rendering](http://man.hubwiz.com/docset/VueJS.docset/Contents/Resources/Documents/vuejs.org/guide/list.html#Caveats)

- Object: initial value has to be set in data (setting it in `created` doesn't work)
    - ex). make object outside of app block and add to data as initial value
        ```js
        var data = { a: 1 }
        var vm = new Vue({
        data: data
        })
        // `vm.a` and `data.a` are now reactive

        vm.b = 2
        // `vm.b` is NOT reactive

        data.b = 2
        // `data.b` is NOT reactive
        ```
- Array: mutation methods + replacing
    - push(), pop(), sort(), ...
    - filter(), concat(), slice()
    - **simply changing a value is not detected**

## updated lifecycle hook
> Called after a data change causes the virtual DOM to be re-rendered and patched.
- just simple change in data will not activate the `updated` hook

## reactivity in depth
- For every **directive / data binding** in the template, there will be a corresponding watcher object, which records any properties “touched” during its evaluation as dependencies. Later on when a dependency’s setter is called, it triggers the watcher to re-evaluate, and in turn causes its associated directive to perform DOM updates.

## watch
- give option `deep` for objects and lists
```js
watch: {
    todosApp: {
        deep: true,
        handler: function () {
        console.log('diff')
        }
    }
}
```