import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView";
import store from "../store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/about",
    name: "about",
    component: About
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const requireAuth = to.matched.some(x => x.meta.requiresAuth);
  const isLoggedIn = store.getters.isLoggedIn;
  if (requireAuth && !isLoggedIn) {
    next({ name: "Home" });
  }
  next();
});

export default router;
