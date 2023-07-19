import React from 'react';
import './App.css';
import SearchPage from "./pages/SearchPage";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";


const pageMarginStyle = {
    margin: '60px 30px 30px 30px',
}


const App = () => {

    return (
        <div style={pageMarginStyle}>
            <Navbar />
            {<SearchPage />}
            <Footer />
        </div>
    );
}

export default App;
