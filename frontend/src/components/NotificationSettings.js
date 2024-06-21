import React, { useState } from 'react';
import axios from 'axios';

const NotificationSettings = () => {
  const [notificationsEnabled, setNotificationsEnabled] = useState(false);
  const [notificationType, setNotificationType] = useState('push');

  const handleSave = async () => {
    try {
      const response = await axios.post('/api/notifications/settings', {
        notificationsEnabled,
        notificationType,
      });
      console.log(response.data);
    } catch (error) {
      console.error("There was an error saving the notification settings!", error);
    }
  };

  return (
    <div>
      <h1>Notification Settings</h1>
      <div>
        <label>
          Enable Notifications:
          <input
            type="checkbox"
            checked={notificationsEnabled}
            onChange={() => setNotificationsEnabled(!notificationsEnabled)}
          />
        </label>
      </div>
      <div>
        <label>
          Notification Type:
          <select
            value={notificationType}
            onChange={(e) => setNotificationType(e.target.value)}
          >
            <option value="push">Push</option>
            <option value="email">Email</option>
          </select>
        </label>
      </div>
      <button onClick={handleSave}>Save</button>
    </div>
  );
};

export default NotificationSettings;

