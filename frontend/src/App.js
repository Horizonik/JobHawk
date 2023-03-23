import React, {useState, useEffect} from "react";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import SearchBar from "./components/SearchBar";
import JobList from "./components/JobList";
import axios from "axios";
import "./styles.css";

const SamlRedirectHandler = () => {
    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/saml-auth/", {
            credentials: "include",
        })
            .then((response) => response.json())
            .then((userData) => {
                // Save the user data in your frontend state management system
            })
            .catch((error) => {
                // Handle the error
            });
    }, []);

    // Render a message or loading spinner while fetching the user data
    return (<div>
        <p>Authenticating...</p>
    </div>);
};

function App() {
    const [jobs, setJobs] = useState([]);

    const handleSearch = async (searchQuery) => {
        try {
            const response = await axios.get(`/api/jobs/?search=${searchQuery}`);
            console.log(response.data); // Log the search results to the console
            setJobs(response.data);
        } catch (error) {
            console.error("Error fetching jobs:", error);
        }
    };

    return (<Router>
            <Routes>
                <Route path="/saml-redirect" element={<SamlRedirectHandler/>}/>
                <Route path="/" element={<>
                    <div className="App">
                        <a href="http://127.0.0.1:8000/saml2/login/">Login with SAML</a>
                        <SearchBar onSearch={handleSearch}/>
                        <JobList jobs={jobs}/>
                    </div>
                </>}/>
            </Routes>
        </Router>);
}

export default App;