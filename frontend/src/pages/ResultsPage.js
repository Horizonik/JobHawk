// import React, { useState, useEffect, useCallback } from 'react';
// import JobCard from '../components/JobCard';
// import axios from 'axios';
//
// const ResultsPage = ({ searchQuery }) => {
//     const [jobs, setJobs] = useState([]);
//     const [page, setPage] = useState(1);
//     const [loading, setLoading] = useState(false);
//     const [hasMore, setHasMore] = useState(true);
//
//     const fetchJobs = useCallback(async () => {
//         setLoading(true);
//         try {
//             const response = await axios.get(`/api/jobs/?search=${searchQuery}&page=${page}`);
//             setJobs((prevJobs) => [...prevJobs, ...response.data.results]);
//             setHasMore(response.data.next !== null);
//         } catch (error) {
//             console.error(error);
//         } finally {
//             setLoading(false);
//         }
//     }, [searchQuery, page]);
//
//     useEffect(() => {
//         fetchJobs();
//     }, [fetchJobs]);
//
//     const handleScroll = (e) => {
//         const { scrollTop, clientHeight, scrollHeight } = e.currentTarget;
//         if (scrollHeight - scrollTop === clientHeight && !loading && hasMore) {
//             setPage((prevPage) => prevPage + 1);
//         }
//     };
//
//     return (
//         <div className="results-page" onScroll={handleScroll}>
//             <div className="job-cards">
//                 {jobs.map((job) => (
//                     <JobCard key={job.id} job={job} />
//                 ))}
//             </div>
//             {loading && <p>Loading...</p>}
//             {!hasMore && <p>No more jobs to display.</p>}
//         </div>
//     );
// };
//
// export default ResultsPage;


// ResultsPage.js (update)
import React, {useState, useEffect, useCallback} from 'react';
import JobCard from '../components/JobCard';
import axios from 'axios';

const ResultsPage = ({searchQuery}) => {
    const [jobs, setJobs] = useState([]);
    const [page, setPage] = useState(1);
    const [loading, setLoading] = useState(false);
    const [hasMore, setHasMore] = useState(true);

    const fetchJobs = useCallback(async () => {
        setLoading(true);
        try {
            const response = await axios.get(`/api/jobs/?search=${searchQuery}&page=${page}`);
            if (Array.isArray(response.data.results)) {
                setJobs((prevJobs) => [...prevJobs, ...response.data.results]);
                setHasMore(response.data.next !== null);
            } else {
                console.error('Invalid response data:', response.data);
            }
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    }, [searchQuery, page]);

    useEffect(() => {
        fetchJobs();
    }, [fetchJobs]);

    const handleScroll = (e) => {
        const {scrollTop, clientHeight, scrollHeight} = e.currentTarget;
        if (scrollHeight - scrollTop === clientHeight && !loading && hasMore) {
            setPage((prevPage) => prevPage + 1);
        }
    };

    return (
        <div className="results-page" onScroll={handleScroll}>
            <div className="job-cards">
                {jobs.map((job) => (
                    <JobCard key={job.id} job={job}/>
                ))}
            </div>
            {loading && <p>Loading...</p>}
            {!hasMore && <p>No more jobs to display.</p>}
        </div>
    );
};

export default ResultsPage;
