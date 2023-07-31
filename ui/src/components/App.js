
import React, { Component, useState} from "react";

// import * as React from 'react';
import {Typography , Card , CardContent,Box, Button, CardActions, Grid, Paper} from '@material-ui/core/'
// import Body from './body'
import { styled } from '@material-ui/styles';
const axios = require('axios');


const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

const BB = () =>  { 
  return (<Card sx={{ minWidth: 275 }}>
  <CardContent>
    {/* <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom> */}
      Word of the Day
    {/* </Typography> */}
    {/* <Typography variant="h5" component="div">
      be{bull}nev{bull}o{bull}lent
    </Typography> */}
    {/* <Typography sx={{ mb: 1.5 }} color="text.secondary"> */}
      adjective
    {/* </Typography> */}
    <Typography variant="body2">
      well meaning and kindly.
      <br />
      {'"a benevolent smile"'}
    </Typography>
  </CardContent>
  <CardActions>
    <Button size="small">Learn More</Button>
  </CardActions>
  </Card>
  );
}


const App = () => {

  const [state,setState] = useState({'results':[{'results':"Nothing"}]})


  const onGet = () => {
      console.log('Making request')

      axios
      .get(" http://127.0.0.1:8000/blog/post/")

      .then((res) => {
        console.log('SUCCES SUCCES SUCCES')
        setState(res.data)
      })

      .catch((err) => console.log(err+'ERORR ERORR ERORR ERORR '));
  }


            {/* <Body onGet={onGet} data={state}></Body> */}

    return (
      <>
          <h1>
          Hello React !
          </h1>
          <Grid container spacing={3}>
          <BB/>
          <BB/>
          <BB/>
          </Grid>
      </>
    );
};


export default App;



// export default  class App extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {'data':'Nothing'}
//     this.onGet = this.onGet.bind(this)
//   }

//   onGet(){
//     console.log('Making request')

//     axios
//     .get(" http://127.0.0.1:8000/blog/")

//     .then((res) => {
//       console.log('SUCCES SUCCES SUCCES')
//       setState(res.data)
//     })

//     .catch((err) => console.log(err+'ERORR ERORR ERORR ERORR '));
// }

//   render() { 
//     return (
//       <>
//           <h1>
//             {console.log(typeof(this.onGet)+ 'BEFORE TYPE')}
//           Hello React !
//           </h1>

//           <Card aria-owns="" >
//             <Body onGet={this.onGet.bind(this)} data={this.state}></Body>
//           </Card>
//           {/* {console.log(dd.data)} */}
//       </>
//     );
//   }
// }
 
// export default App;



