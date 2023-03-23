import React from 'react';

const JobCard = ({ job }) => {
    return (
        <div className="job-card" style={{ width: '50%', height: '25%', backgroundColor: 'lightgray', marginBottom: '1rem', padding: '1rem' }}>
            <h3>{job.title}</h3>
            <p>{job.company}</p>
            <p>{job.location}</p>
            <a href={job.url} target="_blank" rel="noopener noreferrer">View job details</a>
        </div>
    );
};

function JobList({ jobs }) {
    return (
        <div className="job-list">
            {jobs.map((job) => (
                <JobCard key={job.id} job={job} />
            ))}
        </div>
    );
}

export default JobList;
