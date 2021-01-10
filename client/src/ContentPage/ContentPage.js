import React from 'react';

import './ContentPage.css';
import Row from 'react-bootstrap/Row';
import Spinner from 'react-bootstrap/Spinner';
import Container from 'react-bootstrap/Container';


import NewsCard from '../components/NewsCard/NewsCard'

import axios from 'axios';
import equal from 'fast-deep-equal'

class ContentPage extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      listNews: null,
      requestError: false,
    }

  }

  componentDidMount() {
    this.getFeedNews();
  }

  componentDidUpdate(prevProps) {
    if (!equal(this.props.tag, prevProps.tag)) {
      this.getFeedNews();
    }
  }

  getFeedNews() {
    let url = process.env.REACT_APP_API_URL + "news/"

    if (this.props.tag && this.props.tag != 'all') {
      url = url + '?tag=' + this.props.tag
    }

    axios.get(url)
      .then(res => {
        this.prepareDateToFeedNews(res.data.data)

      })
      .catch((err) => this.setState({ requestError: true }))
  }

  prepareDateToFeedNews(data) {

    let feedNews = {
      principal: null,
      middle: [],
      footer: []
    }

    if (data.length > 0) {
      feedNews.principal = data[0]
      feedNews.middle = data.splice(1, 2)
      feedNews.footer = data.splice(3, data.length)
    }

    this.setState({ listNews: feedNews })
  }

  render() {

    // LOADING RENDER
    if (!this.state.listNews && !this.state.error) {
      return (
        <Container className="ContentPage ">
          <div className="d-flex justify-content-center">
            <Spinner className="ContentPageSpinner" animation="border"></Spinner>
          </div>
        </Container>);
    }

    // ERROR ON REQUEST
    if (this.state.error) {
      return (
        <Container className="ContentPage">
          Erro ao fazer a requisição dos dados
        </Container>);
    }

    // ANY NEWS FIND
    if (this.state.listNews.principal == null) {
      return (
        <Container className="ContentPage ">
          <div className="d-flex justify-content-center">
            <p className="ContentPageSpinner">Nenhuma notícia encontrada :(</p>
          </div>
        </Container>);
    }

    // TAG TITLE
    let tag_title = ''
    if (this.props.tag && this.props.tag != 'all') {
      tag_title = <div><h2 className={'ContentPageSpinner ' + this.props.tag.toLowerCase()}>{this.props.tag.toUpperCase()}</h2> <hr /></div>

    }

    return (
      <Container className="ContentPage">

        {tag_title}

        <Row>

          {/* PRINCIPAL NEWS */}
          <NewsCard
            kind="principal"
            tag={this.state.listNews.principal.tag}
            title={this.state.listNews.principal.title}
            text={this.state.listNews.principal.text}
            photo={this.state.listNews.principal.photo}
            author_name={this.state.listNews.principal.author_name}
            author_photo={this.state.listNews.principal.author_photo}
          />

          {/* MIDDLE NEWS */}
          {this.state.listNews.middle.map((news) => (
            <NewsCard
              kind="middle"
              tag={news.tag}
              title={news.title}
              text={news.text}
              photo={news.photo}
              author_name={news.author_name}
              author_photo={news.author_photo}
            />

          ))}

        </Row>

        <hr className="ContentPageHR" />

        <Row>

          {/* FOOTER NEWS */}
          {this.state.listNews.footer.map((news) => (
            <NewsCard
              kind="footer"
              tag={news.tag}
              title={news.title}
              text={news.text}
              photo={news.photo}
              author_name={news.author_name}
              author_photo={news.author_photo}
            />
          ))}

        </Row>
      </Container >
    );
  }
}

export default ContentPage;
