import React from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    if (window.confirm('Do you want to logout?')) {
      // remove the username from local storage
      localStorage.removeItem('username');
     navigate('/');
    }
  };

  return (
    <div>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Logout;