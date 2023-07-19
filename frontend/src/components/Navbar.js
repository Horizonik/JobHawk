import React, {useContext} from 'react';
import LoadingContext from '../contexts/LoadingContext';

const Navbar = () => {

    const {loading} = useContext(LoadingContext);

    return (
        <header className="App-header">
            <nav className="navbar">
                <div className="navbar-logo">JobHawk</div>
                <div className="navbar-links">
                    <a href="#loading" id="loading-icon" className="navbar-link">
                        <i
                            className={`bi ${
                                loading ? 'bi-arrow-repeat' : 'bi-circle-fill'
                            } ${loading ? 'spinning' : ''}`}
                        ></i>
                    </a>
                    <a href="#home" className="navbar-link"><i className="bi bi-house"></i></a>
                    <a href="#contact" className="navbar-link"><i className="bi bi-envelope"></i></a>
                </div>
            </nav>
        </header>
    );
};

export default Navbar;
