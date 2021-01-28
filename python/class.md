# Class

## instance var vs class var
```python
class Animal():
    looks = 'cute'
    def speak(self):
        print(looks)
```
- 만약 instance var을 선언을 안 했으면 `dog.looks`출력하면 `Animal.looks = cute`가 그대로 나온다 하지만 `dog.looks = adorable` 를 하면 새로 입력한 값이 나오는 거다. BUT `Animal.looks`에는 영향이 없고 그대로 `cute`가 나온다는 것.
- 조심해야되는게 instance method 안에서 그냥 `looks`를 불러와도 NameError가 뜬다는 점.  -> method 안에서는 class var은 쓸 수 없다. -> 저게 `self.looks` 였으면 사용 가능!
- 파이썬 변수의 scope LEGB랑 비슷한 느낌 

<br>

## instance method vs class method vs static method
- 보통 어떤 걸 사용해도 사용은 가능하다
- 하지만 암묵적으로 사용하는 용도가 다른 것
- **instance method** : self를 통해 instance var 사용\
ex). 
    ```python
    class Animal:
        population = 0
        
        def speak(self):
            print(f"hi i'm {self.name}")
    ```
    - 여기서 `Animal.speak`는 불가 -> `self`에 넘겨줄 instance 인자가 없다

- **class method** : cls를 통해 class var을 사용\
ex).
    ```python
    ...
    @classmethod
    def get_population(cls):
        print(cls.population)
    ```
    - 비슷하게 여기서 `dog.get_population()`은 불가 -> `cls`에 넘겨줄 class 인자가 없음

- **static method** : 둘다 사용 X
ex).
    ```python
    ...
    @staticmethod
    def bark():
        print('woof woof')
    ```
    - 얘는 `Animal.bark()`, `dog.bark()` 둘다 가능

<br>

## self, cls
파이썬에서 self란 어떤 instance가 instance method를 사용할 때 자동으로 자기자신(instance)를 인자로 넣어주는 것을 나타내는 별명같은 것이다

```python
class Animal:
    population = 0
    
    def speak(self):
        print(f"hi i'm {self.name}")

human = Animal()
human.speak()
```
이런식으로 `speak()`method를 사용하면 내가 인자를 안 넣어줘도 파이썬이 내부적으로 instance 자기 자신을 넣어준다. 그래도 `self.name`은 `human`이라는 `Animal` 이라는 class의 instance의 `name`을 보는 것이다. \
-> 그냥 진짜 `self` 자리에 `human`이 들어간다고 생각하면 쉽다.

cls 도 비슷하게 그냥 그거 들어갈 자리에 `Animal`이라는 class를 대신 넣어보면 이해하기 쉽다.

<br>

## 상속
- .mro()를 쳐보면 상속 관계를 볼 수 있다
- classmethod 에서 cls 사용 예시

```python
class Animal:
    num = 0

    def __init__(self):
        Animal.num += 1
    
    @classmethod
    def get_num(cls):
    print(cls.num)

class Dog(Animal):
    num = 0

    def __init__(self):
        super().__init__()
        Dog.num += 1

beaver = Animal()
coco = Dog()
Animal.get_num() # 2
Dog.get_num()    # 1
```
-> 여기서 만약에 `print(Animal.num)` 이었으면 결과가 2, 2로 둘다 `Animal` class의 `num`이 출력됐을 것이다.

<br>

## super()
이건 그냥 상위 class를 저 위치에 넣는다고 생각하면 된다.
`super()` 위치에 `Animal`을 넣어도 웬만하면 비슷하게 작동할 것이다.\
 
 차이점은
 -  상속 관계가 복잡할 때\
 A\
 B C\
 D\
 이런식으로 B, C가 A를 상속하고, D가 B, C를 상속할 때

  ```python
  class A (object):
    def __init__ (self):
        super().__init__()
        print('A')

class B (A):
    def __init__ (self):
        super().__init__()
        print('B')

class C (A):
    def __init__ (self):
        super().__init__()
        print('C')

class D (C, B):
    def __init__ (self):
        super().__init__()
        print('D')
```
이러면 결과가 A B C D가 출력되지만 `super()`을 쓰지 않으면
```python
class A2 (object):
    def __init__ (self):
        print('A2')

class B2 (A2):
    def __init__ (self):
        A2.__init__(self)
        print('B2')

class C2 (A2):
    def __init__ (self):
        A2.__init__(self)
        print('C2')

class D2 (C2, B2):
    def __init__ (self):
        B2.__init__(self)
        C2.__init__(self)
        print('D2')
```
A2 B2 A2 C2 D2 이런식으로 A가 중복 출력된다! 물론 `A2.__init__`을 B 랑 C에서 두번 실행시켰으니 당연히 그렇다.

-> `super()`은 이런걸 알아서 잘 정리해준다\
[참고: stackoverflow](https://stackoverflow.com/questions/21639788/difference-between-super-and-calling-superclass-directly)


