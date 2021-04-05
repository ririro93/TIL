# Webpack vs Babel
> [blog](https://dev.to/getd/wtf-are-babel-and-webpack-explained-in-2-mins-43be)

## Babel
> simply a translator that translates ES6+ JS code into ES5 ones
- also called a transpiler
- used both for front and back end

## Webpack
> a huge giant translator that works with all kinds of languages and assets.
- by assets: CSS, SCSS, images, fonts, etc.
- often uses babel for some of its jobs
- collect all inline css -> bundle into one small file -> aka minify
- -> allows browser to load faster
- modules are not originall supported by browsers -> webpack to rescue