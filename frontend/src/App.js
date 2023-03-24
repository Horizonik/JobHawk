// App.js
import React from 'react';
import './App.css';
import MainPage from './pages/MainPage';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <section>
                    <nav>
                        <a href="#mainpage" className="logo">JobHawk</a>
                        <ul className="menu">
                            <li><a href="#about">About Us</a></li>
                            <li><a href="#contact">Contact</a></li>
                        </ul>
                    </nav>
                </section>
            </header>
            <main>
                <MainPage/>
            </main>
            <footer>
                <section>
                    <p>&copy; 2023 JobHawk. All rights reserved.</p>
                </section>
            </footer>
        </div>
    );
}

export default App;
