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
                <section>
                    <h1>Find Your Dream Job with JobHawk</h1>
                    <p>Find your dream job with ease using our AI-powered job search.</p>
                    <div className="button-container">
                        <button className="start-button" onClick={handleStartSearching}>Let's Start</button>
                    </div>
                    <div className="button-container">
                        <button className="start-button" onClick={handleSamlLogin}>SAML Login</button>
                    </div>
                </section>
                <section>
                    <div className="features-wrapper">
                        <h2>Why Choose JobHawk?</h2>

                        <div className="groups-container">
                            <div className="blur"></div>

                            <div className="group">
                                <img src="icons/fast.png" alt="fast_icon"/>
                                <h3>Fast Results</h3>
                                <p>Get job recommendations instantly with our AI-powered system.</p>
                            </div>

                            <div className="group">
                                <img src="icons/accurate.png" alt="accurate_icon"/>
                                <h3>Accurate Results</h3>
                                <p>Our system matches you with the most relevant job openings based on your skills and
                                    experience.</p>
                            </div>
                            <div className="group">
                                <img src="icons/easy.png" alt="easy_icon"/>
                                <h3>Easy to Use</h3>
                                <p>Our simple and intuitive interface makes job searching a breeze.</p>
                            </div>
                        </div>
                    </div>
                </section>
            </div>)}
        </CSSTransition>
    </TransitionGroup>);
};

export default MainPage;


