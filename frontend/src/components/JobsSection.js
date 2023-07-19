import JobCard from "./JobCard";
import React from "react";
import axios from "axios";


const tasksGridStyle = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
    gap: '20px',
    alignItems: 'start',
};

class JobsSection extends React.Component {

    state = {
        details: [],
    }

    componentDidMount() {
        let data;
        axios.get('http://localhost:8000')
            .then(res => {
                data = res.data;
                this.setState({
                    details: data
                });
            })
            .catch(err => {
            })
    }

    render() {
        return (
            <div className="results-section" style={tasksGridStyle}>
                {this.state.details.map((output, id) => (
                    <JobCard key={id} job={output} />
                ))}
            </div>
        );
    }
}

export default JobsSection;