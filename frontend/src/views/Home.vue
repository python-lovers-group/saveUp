<template>
  <div class="home">
    <NavBar />
    <Hero />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "../components/NavBar";
import Hero from "../components/Hero";

export default {
  name: "Home",
  components: {
    Hero,
    NavBar
  }
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
}
</style>
