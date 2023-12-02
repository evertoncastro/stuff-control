import { Component } from "react";
import { Link } from 'react-router-dom';

class HomePage extends Component {
  render() {
    return (
      <main className="container">
        <h1 className="text-uppercase text-center my-4">Home page</h1>
        <Link to="/expenses">Expenses</Link>
        <Link to="/login">Login</Link>
        <Link to="/logout">Logout</Link>
      </main>
    );
  }
}

export default HomePage;