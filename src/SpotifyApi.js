export default {
  fetchArtists: async (artistName) => {
    if (artistName.length > 0) {
      const endpoint = 'http://127.0.0.1:5000/artists/' + artistName
      return await (await fetch(endpoint)).json();
    } else {
      return null;
    }
  }
}