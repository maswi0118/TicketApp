export default {
  fetchEvents: async (searchTerm) => {
    if (searchTerm.length > 0) {
      const endpoint = 'http://127.0.0.1:5000/get_events/' + searchTerm
      return await (await fetch(endpoint)).json();
    } else {
      const endpoint = 'http://127.0.0.1:5000/get_events';
      return await (await fetch(endpoint)).json();
    }
  },
  fetchLogin: async (username, password) => {
    if (username.length > 0 && password.length > 0) {
      const endpoint = 'http:/127.0.0.1:5000/auth/login'
    }
  }
}