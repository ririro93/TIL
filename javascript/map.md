# Array.prototype.map()
>[MND docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

```js
let newArray = arr.map(callback(currentValue[, index[, array]]) {
  // return element for newArray, after executing something
}[, thisArg]);

// example
let numbers = [1, 2, 3, 4, 5]
let filteredNumbers = numbers.map(function(num, index, my_array) {
  if (index < 3) {
     return num
  } else if (index == 3) {
     return 
  } else {
     return my_array
  }
})
// index goes from 0
// filteredNumbers is [1, 2, 3, undefined, [1, 2, 3, 4, 5]]
// numbers is still [1, 2, 3, 4]
```
- 여기에 들어가는 콜백 함수에는 3개의 인자를 넣어줄 수 있다
    1. currentValue: map을 실행시키는 array의 각 원소들
    2. index: 각 원소들의 index값
    3. array: map 실행시킨 array 그 자체로 통째로