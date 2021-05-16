# events

## to pass in `event` object with own arguments
- explicitly use the `$event` argument
    ```html
    <div @mouseover="handleEvent($event, 4)">mouseover </div>
    ```