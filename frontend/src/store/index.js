import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { types } from "./mutation-types";

Vue.use(Vuex);

const AUTH_API_URL = "http://127.0.0.1:8100/accounts/";

const state = {
  status: "",
  token: localStorage.getItem("token") || "",
  user: {},
  loading: false,
};

const mutations = {
  [types.START_LOADING](state) {
    state.loading = true;
  },

  [types.END_LOADING](state) {
    state.loading = false;
  },

  [types.AUTH_REQUEST](state) {
    state.status = "loading";
  },

  [types.AUTH_SUCCESS](state, token, user) {
    state.status = "success";
    state.token = token;
    state.user = user;
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

    return new Promise((resolve, reject) => {
      commit(types.AUTH_REQUEST);
      axios({ url: AUTH_API_URL + "login/", data: user, method: "POST" })
        .then(resp => {
          const token = resp.data.key;
          // const user = resp.data.user;
          const user = {};
          localStorage.setItem("token", token);
          axios.defaults.headers.common["Authorization"] = "Token: " + token;

          commit(types.END_LOADING);
          commit(types.AUTH_SUCCESS, token, user);
          resolve(resp);
        })
        .catch(err => {
          commit(types.AUTH_ERROR, err);
          commit(types.END_LOADING);
          localStorage.removeItem("token");
          reject(err);
        });
    });
  },

  register({ commit }, user) {
    commit(types.START_LOADING);

    return new Promise((resolve, reject) => {
      commit(types.AUTH_REQUEST);
      axios({
        url: AUTH_API_URL + "registration/",
        data: user,
        method: "POST"
      })
        .then(resp => {
          const token = resp.data.key;
          // const user = resp.data.user;
          const user = {};
          localStorage.setItem("token", token);
          axios.defaults.headers.common["Authorization"] = "Token: " + token;

          commit(types.END_LOADING);
          commit(types.AUTH_SUCCESS, token, user);
          resolve(resp);
        })
        .catch(err => {
          commit(types.AUTH_ERROR, err);
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
  }
};
const getters = {
  isLoggedIn: state => !!state.token,
  authStatus: state => state.status,
  getUser: state => state.user,
  loading: state => state.loading,
};

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
