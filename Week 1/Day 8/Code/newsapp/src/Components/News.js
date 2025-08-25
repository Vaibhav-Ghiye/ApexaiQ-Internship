import React, { use, useEffect, useState } from "react";
import NewItem from "./NewItem";
import Spinner from "./Spinner";
import PropTypes from "prop-types";
import InfiniteScroll from "react-infinite-scroll-component";


const News = (props) => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [totalResults, setTotalResults] = useState(0);

  const capitalizeFirstLetter = (string) => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };

  
  const updateNews = async () => {
    props.setProgress(0);
    const url = `https://newsapi.org/v2/top-headlines?country=${props.country}&category=${props.category}&apiKey=3107f460bfbc4778817c920f47f2e61c&page=1&pageSize=${props.pageSize}`;
    setLoading(true);

    let response = await fetch(url);

    props.setProgress(30);

    let parseData = await response.json();
    console.log(parseData);

    props.setProgress(70);

    setArticles(parseData.articles);
    setTotalResults(parseData.totalResults);
    setLoading(false);
    
    props.setProgress(100);
  }

  useEffect(() => {
    document.title = `${capitalizeFirstLetter( props.category )} - NewsMonkey`;
    updateNews(1);
    
  }, [])
  
  

  const handlePrevCLick = async () => {
   setPage(page - 1);
    updateNews();
  };

  const handleNextCLick = async () => {
    setPage(page + 1);
    updateNews();
  };

  const fetchMoreData = async () => {
    const url = `https://newsapi.org/v2/top-headlines?country=${props.country}&category=${props.category}&apiKey=3107f460bfbc4778817c920f47f2e61c&page=1&pageSize=${props.pageSize}`;

    setPage(page + 1);
    let response = await fetch(url);
    let parseData = await response.json();
    console.log(parseData);
    setArticles(articles.concat(parseData.articles));
    setTotalResults(parseData.totalResults);
  };

    return (
      // below code is of infinite scroll

      <div className="container my-3">
        <h1 className="text-center" style={{ margin: "35px 0", marginTop: '90px' }}>
          NewsMonkey - Top Headlines from{" "}
          {capitalizeFirstLetter(props.category)} category{" "}
        </h1>
        {loading && <Spinner />}
        <InfiniteScroll
          dataLength={articles.length}
          next={fetchMoreData}
          hasMore={articles.length < totalResults}
          loader={<Spinner />}
        >
          <div className="container">
            <div className="row">
              {articles.map((element) => (
                <div className="col-md-4" key={element.url}>
                  <NewItem
                    title={element.title ? element.title.slice(0, 40) : ""}
                    description={
                      element.description
                        ? element.description.slice(0, 80)
                        : ""
                    }
                    imageUrl={
                      element.urlToImage
                        ? element.urlToImage
                        : "https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/TGJZRTAEEEQPI43HIGY42CNRCE.jpg&w=1440"
                    }
                    newsUrl={element.url}
                    author={element.author}
                    date={element.publishedAt}
                    source={element.source.name}
                  />
                </div>
              ))}
            </div>
          </div>
        </InfiniteScroll>
      </div>
    );
}
News.defaultProps = {
  country: "us",
  pageSize: 8,
  category: "general",
};

News.propTypes = {
  country: PropTypes.string.isRequired,
  pageSize: PropTypes.number.isRequired,
  category: PropTypes.string.isRequired,
};

export default News;