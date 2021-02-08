# chart.js

## add click events to labels
[doc](https://chartjs-plugin-datalabels.netlify.app/guide/events.html#listeners)
```js
data: {
  datasets: [{
    datalabels: {
      listeners: {
        click: function(context) {
          // Receives `click` events only for labels of the first dataset.
          // The clicked label index is available in `context.dataIndex`.
          console.log('label ' + context.dataIndex + ' has been clicked!');
        }
      }
    }
  }, {
      //...
  }]
},
options: {
  plugins: {
    datalabels: {
      listeners: {
        enter: function(context) {
          // Receives `enter` events for any labels of any dataset. Indices of the
          // clicked label are: `context.datasetIndex` and `context.dataIndex`.
          // For example, we can modify keep track of the hovered state and
          // return `true` to update the label and re-render the chart.
          context.hovered = true;
          return true;
        },
        leave: function(context) {
          // Receives `leave` events for any labels of any dataset.
          context.hovered = false;
          return true;
        }
      },
      color: function(context) {
        // Change the label text color based on our new `hovered` context value.
        return context.hovered ? "blue" : "gray";
      }
    }
  }
}
```