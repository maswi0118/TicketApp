export default {
  fetchArtists: async (artistName) => {
    const endpoint = 'http://127.0.0.1:5000/artists/' + artistName
    return await (await fetch(endpoint)).json();
  }
}