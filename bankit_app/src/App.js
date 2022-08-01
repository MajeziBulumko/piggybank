import logo from './logo.svg';
import './App.css';
import {Home} from './Home';
import {Account} from './Account';
import {Client} from './Client';
import {Login} from './Login';
import {BrowserRouter, Routes,NavLink, Route} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <h3 className='d-flex justify-content-center m-3'>
        Piggy BagIt
      </h3>
      <nav className="navbar navbar-expand-sm bg-light navbar-dark">
        <ul className="navbar-nav">
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/home">
              Home
            </NavLink>
          </li>
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/account">
              Account
            </NavLink>
          </li>
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/client">
              Client
            </NavLink>
          </li>
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/login">
              Login
            </NavLink>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path='/home' component={<Home/>}/>
        <Route path='/account' component={<Account/>}/>
        <Route path='/client' component={<Client/>}/>
        <Route path='/login' component={<Login/>}/>
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
