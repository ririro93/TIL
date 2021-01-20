# Scope

## LEGB Rule

- Local (지역 스코프)

- Enclosed (상위 함수)

- Global (전역 스코프)

- Built-in (내장 함수)

  ```python
  print('hi')
  print = 6
  print('hi')
  
  '''
  TypeError                                 Traceback (most recent call last)
  <ipython-input-3-ee28a126169c> in <module>
  ----> 1 print('hi')
        2 print = 6
        3 print('hi')
  
  TypeError: 'int' object is not callable
  '''
  ```

  - 처음 `print`는 LEG를 거쳐서 B에서 처음 찾아서 실행되기 된다
  - 두번째 `print`는 LE를 거쳐서 G에서 `print=6`을 보고 `6('hi')`가 실행된다