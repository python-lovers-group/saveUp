<template>
  <div>
    <NavBar />
    <Register />
    <Footer />
  </div>
</template>

<script>
import NavBar from "../components/NavBar";
import Register from "../components/Register";
import Footer from "../components/Footer";
export default {
  name: "RegisterView",
  components: {Footer, Register, NavBar }
};
</script>

<style scoped></style>
