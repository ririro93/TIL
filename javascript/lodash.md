# lodash library
> 다양한 기능들이 있는 js 라이브러리

## basics
```js
const _ = require('lodash');
```

## _.isEqual()
> used to compare 2 objects
- 배열 두 개 같은 값 들어있는지 확인할 때 쓰니깐 편하다
```js
a = [1, 2];
b = [1, 2];

a == b // false
_.isEqual(a, b) // true
```

## _.cloneDeep()
> 2차원 배열까지 deep copy 할 수 있는 method
```js
a = [[1, 1], [1, 2]];
b = _.cloneDeep(a);
b[0][0] = 3;

b // [[3, 1], [1, 2]]
a // [[1, 1], [1, 2]]