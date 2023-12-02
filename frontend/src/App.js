import * as React from 'react';
import { Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import LogoutPage from './pages/LogoutPage';
import ExpensesPage from './pages/ExpensesPage';

export default function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="login" element={<LoginPage />} />
        <Route path="logout" element={<LogoutPage />} />
        <Route path="expenses" element={<ExpensesPage />} />
      </Routes>
    </div>
  );
}


// Routes https://www.codeconcisely.com/posts/react-navigation/