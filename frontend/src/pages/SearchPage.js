import React from 'react';
import {useState} from 'react';
import InfoSection from '../components/InfoSection';
import JobsSection from "../components/JobsSection";

const SearchPage = () => {

    const [clickedSearch, setClickedSearch] = useState(false);

    return (
        <div>
            <div className="header">
                <h1>Welcome to JobHawk</h1>
                <p>
                    Find your dream job among thousands of available opportunities. Enter a job title, keyword, or
                    location and start your search now!
                </p>

                <div className="search-container search-focused">
                    <input
                        className="search-input"
                        type="text"
                        placeholder="Job title, keywords or location"
                    />
                    <button className="search-button" onClick={() => setClickedSearch(!clickedSearch)}>
                        <i className="bi bi-search"></i> {/* magnifying glass icon */}
                    </button>
                </div>

                <div className="separator"></div>
                {clickedSearch ? <JobsSection /> : <InfoSection />}
            </div>
        </div>
    );
}

export default SearchPage;
