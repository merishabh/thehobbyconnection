'use strict';

var $ = require('./bower_components/jquery/dist/jquery.min.js'); 
var React = require('./bower_components/react/react.min.js');
var ReactDOM= require('./bower_components/react/react-dom.min.js');

var Hello = React.createClass({
  render: function() {
    return <div>Hello {this.props.name}</div>;
  }
});

ReactDOM.render(
  <Hello name="World" />,
  document.getElementById('container')
);