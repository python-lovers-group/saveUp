<template>
  <nav class="navbar navbar-expand-lg navbar-light" style="background-color: white">
    <Logo />
    <v-spacer></v-spacer>
    <v-spacer></v-spacer>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNavAltMarkup"
      aria-controls="navbarNavAltMarkup"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-item nav-main" href="#">Products</a>
        <a class="nav-item nav-main" href="#">About us</a>
        <router-link
          v-if="!isLoggedIn"
          class="nav-item nav-main"
          :to="{ name: 'Login' }"
          >Login</router-link
        >
        <router-link
                v-if="isLoggedIn"
                class="nav-item nav-main"
                :to="{ name: 'Profile' }"
        >Profile</router-link
        >
      </div>
      <v-btn
        rounded
        color="#02C39A"
        class="nav-btn"
        v-if="!isLoggedIn"
        :to="{ name: 'Register' }"
        dark
        >Get Started</v-btn
      >
      <v-btn
        rounded
        color="#02C39A"
        class="nav-btn"
        @click="logout"
        v-if="isLoggedIn"
        dark
        >Logout</v-btn
      >
    </div>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";
import Logo from "../components/Logo";

export default {
  name: "NavBar",
  components: {Logo},
  methods: {
    logout() {
      window.Swal.fire({
        title: "Are you sure?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Logout!"
      }).then(result => {
        if (result.value) {
          this.$store
            .dispatch("logout")
            .then(() => {
              this.$router.push({ name: "Home" });
              window.Toast.fire({
                icon: "success",
                title: this.message
              });
            })
            .catch(err => console.log(err));
        }
      });
    }
  },
  computed: {
    ...mapGetters({
      isLoggedIn: "isLoggedIn",
      message: "getMessage"
    })
  }
};
</script>

<style scoped>
.nav-main {
  font-weight: 800;
  font-size: 18px;
  color: #00a896;
  margin-top: 1rem;
  margin-right: 50px;
  text-decoration: none;
  transition: all 0.3s ease-out;
}

.nav-main:nth-last-child(1) {
  margin-right: 80px;
}

.nav-main:hover {
  color: #006e5c;
  text-decoration: underline;
}

.nav-btn {
  margin-top: 1rem;
  font-weight: 800;
  transition: all 0.3s ease-out;
}
</style>
