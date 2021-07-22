import React from 'react'

import { BrowserRouter, Route, Switch} from 'react-router-dom'

import StartPage from './pages/Start.js';
const Routes = () => (
    <BrowserRouter>
        <Switch>
            <Route exact path="/" component={() => <StartPage/> } />
        </Switch>
    </BrowserRouter>
)

export default Routes
