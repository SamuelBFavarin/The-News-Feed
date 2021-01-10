import React from 'react';

import './NewsCard.css';

import defaultNewsPhoto from '../../assets/images/photo_news_default.jpg'

import AuthorCard from '../AuthorCard/AuthorCard'

import Col from 'react-bootstrap/Col';
import { Link } from "react-router-dom";


class NewsCard extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            sm_size: 12,
            lg_size: 6,
            author_photo_size: 50,
            photo_class: ""
        }
    }

    componentDidMount() {
        if (this.props.kind == 'principal') {
            this.setState({ sm_size: 12 })
            this.setState({ lg_size: 6 })
            this.setState({ author_photo_size: 50 })
            this.setState({ photo_class: "PrincipalNewsPhoto" })
        }

        else if (this.props.kind == 'middle') {
            this.setState({ sm_size: 6 })
            this.setState({ lg_size: 3 })
            this.setState({ author_photo_size: 35 })
            this.setState({ photo_class: "MiddleNewsPhoto" })
        }

        else if (this.props.kind == 'footer') {
            this.setState({ sm_size: 6 })
            this.setState({ lg_size: 4 })
            this.setState({ author_photo_size: 35 })
        }
    }

    saveNewsInfoOnLocalStorage(news) {
        localStorage.setItem('news', JSON.stringify(news));
    }

    render() {

        let news_title = ""
        let news_text = ""
        let news_photo = ""

        // SETUP NEWS WHEN IS PRINCIPAL
        if (this.props.kind == 'principal') {
            news_title = <h3 className="NewsTitle">{this.props.title}</h3>
            news_photo =
                <div className="d-flex align-items-center" >
                    <img
                        src={this.props.photo != null ? this.props.photo : defaultNewsPhoto}
                        width="100%"
                        className={"d-inline-block align-top NewsPhoto " + this.state.photo_class}
                    />
                    <Link
                        onClick={() => (this.saveNewsInfoOnLocalStorage(this.props))}
                        to="/news"
                        className="NewsButton align-center"
                    >
                        Read More</Link>
                </div>
        }

        // SETUP NEWS WHEN IS MIDDLE
        else if (this.props.kind == 'middle') {
            news_title = <h6 className="NewsTitle">{this.props.title}</h6>
            news_text = <p className="NewsText"> {this.props.text} </p>
            news_photo =
                <div className="d-flex align-items-center" >
                    <img
                        src={this.props.photo != null ? this.props.photo : defaultNewsPhoto}
                        width="100%"
                        className={"d-inline-block align-top NewsPhoto " + this.state.photo_class}
                    />
                    <Link
                        onClick={() => (this.saveNewsInfoOnLocalStorage(this.props))}
                        to="/news"
                        className="NewsButton align-center"
                    >
                        Read More</Link>
                </div>
        }

        // SETUP NEWS WHEN IS FOOTER
        else if (this.props.kind == "footer") {
            news_text = <p className="NewsText"> {this.props.text} </p>
            news_title =
                <Link
                    onClick={() => (this.saveNewsInfoOnLocalStorage(this.props))}
                    to="/news"
                >
                    <h6 className="NewsTitle">{this.props.title}</h6>
                </Link>
        }

        return (

            <Col sm={this.state.sm_size} lg={this.state.lg_size}>
                <p className={"Tag " + this.props.tag.toLowerCase()}>{this.props.tag}</p>

                {news_photo}

                {news_title}

                <AuthorCard
                    name={this.props.author_name}
                    photo={this.props.author_photo}
                    size={this.props.author_photo_size}
                />

                {news_text}
            </Col>
        )
    }
}

export default NewsCard;