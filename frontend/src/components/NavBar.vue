<template>
  <nav class="navbar navbar-expand-lg navbar-light">
    <img class="navbar-brand ml-5" src="../assets/svgs/logo.svg">
    <v-spacer></v-spacer>
    <v-spacer></v-spacer>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-item nav-main" href="#">Products</a>
        <a class="nav-item nav-main" href="#">About us</a>
        <a class="nav-item nav-main" href="#">Help</a>
      </div>
      <v-btn rounded color="#02C39A" class="nav-btn" dark>Get Started</v-btn>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar"
};
</script>

<style scoped>
  .nav-main {
    font-weight: 800;
    font-size: 18px;
    color: #00A896;
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
