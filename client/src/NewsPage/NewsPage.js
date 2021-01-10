import React from 'react';

import './NewsPage.css';

import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

import anonPhoto from '../assets/images/anon_avatar.png'
import defaultNewsPhoto from '../assets/images/photo_news_default.jpg'

class NewsPage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            news: {
                tag: 'BUSINESS',
                photo: null,
                title: 'Repercussão de evento de Neymar aumenta antipatia internacional sobre o craque. Em que mundo ele vive?',
                text: "We're rounding 'em up in a very humane way, in a very nice way. And they're going to be happy because they want to be legalized. And, by the way, I know it doesn't sound nice. But not everything is nice It's really cold outside, they are calling it a major freeze, weeks ahead of normal. Man, we could use a big fat dose of global warming! I think if this country gets any kinder or gentler, it's literally going to cease to exist.",
                author_name: 'Samuel Daora',
                author_photo: null
            }
        }
    }

    componentDidMount() {
        this.getNewsInfoOnLocalStorage();
    }

    getNewsInfoOnLocalStorage() {
        var news = localStorage.getItem('news');
        this.setState({ news: JSON.parse(news) });
    }

    render() {

        console.log(this.props.myCustomProps)
        return (

            <Container className="NewsPage">
                <Row>
                    <Col>
                        <p className={this.state.news.tag.toLowerCase()}>{this.state.news.tag}</p>
                        <div>
                            <img
                                src={this.state.news.photo != null ? this.state.news.photo : defaultNewsPhoto}
                                width="100%"
                                className="d-inline-block align-top NewsPagePhoto"
                                alt="Feed News"
                            />
                        </div>

                        <h2 class="NewsPageTitle">{this.state.news.title}</h2>

                        <div className="d-flex align-items-center NewsPageAuthorCard">

                            <img
                                src={this.state.news.author_photo != null ? this.state.news.author_photo : anonPhoto}
                                width="50"
                                height="50"
                                className="d-inline-block align-top NewsPageAuthorImg"
                                alt="Feed News"
                            />

                            <span className="NewsPageAuthorName">by {this.state.news.author_name}</span>
                        </div>

                        <hr />

                        <div>
                            <p>{this.state.news.text}</p>
                        </div>
                    </Col>
                </Row>
            </Container>
        )
    }

}

export default NewsPage;

