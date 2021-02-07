# pip

## using pip
`pip install -` 보다 <br>
`python -m pip install -`이 좋은 습관이라고 한다  <br>
왜냐하면 파이썬 버전에 따라 dependencies 충돌할 수도 있으니깐

## pip freeze
`pip freeze > requirements.txt`로 한번에 requirements.txt를 만들고 거기에 모든 dependency 목록을 저장할 수 있다

-> `pip install -r requirements.txt`로 다른데서 한번에 다 받을 수 있다.