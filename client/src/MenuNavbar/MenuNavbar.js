import React from 'react';
import logo from '../assets/images/logo.png';
import menuToggle from '../assets/images/menu.png';

import './MenuNavbar.css';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';

import {
  Link
} from "react-router-dom";

class MenuNavbar extends React.Component {

  constructor(props) {
    super(props);
    this.state = { showToggle: false };
  }

  alterToggleStatus() {
    if (this.state.showToggle) {
      this.setState({ showToggle: false });
    }
    else {
      this.setState({ showToggle: true });
    }
  }

  render() {

    const showToggle = this.state.showToggle;
    let navCollapse;
    let navContent;

    if (!showToggle) {
      navCollapse =
        <Navbar.Collapse className="TopNavBar-navbar-big-screen justify-content-end" >
          <Nav.Link><Link className="TopNavbar-navbar-link" to="/politics">POLITICS</Link></Nav.Link>
          <Nav.Link><Link className="TopNavbar-navbar-link" to="/business">BUSINESS</Link></Nav.Link>
          <Nav.Link><Link className="TopNavbar-navbar-link" to="/tech">TECH</Link></Nav.Link>
          <Nav.Link><Link className="TopNavbar-navbar-link" to="/science">SCIENCE</Link></Nav.Link>
          <Nav.Link><Link className="TopNavbar-navbar-link" to="/sports">SPORTS</Link></Nav.Link>
          <Nav.Link ><Link to="/">LOGIN</Link></Nav.Link>
        </Navbar.Collapse>

      navContent = ''

    } else {
      navCollapse = ''
      navContent =
        <ul className="TopNavbar-navbar-collapse">
          <li className="TopNavbar-navbar-collapse-element"><Link onClick={() => this.setState({ showToggle: false })} to="/politics">POLITICS</Link></li>
          <li className="TopNavbar-navbar-collapse-element"><Link onClick={() => this.setState({ showToggle: false })} to="/business">BUSINESS</Link></li>
          <li className="TopNavbar-navbar-collapse-element"><Link onClick={() => this.setState({ showToggle: false })} to="/tech">TECH</Link></li>
          <li className="TopNavbar-navbar-collapse-element"><Link onClick={() => this.setState({ showToggle: false })} to="/science">SCIENCE</Link></li>
          <li className="TopNavbar-navbar-collapse-element"><Link onClick={() => this.setState({ showToggle: false })} to="/sports">SPORTS</Link></li>
          <li className="TopNavbar-navbar-collapse-element"><Link onClick={() => this.setState({ showToggle: false })} to="/">LOGIN</Link></li>
        </ul>

    }

    return (
      <div className="TopNavbar" >
        <Navbar className="TopNavbar-navbar" bg="light" expand="lg">
          <Container>

            <Navbar.Brand href="/" className="TopNavbar-navbar-brand order-lg-0 mx-auto order-1">
              <img
                src={logo}
                width="50"
                height="50"
                className="d-inline-block align-top"
              />
            </Navbar.Brand>

            <Navbar.Toggle onClick={() => this.alterToggleStatus()} className="TopNavbar-navbar-toggle-icon order-lg-1 order-0" >
              <img src={menuToggle} />
            </Navbar.Toggle>

            {navCollapse}

          </Container>
        </Navbar>

        {navContent}
      </div>
    );
  }
}

export default MenuNavbar;
