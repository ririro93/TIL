# Selectors
```
#id > p:nth-child(2)
```
이런게 있으면 id 의 자식들 중 2번째 자식이 p이면 적용되는거

```
#id > p:nth-of-type(2)
```
id의 p인 자식들 중 2번째

<br>

# Position

## static (default)
position: static;
HTML elements are positioned static by default.

Static positioned elements are not affected by the top, bottom, left, and right properties.

An element with position: static; is not positioned in any special way; it is always positioned according to the normal flow of the page:

## relative
- 나를 기준으로(내가 원래 있어야될 static위치) 이동한거 처럼 보여줌
- 그 자리에 내가 있다(자기 자리 확보 해둠)
- 원래 위치에서 약간 이동하고 싶을 때 사용

## absolute
- static이 아닌(relative, absolute, fixed) 가장 가까운 parent 기준으로 이동
  - body도 static 이지만 얘보다 상위가 없어서 여기도 이동하는 경우가 많음
- 나 자체가 움직임 (내 자리 없어짐)
- 웹툰 리모콘

## fixed
- 무조건 고정값
- 스크롤 내려도 고정

## z-index
- static 아닌 경우에만 적용 가능
- static이면 애초에 자기 공간만 차지해서 겹칠 일이 없기 때문에

<br>

# height vs line-height
- 박스 높이와 그 안에서 글이 차지하는 높이

# lorem
- lorem 치면 dummy 데이터 만들 수 있다
- lorem2 치면 두 단어만 나옴

# keyframes
```
@keyframes move {

}
```
이거 파이썬 함수 선언하는거랑 비슷