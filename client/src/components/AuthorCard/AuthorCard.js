import React from 'react';

import './AuthorCard.css';

import anonPhoto from '../../assets/images/anon_avatar.png'

class AuthorCard extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {

        return (
            <div className="d-flex align-items-center AuthorCard">
                <img
                    src={this.props.photo != null ? this.props.photo : anonPhoto}
                    width={this.props.size != null ? this.props.size : 50}
                    height={this.props.size != null ? this.props.size : 50}
                    className="AuthorImg d-inline-block align-top"
                />

                <span className="AuthorName">by {this.props.name}</span>
            </div>
        )
    }

}

export default AuthorCard;