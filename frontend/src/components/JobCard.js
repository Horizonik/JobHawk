import React from 'react';

const JobCard = ({ job }) => {
    return (
        <div className="job-card" style={{ width: '100%', height: '150%' }}>
            <h3>{job.title}</h3>
            <p>{job.company}</p>
            <p>{job.location}</p>
            <p>{job.skills.join(', ')}</p>
            <a href={job.url} target="_blank" rel="noopener noreferrer">
                Apply Now
            </a>
        </div>
    );
};

export default JobCard;
