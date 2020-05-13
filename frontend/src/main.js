import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Axios from "axios";
import vuetify from "./plugins/vuetify";
import jQuery from "jquery";
import "popper.js";
import "bootstrap";
import Swal from "sweetalert2";

window.$ = window.jQuery = jQuery;
window.Swal = Swal;

Vue.config.productionTip = false;

Vue.prototype.$http = Axios;
const token = localStorage.getItem("token");
if (token) {
  Vue.prototype.$http.defaults.headers.common["Authorization"] = token;
}

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");

const Toast = window.Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 2000,
  timerProgressBar: true,
  onOpen: toast => {
    toast.addEventListener("mouseenter", window.Swal.stopTimer);
    toast.addEventListener("mouseleave", window.Swal.resumeTimer);
  }
});

window.Toast = Toast;


