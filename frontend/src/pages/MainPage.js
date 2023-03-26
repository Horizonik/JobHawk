import React, {useState} from 'react';
import SearchPage from './SearchPage';
import {CSSTransition, TransitionGroup} from 'react-transition-group';
import './MainPage.css';

const MainPage = () => {
    const [searchStarted, setSearchStarted] = useState(false);

    const handleStartSearching = () => {
        setSearchStarted(true);
    };

    const handleSamlLogin = () => {
        window.location.href = 'http://127.0.0.1:8000/api/saml-auth/';
    };

    return (<TransitionGroup>
        <CSSTransition
            key={searchStarted ? 'search-page' : 'main-page'}
            timeout={300}
            classNames="page-transition"
        >
            {searchStarted ? (<SearchPage/>) : (<div className="main-page">
                <div class="container">
                    <div class="header">
                        <h1>Welcome to JobHawk</h1>
                        <p>Find your dream job among thousands of available opportunities. Enter a job title, keyword or
                            location and start your search now!</p>
                        <div class="search-container">
                            <input class="search-input" type="text" placeholder="Job title, keywords or location"/>
                            <button class="search-button">Search</button>
                        </div>
                    </div>
                    <div class="info-section">
                        <div class="info-box">
                            <h2>Introduction</h2>
                            <p>JobHawk is a web app that enables users to quickly find jobs they're best suited for. Our
                                platform uses AI and NLP algorithms to process user inputs and fetch the most relevant
                                job listings from LinkedIn, Indeed, and Glassdoor.</p>
                        </div>
                        <div class="info-box">
                            <h2>How it works</h2>
                            <ul>
                                <li>Enter a job title or skills you're familiar with.</li>
                                <li>AI generates keywords and topics based on your input.</li>
                                <li>Keywords are searched in job sites and results are scraped.</li>
                                <li>NLP processes the data, extracting essential skills and job descriptions.</li>
                            </ul>
                        </div>
                        <div class="info-box">
                            <h2>Technically speaking</h2>
                            <p>Our backend runs on Django, where AI models, web scrapers, and NLP algorithms operate.
                                Job data is saved as models. The frontend, built using React, offers a seamless SPA
                                (Single Page Application) experience and communicates with the backend for keyword
                                passing.</p>
                        </div>
                        <div class="info-box">
                            <h2>Production & Future</h2>
                            <p>The backend is managed by Nginx and Gunicorn using WSGI. Our web app is Dockerized and
                                tested with GitHub Actions to ensure smooth operation. Future improvements include
                                separate Dockerfiles for front and back ends, using Docker Compose, and refining NLP
                                processing and AI models.</p>
                        </div>
                    </div>
                </div>
                <button className="feedback-button" aria-label="Quick feedback">
                    <i className="fas fa-comment-alt"></i>
                </button>
            </div>)}
        </CSSTransition>
    </TransitionGroup>);
};

export default MainPage;


