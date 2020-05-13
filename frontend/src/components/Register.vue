<template>
  <v-content>
    <v-container fill-height fluid class="header-container">
      <v-row>
        <v-col cols="12" sm="1"></v-col>
        <v-col cols="12" md="4" class="">
          <h6 class="text--secondary subtitle-1">
            Create your account and join us!
          </h6>
          <transition name="slide-up" appear>
            <v-form class="pr-2" ref="signUpForm" @submit.prevent="register">
              <v-text-field
                v-model="username"
                label="Username"
                type="text"
                :rules="usernameRules"
                required
              ></v-text-field>
              <v-text-field
                v-model="email"
                label="Email"
                type="email"
                :rules="emailRules"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                :rules="passwordRules"
                required
              ></v-text-field>
              <v-checkbox
                v-model="agreeToTerms"
                label="Agree to terms & conditions"
                class="mt-2"
                :rules="agreeToTermsRules"
              ></v-checkbox>
              <p class="caption">
                Already have an account?
                <router-link :to="{ name: 'Login' }">Log in!</router-link>
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
                <span class="font-weight-black">CREATE AN ACCOUNT</span>
              </v-btn>
            </v-form>
          </transition>
        </v-col>
        <v-col cols="12" md="6">
          <v-img
            src="../assets/svgs/register.svg"
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
  name: "Register",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      password2: "",
      agreeToTerms: false,
      is_admin: null,
      usernameRules: [value => !!value || "Username is required."],
      passwordRules: [value => !!value || "Password is required."],
      emailRules: [
        value => !!value || "Email address is required.",
        value => value.indexOf("@") !== 0 || "Email is invalid.",
        value => value.includes("@") || "Email should include and @ symbol."
      ],
      agreeToTermsRules: [
        value =>
          !!value ||
          "You must agree to the terms and conditions to sign up for an account."
      ]
    };
  },
  methods: {
    register: function() {
      let data = {
        username: this.username,
        email: this.email,
        password: this.password
      };
      this.$store
        .dispatch("register", data)
        .then(() => {
          window.Toast.fire({
            icon: "success",
            title: this.message
          });
          this.$router.push({ name: "Login" });
        })
        .catch(err => {
          window.Swal.fire({
            icon: "error",
            title: "Oops...",
            text:
              "Something went wrong! Please try register your account one more time!"
          });
          console.log(err);
        });
    }
  },
  computed: {
    ...mapGetters({
      user: "getUser",
      loading: "loading",
      error: "getError",
      message: "getMessage"
    })
  }
};
</script>

<style scoped></style>
