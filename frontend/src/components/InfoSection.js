import React from 'react';

const InfoSection = ({searchFocused}) => {
    return (
        <div className={`info-section ${searchFocused ? 'fadeOut' : 'fadeIn'}`}>
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
                Enter a job title or skills you're familiar with.
                AI generates keywords and topics based on your input.
                Keywords are searched in job sites and results are scraped.
                NLP processes the data, extracting essential skills and job descriptions.

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
    );
};

export default InfoSection;
