import React, { useState } from 'react';

function SearchBar({ onSearch }) {
    const [searchQuery, setSearchQuery] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        onSearch(searchQuery);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search for jobs..."
            />
            <button type="submit">Search</button>
        </form>
    );
}

export default SearchBar;
