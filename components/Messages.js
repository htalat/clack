var React = require('react')
var ReactDOM = require('react-dom')

var Messages = React.createClass({

    render: function()
    {
      if(!this.props.messages){return null;}

      var messageList = this.props.messages.map(function(message,i){
        var text = message.text;
        return(
          <div key ={i} className="message">
            {message.name}
            <span className="message_timestamp"> {message.time.toLocaleTimeString()}</span>
            <span className="message_content" dangerouslySetInnerHTML={{__html:text}}></span>
          </div>
        )
      });

      return(
        <div id="message-list">
          <div className="time-divide">
            <span className="date">
            </span>
          </div>
          {messageList}
        </div>
      )
    }
})

module.exports = Messages;
