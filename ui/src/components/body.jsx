import React, {Component, useState} from "react";
import Card from '@material-ui/core/Card'
import {CardContent,Box} from '@material-ui/core/'
import Button from '@material-ui/core/Button'
import Typography from '@material-ui/core/Typography'
// const axios = require('axios');



export default class Body extends Component {
  constructor(props) {
    super(props);
    this.state = {'links':"Initial STATE"}
    this.onChange = this.onChange.bind(this)
  }

  onChange(){
    // console.log('Hit onGet')
    this.props.onGet()
    this.props.data.results
  }

  render() { 
    const data = this.props.data.results
    const mapped = data.map((o,a,b) => <li key={o.id}>o.title</li>)
    console.log('type of data is ',mapped)
    
    return ( 
      <div>
      <Button onClick={this.onChange} color="secondary" variant="contained">click</Button>
      
      {/* <ul> */}
        
      {/* </ul> */}
      
      </div>
     );
  }
}



{(data.map((o,a,b) => (

  <Card key={o.id}>
    {/* <p>{i.thumbnail} </p> */}
    <CardContent>
    {/* <Typography>{o.title}</Typography> */}
    <BB/>
    {/* <p><img src={o.thumbnail} alt="" width={'150px'} height={'100px'} /></p> */}
    </CardContent>
    
    
    </Card>))
     )}


// export default function Body({props}){

//     const [state,setBody] = useState(props)
//     setBody(props)
//     return (
//       <h5>
//       {state}
//       </h5>
//     )
  
//   }
  
  

  // const c = getPost()

