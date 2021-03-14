# Animating three.js

## using `requestAnimationFrame( animate )` -> 원래 브라우저 기능

```javascript
function animate() {
    requestAnimationFrame( animate );
}
```

## using `setAnimationLoop( animation )` -> Three.js renderer method
> this must be used for WebXR projects

```javascript
renderer.setAnimationLoop( animation );

function animation( time ) {
    renderer.render( scene, camera );
}
```