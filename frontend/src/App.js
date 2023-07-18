import axios from "axios";
import React from 'react';
import './App.css';
import JobCard from "./components/JobCard";
import HomePage from "./pages/HomePage";

const tasksGridStyle = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
    gap: '20px',
    alignItems: 'start',
};

const pageMarginStyle = {
    margin: '60px 30px 30px 30px',
}

class App extends React.Component {
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
            <div style={pageMarginStyle}>
                {<HomePage />}

                <header>Data Generated From Django</header>
                <hr />
                <div style={tasksGridStyle}>
                    {this.state.details.map((output, id) => (
                        <JobCard key={id} job={output} />
                    ))}
                </div>
            </div>
        );
    }
}

export default App;
