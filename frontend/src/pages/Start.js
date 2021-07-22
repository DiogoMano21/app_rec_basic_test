import {Redirect} from 'react-router';
import React, {Component} from "react";
import { connect } from 'react-redux'



//import  {Button, Spinner } from 'react-bootstrap'
import { recommend } from '../redux/actions/recommend';
class Start extends Component {
        constructor(props) {
            super(props)
            this.state = {
              app_id : 56965434
            }
        }
        
        onChange = () => {
            console.log("aqui")
          const { dispatch } = this.props
          dispatch(recommend(this.state.app_id))
        }
        render(){  
          const {recommend, loading} = this.props
          if (loading===false){
            console.log(recommend)
          }
          return (
            <div>
                <button onClick={this.onChange} style={{height: "100px"}}>Recommendations</button>
            </div>
      
          );
        }
      }
      
            
        
    export default connect((state) => ({
        recommend: state.recommendReducer.data || [],
            loading: state.recommendReducer.loading 
    }))(Start)
            
    
