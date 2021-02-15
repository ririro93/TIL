# git CLI commands

## HEAD
> 그냥 지금 내가 보고 있는 branch 가르쳐주는거

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
- -a lets you skip `git add` and automatically stages all tracked files before the commit

  ```
  git commit -a -m 'message'
  ```
- --amend
  ```
  $ git commit -m 'Initial commit'
  $ git add forgotten_file
  $ git commit --amend
  ```




### push

- `git push <원격저장소 이름> <올릴 브랜치 이름>`

  - `git push origin master`
- commit history를 원격 저장소에 업로드



### clone

- `git clone` 첨에 한번에 다 가져올 때 쓰는거



### pull

- `git pull <origin> <master>` 업데이트 된 내용도 다 가져와줘

### rm

`git rm --cached`
그냥 `git rm`만 하면 내 local이랑 git 이 tracking 하고 있는 파일이 둘다 없어진다. <br>
그냥 깃으로 관리하고 있는 파일만 없애고 싶은 경우에는 `git rm --cached`를 하면 내 로컬에서는 파일이 유지된다. -> 실수로 .gitignore 적용 안하고 stage 했을 때 쓸 수 있다.

## branches
>[git book](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

- will try to create a new branch for each feature for practice
  ```
  git checkout -b <branchName>
  ```

  this is the same as
  ```
  git branch <branchName>
  git checkout <branchName>
  ```

- deleting a branch after merging with master
  ```
  git branch -d <branchName>
  ```

- checking which branches need to be merged
  ```
  git branch --no-merged
  ```