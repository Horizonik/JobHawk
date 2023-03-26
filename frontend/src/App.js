import React, {useState} from 'react';
import './App.css';
import ResultsPage from "./pages/ResultsPage";

const App = () => {
    const [searchValue, setSearchValue] = useState('');
    const [results, setResults] = useState([]);
    const [searchFocused, setSearchFocused] = useState(false);

    const handleSearch = () => {
        if (searchValue.trim() !== '') {
            setSearchFocused(true);
            // Fetch search results and update the results state
        }
    };

    const handleSearchInput = (event) => {
        setSearchValue(event.target.value);
    };

    const handleSearchKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    return (<div className="App">
            <header className="App-header">
                <nav className="navbar">
                    <div className="navbar-logo">JobHawk</div>
                    <div className="navbar-links">
                        <a href="#" className="navbar-link">Home</a>
                        <a href="#" className="navbar-link">About</a>
                        <a href="#" className="navbar-link">Contact</a>
                    </div>
                </nav>
            </header>

            <div className="container">
                <div className="header">
                    <h1>Welcome to JobHawk</h1>
                    <p>Find your dream job among thousands of available opportunities. Enter a job title, keyword or
                        location and start your search now!</p>
                    <div className={`search-container ${searchFocused ? 'search-focused' : ''}`}>
                        <input
                            className="search-input"
                            type="text"
                            placeholder="Job title, keywords or location"
                            value={searchValue}
                            onChange={handleSearchInput}
                            onKeyPress={handleSearchKeyPress}
                        />
                        <button className="search-button" onClick={handleSearch}>
                            Search
                        </button>
                    </div>
                </div>


                <div className={`info-section ${searchFocused ? 'fadeOut' : 'fadeIn'}`}>
                    <div className="info-section">
                        <div className="info-box">
                            <h2>Introduction</h2>
                            <p>JobHawk is a web app that enables users to quickly find jobs they're best suited for.
                                Our
                                platform uses AI and NLP algorithms to process user inputs and fetch the most
                                relevant
                                job listings from LinkedIn, Indeed, and Glassdoor.</p>
                        </div>
                        <div className="info-box">
                            <h2>How it works</h2>
                            <ul>
                                <li>Enter a job title or skills you're familiar with.</li>
                                <li>AI generates keywords and topics based on your input.</li>
                                <li>Keywords are searched in job sites and results are scraped.</li>
                                <li>NLP processes the data, extracting essential skills and job descriptions.</li>
                            </ul>
                        </div>
                        <div className="info-box">
                            <h2>Technically speaking</h2>
                            <p>Our backend runs on Django, where AI models, web scrapers, and NLP algorithms
                                operate.
                                Job data is saved as models. The frontend, built using React, offers a seamless SPA
                                (Single Page Application) experience and communicates with the backend for keyword
                                passing.</p>
                        </div>
                        <div className="info-box">
                            <h2>Production & Future</h2>
                            <p>The backend is managed by Nginx and Gunicorn using WSGI. Our web app is Dockerized
                                and
                                tested with GitHub Actions to ensure smooth operation. Future improvements include
                                separate Dockerfiles for front and back ends, using Docker Compose, and refining NLP
                                processing and AI models.</p>
                        </div>
                    </div>
                </div>

                {searchFocused && (<div className="results-section">
                    <ResultsPage/>
                </div>)}

                <footer className="footer">
                    &copy; 2023 JobHawk. All rights reserved.
                </footer>
            </div>

            <button className="feedback-button" aria-label="Quick feedback">
                <i className="fas fa-comment-alt"></i>
            </button>
        </div>

    );
}

export default App;
