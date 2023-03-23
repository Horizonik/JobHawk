import React, {useState} from 'react';
import SearchBar from './components/SearchBar';
import JobList from './components/JobList';
import axios from "axios";
import './styles.css';

function App() {
    const [jobs, setJobs] = useState([]);

    const handleSearch = async (searchQuery) => {
        try {
            const response = await axios.get(`/api/jobs/?search=${searchQuery}`);
            console.log(response.data); // Log the search results to the console
            setJobs(response.data);
        } catch (error) {
            console.error('Error fetching jobs:', error);
        }
    };

    return (
        <div className="App">
            <SearchBar onSearch={handleSearch}/>
            <JobList jobs={jobs}/>
        </div>
    );
}

export default App;
