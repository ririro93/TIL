# git CLI commands



## 설정

### init

- `git init`

- 폴더를 git으로 관리하기 위해 .git 폴더 생성하는 명령어

  

### status

- `git status`

- 현재 git의 상태 출력

  

### log

- `git log`

- 현재 쌓여있는 commit history 출력

  

### diff

- `git diff`
- 마지막 commit과 현재 wd의 상태 비교 결과 출력
- `add` 하기 전에 찍어보는 거



### remote add

- `git remote add <별명> <주소> `
- ex). `git remote add origin [<https://github.com/ririro93/first-git.git>]`
- 이게 뭐냐하면 저 주소 별명을 origin 이라고 하겠다는 뜻
- 그래서 나중에`git push origin master` 이라고 하면 내 로컬의 마스터를 origin이라고 지정한 주소에 push 하라는 뜻



## 조작

### add

- `git add <파일이름>`
  - `<파일이름>`에 `.`을 입력하면 현재 wd 전체 추가
- wd 에 있는 파일을 staging area(INDEX)에 올림



### commit

- `git commit -m "<commit message>"`
- staging area 에 있는 파일들을 스냅샷으로 저장



### push

- `git push <원격저장소 이름> <올릴 브랜치 이름>`

  - `git push origin master`
- commit history를 원격 저장소에 업로드



### clone

- `git clone` 첨에 한번에 다 가져올 때 쓰는거



### pull

- `git pull <origin> <master>` 업데이트 된 내용도 다 가져와줘