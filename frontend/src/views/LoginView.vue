<template>
  <div>
    <NavBar />
    <Login />
    <Footer />
  </div>
</template>

<script>
import NavBar from "../components/NavBar";
import Login from "../components/Login";
import Footer from "../components/Footer";
export default {
  name: "LoginView",
  components: {Footer, Login, NavBar }
};
</script>

<style scoped></style>
