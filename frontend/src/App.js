import React, {useEffect, useState} from 'react';
import './App.css';
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import InfoSection from "./components/InfoSection";
import axios from "axios";
import JobCard from "./components/JobCard";

const pageMarginStyle = {
    margin: '60px 30px 30px 30px',
};

const tasksGridStyle = {
    display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', alignItems: 'start',
};

const App = () => {
    const [jobs, setJobs] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [filteredJobs, setFilteredJobs] = useState([]);

    // Getting jobs data from django using axios and rest api
    useEffect(() => {
        axios.get('http://localhost:8000')
            .then(res => {
                const data = res.data;
                setJobs(data);
            })
            .catch(err => {
            });
    }, []);

    // Filter jobs based on searchTerm
    useEffect(() => {
        if (searchTerm === '') {
            setFilteredJobs([]);

        } else {
            const search = searchTerm.toLowerCase();

            const filteredResults = jobs.filter(job => {
                const title = job.title.toLowerCase();
                return title.includes(search);
            });
            setFilteredJobs(filteredResults);
            console.log(filteredResults.toString());
        }
    }, [searchTerm, jobs]);

    return (<div style={pageMarginStyle}>
            {/*<Navbar />*/}
            <div>
                <div className="header">
                    <h1>Welcome to JobHawk</h1>
                    <p>
                        Find your dream job among thousands of available opportunities. Enter a job title, keyword, or
                        location and start your search now!
                    </p>
                </div>

                <div className="search-container search-focused">
                    <input
                        className="search-input"
                        type="text"
                        placeholder="Job title, keywords or location"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                    <button className="search-button">
                        <i className="bi bi-search"></i> {/* magnifying glass icon */}
                    </button>
                </div>

                <div className="separator"></div>

                {/* displays jobs if more than 0 match the search term */}
                {filteredJobs.length > 0 ? (<div className="results-section" style={tasksGridStyle}>
                        {filteredJobs.map((job) => (<JobCard job={job} key={job.id} />))}
                    </div>) : (searchTerm ? <div className="emptyResults">
                        <h2>No jobs found</h2>
                        <InfoSection />
                    </div>: '')}

            </div>
            <Footer />
        </div>);
}

export default App;
