import SERVER from './serverUrl';

const SERVER_URL = `${SERVER}/authors`;

class AuthorApi {
  static getAllAuthors() {
    return fetch(SERVER_URL).then(response => response.json())
    .then((data) => {
        console.log('Success:', data);
        })
        .catch((error) => {
        console.error('Error:', error);
        });
  }
}

export default AuthorApi;
