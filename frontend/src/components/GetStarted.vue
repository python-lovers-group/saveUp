<template>
  <div>
    <section class="green-wave"></section>
<!--    <section class="wave"></section>-->
    <section></section>
  </div>
</template>

<script>
  export default {
    name: "GetStarted"
  }
</script>

<style scoped>
  section {
    width: 100%;
    min-height: 1500px;
  }

  @media (min-width: 960px) {
    .green-wave {
      position: relative;
      top: -200px;
      left: 0;
      width: 100%;
      height: 280px;
      background: url("../assets/svgs/green-bg-full.svg");
      background-color: transparent;
      background-size: cover;
      background-repeat: no-repeat;
    }
  }

  @media (max-width: 960px) {
    .green-wave {
      position: relative;
      top: 0px;
      left: 0;
      width: 100%;
      height: 280px;
      background: url("../assets/svgs/green-bg-full.svg");
      background-color: transparent;
      background-size: cover;
      background-repeat: no-repeat;
    }
  }

  .wave {
    position: relative;
    background: linear-gradient(90deg, #f0027f, #75489f);
  }
  .wave:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 280px;
    background: url("../assets/svgs/wave.svg");
    background-color: transparent;
    background-size: cover;
    background-repeat: no-repeat;
  }
</style>