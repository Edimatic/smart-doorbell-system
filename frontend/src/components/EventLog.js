import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EventLog = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await axios.get('/api/events');
        setEvents(response.data);
      } catch (error) {
        console.error("There was an error fetching the events!", error);
      }
    };

    fetchEvents();
  }, []);

  return (
    <div>
      <h1>Event Log</h1>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            {event.event_type} at {event.event_time}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventLog;

