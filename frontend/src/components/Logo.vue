<template>
  <img
    class="navbar-brand ml-5"
    style="cursor: pointer"
    @click="reconnectToHome"
    src="../assets/svgs/logo.svg"
  />
</template>

<script>
export default {
  name: "Logo",
  methods: {
    reconnectToHome() {
      this.$router.push({ name: "Home" });
    }
  }
};
</script>

<style scoped></style>
