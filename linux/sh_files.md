# .sh files
>[stackoverflow](https://stackoverflow.com/questions/13805295/whats-a-sh-file)

얘네는 shell script 파일인데. 리눅스에서 뭔가 명령어를 실행시킬 때 쓰는 애다.

재미있는 점은 윈도우 처럼 확장자로 얘의 역할이 정해지는게 아니라 그냥 텍스트 파일을 실행 시키는거랑 똑같은건데 .sh 는 사용자가 알아보기 편하게 적는거란다.

보통은 그냥 file.sh 이면 bash에서 file만 치면 실행 시킬 수 있는데 os에 따라 권한을 바꿔줘야될 수도 있다 그러면 `chmod +x file.sh`를 실행하면 권한을 everybody로 바꾼다

Shell scripts are interpreted, not compiled. The shell reads commands from the script line per line and searches for those commands on the system (see Section 1.2), while a compiler converts a program into machine readable form, an executable file - which may then be used in a shell script.


<br>

## shebang
첫줄에 `#!` 로 시작하는게 magic line, shebang 등으로 불리는데 이걸로 사람이 읽을 수 있는 파일이라는걸 알 수 있고(그냥 binary는 저걸로 시작하지 않는듯) `#!/bin/ksh` 이라고 써있으면 ksh라는 interpreter을 사용하겠다는 뜻이래.

`#!/bin/bash` : 이걸로 시작하는 경우가 많다, bash로 실행시키라는 뜻이라서
`#!/usr/local/bin/python` : 이런식으로 파일을 파이썬으로 실행시켜라라고도 가능


