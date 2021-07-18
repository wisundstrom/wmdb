import settings from '../config/settings';
import axios from './axios';
import _ from 'lodash';

const {apiBaseURL} = settings;

export default class MoviesApi {
  static getGenres() {
    return axios.get(`${apiBaseURL}/genres`);
  }

  static getMoviesByGenres(genreNames) {
    return MoviesApi.getGenres()
      .then(genres => {
        var movieGenres = _.filter(genres, g => {
          return genreNames.indexOf(g.name) > -1;
        });

        return Promise.all(
          movieGenres.map(genre => {
              return axios.get(`${apiBaseURL}/movies/genre/${genre.id}/`);
            }
          ))
          .then(genreResults => {
            var result = {};
            genreResults.forEach((movies, i) => {
              result[movieGenres[i].name] = movies;
            });

            return result;
          });
      });
  }

  // convert this to top 3 most rated movies
  static getFeaturedMovies() {
    return Promise.all([
      axios.get(`${apiBaseURL}/movies/177c063e-5d2a-49de-b933-5cf1aa8cebfb`),
      axios.get(`${apiBaseURL}/movies/f1119178-c1f9-421b-b501-4f441c08337a`),
      axios.get(`${apiBaseURL}/movies/b28be524-187e-432d-bed4-050c19d33d5c`)
    ]);
  }

  static getMovie(id) {
      return axios.get(`${apiBaseURL}/movies/${id}`);
  }

  static rateMovie(id, rating) {
    return axios.post(`${apiBaseURL}/movies/${id}/rate`, {rating});
  }

  static deleteRating(id) {
    return axios.delete(`${apiBaseURL}/movies/${id}/rate`);
  }
}


