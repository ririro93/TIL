# Basics
1. import THREE from cdn
2. create scene, camera, object, renderer
4. render with setAnimationLoop

ex). a cube that changes materials when clicked

```javascript
import * as THREE from 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r126/three.module.min.js';

let camera, scene, renderer;
let geometry, material, mesh, texture;

init();
window.addEventListener("resize", onWindowResize, false); 
window.addEventListener("click", onWindowClick, false); 

function init() {
	// Scene
	scene = new THREE.Scene();

	// Camera
	camera = new THREE.PerspectiveCamera( 
		70,
		window.innerWidth / window.innerHeight,
		0.01,
		10 
	);
	camera.position.z = 1;
	
	// Box
	geometry = new THREE.BoxGeometry( 0.2, 0.2, 0.2 );
	const randTextureNum = Math.floor(Math.random() * Math.floor(5)) + 1;
	console.log(randTextureNum);
	texture = new THREE.TextureLoader().load(`static/textures/${randTextureNum}.jpg`);
	material = new THREE.MeshBasicMaterial({ map: texture });
	// material = new THREE.MeshNormalMaterial();
	mesh = new THREE.Mesh( geometry, material );
	scene.add( mesh );
	
	// Renderer
	renderer = new THREE.WebGLRenderer( { antialias: true } );
	renderer.setSize( window.innerWidth, window.innerHeight );
	renderer.setAnimationLoop( animation );
	document.body.appendChild( renderer.domElement );
	
}

function animation( time ) {
	
	mesh.rotation.x = time / 2000;
	mesh.rotation.y = time / 1000;
	
	renderer.render( scene, camera );
	
}

function onWindowResize() {
	console.log('window resized');
	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();
	renderer.setSize( window.innerWidth, window.innerHeight );
}

function onWindowClick() {
	console.log('window clicked');
	const randTextureNum = Math.floor(Math.random() * Math.floor(4)) + 1;
	texture = new THREE.TextureLoader().load(`static/textures/${randTextureNum}.jpg`);
	material.map = texture;
}
```