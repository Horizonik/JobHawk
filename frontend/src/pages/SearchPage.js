// SearchPage.js (update)
import React, {useState} from 'react';
import {CSSTransition, TransitionGroup} from 'react-transition-group';
import ResultsPage from './ResultsPage';
import './SearchPage.css';
import MainPage from "./MainPage";

const SearchPage = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [submittedQuery, setSubmittedQuery] = useState('');

    const [searchStarted, setSearchStarted] = useState(true);

    const handleStopSearching = () => {
        setSearchStarted(false);
    };

    const handleSearchChange = (e) => {
        setSearchQuery(e.target.value);
    };

    const handleSearchSubmit = (e) => {
        e.preventDefault();
        setSubmittedQuery(searchQuery);
    };

    return (<TransitionGroup>
        <CSSTransition
            key={searchStarted ? 'search-page' : 'main-page'}
            timeout={300}
            classNames="page-transition"
        >
            {!searchStarted ? (<MainPage/>) : (
                <div className="search-page">
                    <main>
                        <section>
                            <button onClick={handleStopSearching}>Go Back</button>
                            <form onSubmit={handleSearchSubmit}>
                                <input
                                    type="text"
                                    placeholder="Enter keywords or job titles"
                                    value={searchQuery}
                                    onChange={handleSearchChange}
                                />
                                <button type="submit">Search</button>
                            </form>
                        </section>
                        <section>
                            <div className="padding-wrapper">
                                <h2 className="sub-title">Results</h2>

                                <div className="container">
                                </div>
                            </div>
                        </section>
                    </main>

                    <TransitionGroup component={null}>
                        <CSSTransition
                            key={submittedQuery}
                            timeout={300}
                            classNames="page-transition"
                            in={!!submittedQuery}
                        >
                            <ResultsPage searchQuery={submittedQuery}/>
                        </CSSTransition>
                    </TransitionGroup>
                </div>
            )}
        </CSSTransition>
    </TransitionGroup>);
};

export default SearchPage;
