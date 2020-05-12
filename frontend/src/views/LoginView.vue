<template>
  <div>
    <NavBar />
    <Login />
  </div>
</template>

<script>
  import NavBar from "../components/NavBar";
  import Login from "../components/Login";
  export default {
    name: "LoginView",
    components: {Login, NavBar}
  }
</script>

<style scoped>

</style>