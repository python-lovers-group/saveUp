<template>
  <v-content>
    <v-container fill-height fluid class="header-container">
      <v-row>
        <v-col cols="12" sm="1"></v-col>
        <v-col cols="12" md="4" class="">
          <h6 class="text--secondary subtitle-1">
            Sign in to your wallet.
          </h6>
          <transition name="slide-up" appear>
            <v-form class="pr-2" ref="signUpForm" @submit.prevent="login">
              <v-text-field
                      v-model="username"
                      label="Username"
                      type="text"
                      :rules="usernameRules"
                      required
              ></v-text-field>
              <v-text-field
                      v-model="password"
                      label="Password"
                      type="password"
                      :rules="passwordRules"
                      required
              ></v-text-field>
              <p class="caption">
                Don't have an account?
                <router-link :to="{ name: 'Register' }">Sign up!</router-link>
              </p>
              <v-btn
                      type="submit"
                      class="ma-2"
                      :loading="loading"
                      :disabled="loading"
                      color="#02C39A"
                      style="color: white"
                      rounded
                      @click="loader = 'loading'"
              >
                <span class="font-weight-black">Login</span>
              </v-btn>
            </v-form>
          </transition>
        </v-col>
        <v-col cols="12" md="6">
          <v-img
                  src="../assets/svgs/sign-in.svg"
                  class="mr-5"
                  max-width="600px"
          ></v-img>
        </v-col>
      </v-row>
      <v-spacer></v-spacer>
    </v-container>
  </v-content>
</template>

<script>
  import { mapGetters } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      usernameRules: [
        value => !!value || "Username is required.",
      ],
      passwordRules: [value => !!value || "Password is required."]
    };
  },
  computed: {
    ...mapGetters({
      user: "getUser",
      loading: "loading",
    })
  },
  watch: {
    // user(value) {
    //   // TODO: Validation
    //   return true
    // }
  },
  methods: {
    login() {
      let username = this.username;
      let password = this.password;
      this.$store
        .dispatch("login", { username, password })
        .then(() => this.$router.push({ name: "Home" }))
        .catch(err => console.log(err));
    }
  }
};
</script>

<style>
  .slide-up-enter {
    transform: translateY(40px);
    opacity: 1;
  }
  .slide-up-enter-active {
    transition: all 0.4s ease-out;
  }
  .slide-up-move {
    transition: transform 0.3s ease-out;
  }
  .text--gray {
    color: #525252;
  }

  @media (min-width: 600px) {
    .header-container {
      background: #fff url("../assets/svgs/bg-hero.svg") no-repeat;
      width: 100%;
      background-position: 100wh;
      background-size: cover;
      height: calc(100vh - 72px);
    }
  }
</style>
