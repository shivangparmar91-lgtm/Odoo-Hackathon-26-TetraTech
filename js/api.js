const API_URL = 'http://localhost:5000/api';

const API = {
  fetchData: async (endpoint) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${API_URL}/${endpoint}`, {
        headers: {
          'Authorization': token ? `Bearer ${token}` : ''
        }
      });
      const text = await response.text();
      try {
        const data = JSON.parse(text);
        return data;
      } catch (parseError) {
        console.error('JSON Parse Error. Raw response:', text);
        return { success: false, message: 'Invalid JSON response from server' };
      }
    } catch (error) {
      console.error('Error fetching data:', error);
      return { success: false, message: error.message };
    }
  },
  
  postData: async (endpoint, payload) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${API_URL}/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token ? `Bearer ${token}` : ''
        },
        body: JSON.stringify(payload)
      });
      const text = await response.text();
      try {
        const data = JSON.parse(text);
        return data;
      } catch (parseError) {
        console.error('JSON Parse Error. Raw response:', text);
        return { success: false, message: 'Invalid JSON response from server' };
      }
    } catch (error) {
      console.error('Error posting data:', error);
      return { success: false, message: error.message };
    }
  },

  putData: async (endpoint, payload) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${API_URL}/${endpoint}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token ? `Bearer ${token}` : ''
        },
        body: JSON.stringify(payload)
      });
      const text = await response.text();
      try {
        const data = JSON.parse(text);
        return data;
      } catch (parseError) {
        console.error('JSON Parse Error. Raw response:', text);
        return { success: false, message: 'Invalid JSON response from server' };
      }
    } catch (error) {
      console.error('Error putting data:', error);
      return { success: false, message: error.message };
    }
  },

  deleteData: async (endpoint) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${API_URL}/${endpoint}`, {
        method: 'DELETE',
        headers: {
          'Authorization': token ? `Bearer ${token}` : ''
        }
      });
      const text = await response.text();
      try {
        const data = JSON.parse(text);
        return data;
      } catch (parseError) {
        console.error('JSON Parse Error. Raw response:', text);
        return { success: false, message: 'Invalid JSON response from server' };
      }
    } catch (error) {
      console.error('Error deleting data:', error);
      return { success: false, message: error.message };
    }
  }
};

