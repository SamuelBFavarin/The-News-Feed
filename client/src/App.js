import React from 'react';
import MenuNavbar from './MenuNavbar/MenuNavbar'
import ContentPage from './ContentPage/ContentPage'
import NewsPage from './NewsPage/NewsPage'


import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";



class App extends React.Component {

  render() {

    return (
      <div className="App">
        <Router>
          <MenuNavbar />
          <Switch>
            <Route exact path="/">
              <ContentPage tag="all" />
            </Route>
            <Route exact path="/news">
              <NewsPage />
            </Route>
            <Route exact path="/science">
              <ContentPage tag='SCIENCE' />
            </Route>
            <Route exact path="/business">
              <ContentPage tag='BUSINESS' />
            </Route>
            <Route exact path="/tech">
              <ContentPage tag='TECH' />
            </Route>
            <Route exact path="/politics">
              <ContentPage tag="POLITICS" />
            </Route>
            <Route exact path="/sports">
              <ContentPage tag="SPORTS" />
            </Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
