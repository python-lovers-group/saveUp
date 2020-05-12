import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { types } from "./mutation-types";

Vue.use(Vuex);

// const AUTH_API_URL = "http://127.0.0.1:8100/accounts/";
const HEROKU_APP_API_URL = "https://saveupyourmoney.herokuapp.com/";

const state = {
  status: "",
  token: localStorage.getItem("token") || "",
  user: {},
  loading: false,
  error: null
};

const mutations = {
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
    console.log(payload.user);
  },

  [types.AUTH_ERROR](state, error) {
    state.status = error;
  },

  [types.LOGOUT](state) {
    state.status = "";
    state.token = "";
  }
};

const actions = {
  login({ commit }, user) {
    commit(types.START_LOADING);
    commit(types.CLEAR_ERROR);

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
            "Token: " + resp.data.token;
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
    commit(types.CLEAR_ERROR);

    return new Promise((resolve, reject) => {
      commit(types.AUTH_REQUEST);
      axios({
        url: HEROKU_APP_API_URL + "user/create/",
        data: user,
        method: "POST"
      })
        .then(resp => {
          // const token = resp.data.key;
          // const user = resp.data.user;
          // const userObj = {...resp.data};
          // localStorage.setItem("token", token);
          // axios.defaults.headers.common["Authorization"] = "Token: " + token;
          console.log(resp.data);
          commit(types.END_LOADING);
          // commit(types.AUTH_SUCCESS, token, userObj);
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
    return new Promise((resolve, reject) => {
      commit(types.LOGOUT);
      commit(types.END_LOADING);
      localStorage.removeItem("token");
      delete axios.defaults.headers.common["Authorization"];
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
  getError: state => state.error
};

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
