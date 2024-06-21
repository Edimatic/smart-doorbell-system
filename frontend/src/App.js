import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RegistrationForm from './components/RegistrationForm';
import LoginForm from './components/LoginForm';
import Dashboard from './components/Dashboard';
import LiveVideoFeed from './components/LiveVideoFeed';
import NotificationSettings from './components/NotificationSettings';
import EventLog from './components/EventLog';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/register" component={RegistrationForm} />
        <Route path="/login" component={LoginForm} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/live-video" component={LiveVideoFeed} />
        <Route path="/notifications" component={NotificationSettings} />
        <Route path="/events" component={EventLog} />
        <Route path="/" exact component={Dashboard} />
      </Switch>
    </Router>
  );
}

export default App;

