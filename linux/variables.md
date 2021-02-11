# variables

## basics
> city=Seoul
1. 타입 선언 x
2. 숫자 넣어도 string으로 저장됨
3. 좌우공백없어야됨
4. 전역변수임
5. 대소문자 구분함
6. 변수명은 숫자, _, 영문자만 가능
7. `$name` 은 `${name}`의 줄임말 -> 첨엔 후자로 연습해보자 더 알아보기 쉬운듯
    - `${#name}` 이런식으로 변수 길이 반환시키거나 `{}` 쓰면 여러 기능이 있다

<br>

## positional parameters
`some_command var1 var2` : 이걸 실행시키면 <br>
some_commnad.sh 파일에 있는 
- `$0` == `some_command` -> command 이름
- `$1` == `var1`
- `$2` == `var2` 이런식
- `$#` == arugument 개수
- `$*` == 변수 전체(`$0` 제외)