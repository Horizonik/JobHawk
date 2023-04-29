import React from 'react';
import InfoSection from '../components/InfoSection';
import ResultsPage from './JobList';

const HomePage = ({
                      searchValue, handleSearchInput, handleSearchKeyPress, handleSearch, searchFocused,
                  }) => {
    return (<>
        <div className="header">
            <h1>Welcome to JobHawk</h1>
            <p>Find your dream job among thousands of available opportunities. Enter a job title, keyword, or
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
                    <i className="bi bi-search"></i>
                </button>
            </div>
        </div>
        <div className="separator"></div>
        <InfoSection searchFocused={searchFocused} />
        {searchFocused && (<div className="results-section">
            <ResultsPage />
        </div>)}
    </>);
};

export default HomePage;
