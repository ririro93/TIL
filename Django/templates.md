# templates

## sending data to js via templates
- not writing `|safe` provokes errors 
  ```js
  let { members, num_solved_prob } = processData({{ results|safe }});
  ```