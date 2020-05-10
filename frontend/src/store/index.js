import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { types } from "./mutation-types";

Vue.use(Vuex);

const AUTH_API_URL = "http://127.0.0.1:8100/accounts/";

const state = {
  status: "",
  token: localStorage.getItem("token") || "",
  user: {}
};

const mutations = {
  [types.AUTH_REQUEST](state) {
    state.status = "loading";
  },

  [types.AUTH_SUCCESS](state, token, user) {
    console.log("witam");
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
    return new Promise((resolve, reject) => {
      commit(types.AUTH_REQUEST);
      axios({ url: AUTH_API_URL + "login/", data: user, method: "POST" })
        .then(resp => {
          const token = resp.data.key;
          // const user = resp.data.user;
          const user = {};
          localStorage.setItem("token", token);
          axios.defaults.headers.common["Authorization"] = "Token: " + token;
          commit(types.AUTH_SUCCESS, token, user);
          resolve(resp);
        })
        .catch(err => {
          commit(types.AUTH_ERROR, err);
          localStorage.removeItem("token");
          reject(err);
        });
    });
  },

  register({ commit }, user) {
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
          commit(types.AUTH_SUCCESS, token, user);
          resolve(resp);
        })
        .catch(err => {
          commit(types.AUTH_ERROR, err);
          localStorage.removeItem("token");
          reject(err);
        });
    });
  },

  logout({ commit }) {
    return new Promise((resolve, reject) => {
      commit(types.LOGOUT);
      localStorage.removeItem("token");
      delete axios.defaults.headers.common["Authorization"];
      resolve();
      console.log(reject);
    });
  }
};
const getters = {
  isLoggedIn: state => !!state.token,
  authStatus: state => state.status
};

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
