# SPA

## SPA 
> single-page-application 의 약자로 reloading 없이 뭔가 interaction이 있으면 필요한 element만 따로 받아와서 기존의 index.html에 요소를 추가하는 느낌

## CSR vs SSR vs SSG
> client-side-rendering, server-side-rendering, static site generation

### CSR
- 장점 : 미리 index.html이랑 app.js를 한번에 받아서 TTV(time-to-view) == TTI(time-to-interact)
- 단점 : 
    - 한번에 데이터를 받아와서 처음에 페이지 로딩이 느리다
    - low SEO(seach-engine-optimization) : html 파일이 비어있어서 잘 못찾음

<br>

### SSR
- 장점 : 서버에서 index.html이랑 js 파일을 합쳐서 보내줌 -> 페이지 로딩이 빠름
- 단점 : 
    - blinking issue -> static 사이트 처럼 다시 만들어서 보내줘야돼서 생김
    - 서버 오버헤드
    - TTV > TTI

<br>

### SSG 
>  정적으로 페이지를 다 준비해두고 줌 거의 CSR + SSR 느낌이래 
ex). React + Gatsby

