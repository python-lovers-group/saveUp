import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { types } from "./mutation-types";

Vue.use(Vuex);

// const AUTH_API_URL = "http://127.0.0.1:8100/accounts/";
const HEROKU_APP_API_URL = "https://saveupyourmoney.herokuapp.com/";

const TOKEN = localStorage.getItem("token");
let user = window.localStorage.getItem("user");

const state = {
  status: "",
  token: TOKEN || "",
  user: TOKEN ? JSON.parse(user) : {},
  loading: false,
  error: null,
  message: null
};

const saveUser = () => {
  window.localStorage.setItem("user", JSON.stringify(state.user));
};

const mutations = {
  [types.SET_MESSAGE](state, payload) {
    state.message = payload;
  },

  [types.CLEAR_MESSAGE](state) {
    state.message = null;
  },

  [types.SET_ERROR](state, payload) {
    state.error = payload;
  },

  [types.CLEAR_ERROR](state) {
    state.error = null;
  },

  [types.START_LOADING](state) {
    state.loading = true;
  },

  [types.END_LOADING](state) {
    state.loading = false;
  },

  [types.AUTH_REQUEST](state) {
    state.status = "loading";
  },

  [types.AUTH_SUCCESS](state, payload) {
    state.status = "success";
    state.token = payload.token;
    state.user = payload.user;
    saveUser();
  },

  [types.AUTH_ERROR](state, error) {
    state.status = error;
  },

  [types.LOGOUT](state) {
    state.status = "";
    state.token = "";
    state.user = {};
    saveUser();
  }
};

const actions = {
  login({ commit }, user) {
    commit(types.START_LOADING);
    commit(types.CLEAR_ERROR);
    commit(types.CLEAR_MESSAGE);

    return new Promise((resolve, reject) => {
      commit(types.AUTH_REQUEST);
      axios({
        url: HEROKU_APP_API_URL + "user/token/",
        data: user,
        method: "POST"
      })
        .then(resp => {
          commit(types.AUTH_SUCCESS, {
            token: resp.data.token,
            user: resp.data
          });
          localStorage.setItem("token", resp.data.token);
          axios.defaults.headers.common["Authorization"] =
            "Token " + resp.data.token;
          commit(types.SET_MESSAGE, "You have successfully logged in!");
          commit(types.END_LOADING);
          resolve(resp);
        })
        .catch(err => {
          commit(types.AUTH_ERROR, err);
          commit(types.SET_ERROR, err);
          commit(types.END_LOADING);
          localStorage.removeItem("token");
          reject(err);
        });
    });
  },

  register({ commit }, user) {
    commit(types.START_LOADING);
    commit(types.CLEAR_MESSAGE);
    commit(types.CLEAR_ERROR);

    return new Promise((resolve, reject) => {
      commit(types.AUTH_REQUEST);
      axios({
        url: HEROKU_APP_API_URL + "user/create/",
        data: user,
        method: "POST"
      })
        .then(resp => {
          commit(types.END_LOADING);
          commit(types.SET_MESSAGE, "Your account was created successfully!");
          resolve(resp);
        })
        .catch(err => {
          commit(types.AUTH_ERROR, err);
          commit(types.SET_ERROR, err);
          commit(types.END_LOADING);
          localStorage.removeItem("token");
          reject(err);
        });
    });
  },

  logout({ commit }) {
    commit(types.START_LOADING);
    commit(types.CLEAR_MESSAGE);

    return new Promise((resolve, reject) => {
      commit(types.LOGOUT);
      commit(types.END_LOADING);
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      delete axios.defaults.headers.common["Authorization"];
      commit(types.SET_MESSAGE, "See you later!");
      resolve();
      console.log(reject);
    });
  },

  clearError({ commit }) {
    commit(types.CLEAR_ERROR);
  }
};
const getters = {
  isLoggedIn: state => !!state.token,
  authStatus: state => state.status,
  getUser: state => state.user,
  loading: state => state.loading,
  getError: state => state.error,
  getMessage: state => state.message
};

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
