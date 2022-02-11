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
      const endpoint = 'http://127.0.0.1:5000/auth/login/' + username + "/" + password
      return await (await fetch(endpoint)).json();
    } else {
      return false
    }
  },
  fetchRegister: async (username, password, email, firstname, lastname, phone_number) => {
    if (username.length > 0 && password.length > 0 && email.length > 0 && firstname.length > 0 && lastname.length > 0 && phone_number.length > 0) {
      const endpoint = 'http://127.0.0.1:5000/auth/register/' + username + "/" + password + "/" + email + "/" + firstname + "/" + lastname + "/" + phone_number
      return await (await fetch(endpoint)).json();
    } else {
      return {"response": "False"}
    }
  },
  fetchPurchase: async (eid) => {
    if (localStorage.getItem("logged") != "true" ) {
      return false
    }
    const endpoint = 'http://127.0.0.1:5000/ticket/' + eid + "/" + localStorage.getItem("username")
    return await (await fetch(endpoint)).json();
  },
  fetchAddMoney: async (amount) => {
    const endpoint = 'http://127.0.0.1:5000/add_money/' + localStorage.getItem("username") + "/" + amount
    return await (await fetch(endpoint)).json();
  },
  fetchTickets: async () => {
    const endpoint = 'http://127.0.0.1:5000/get_tickets/' + localStorage.getItem("username")
    return await (await fetch(endpoint)).json();
  }
}