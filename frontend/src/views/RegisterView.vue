<template>
  <div>
    <NavBar />
    <Register />
  </div>
</template>

<script>
import NavBar from "../components/NavBar";
import Register from "../components/Register";
export default {
  name: "RegisterView",
  components: { Register, NavBar }
};
</script>

<style scoped></style>
