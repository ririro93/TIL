# InstancedMesh
> can be used to create large number of objects with same geometry but different transformations

```javascript
const amount = 3
const count = Math.pow( amount, 3 );

mesh = new THREE.InstancedMesh( geometry, material, count );

const matrix = new THREE.Matrix4();
  let i = 0;
  
  for (let x=0; x<amount; x++) {
    for (let y=0; y<amount; y++) {
      for (let z=0; z<amount; z++) {
        matrix.setPosition( 0-x, 0-y, 0-z );
        mesh.setMatrixAt( i, matrix );
        mesh.setColorAt( i, color );
        i++;
      }
    }
  }
  scene.add( mesh );
```

## Matrix4
> a 4x4 transformation matrix [blog](https://www.brainvoyager.com/bv/doc/UsersGuide/CoordsAndTransforms/SpatialTransformationMatrices.html)

- shows any combination of translations, rotations, scaling and shears

ex). scaling matrix (M X v -> v')

M = <br>
x 0 0 0 <br>
0 y 0 0 <br>
0 0 z 0 <br>
0 0 0 1 <br>
