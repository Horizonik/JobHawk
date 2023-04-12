import React, {useState} from 'react';
import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Error404 from './errorPages/Error404';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import ResultsPage from "./pages/JobList";
import LoadingContext from "./contexts/LoadingContext";
import Error500 from "./errorPages/Error500";
import Error502 from "./errorPages/Error502";

const App = () => {
    const [searchValue, setSearchValue] = useState('');
    const [searchFocused, setSearchFocused] = useState(false);

    const handleSearch = () => {
        if (searchValue.trim() !== '') {
            setSearchFocused(true);
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

    const [loading, setLoading] = useState(false);

    return (
        <LoadingContext.Provider value={{loading, setLoading}}>
            <Router>
                <div className="App">
                    <Navbar/>
                    <div className="container">
                        <Routes>
                            <Route
                                path="/"
                                element={
                                    <HomePage
                                        searchValue={searchValue}
                                        handleSearchInput={handleSearchInput}
                                        handleSearchKeyPress={handleSearchKeyPress}
                                        handleSearch={handleSearch}
                                        searchFocused={searchFocused}
                                    />
                                }
                            />
                            <Route path="/results" element={<ResultsPage/>}/>

                            <Route path="/error/404" component={Error404} />
                            <Route path="/error/500" component={Error500} />
                            <Route path="/error/502" component={Error502} />
                        </Routes>
                        <Footer/>
                    </div>
                </div>
            </Router>
        </LoadingContext.Provider>
    );
};

export default App;
