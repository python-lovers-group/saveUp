<template>
  <div class="home">
    <NavBar />
    <Hero />
    <GetStarted />
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "../components/NavBar";
import Hero from "../components/Hero";
import GetStarted from "../components/GetStarted";
import Footer from "../components/Footer";

export default {
  name: "Home",
  components: {
    Footer,
    GetStarted,
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
