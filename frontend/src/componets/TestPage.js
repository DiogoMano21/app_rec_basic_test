import React from 'react'
import { connect } from 'react-redux'
import { recommend } from '../redux/actions/recommend';


function TestPage() {
    return (
        <div>
            <button style={{height: "100px"}}>Recommendations</button>
        </div>
    )
}

export default TestPage