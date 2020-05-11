<template>
  <v-content>
    <v-container fill-height fluid class="header-container">
      <v-row>
        <v-col cols="12" md="2"></v-col>
        <v-col cols="12" md="4" class="pt-12">
          <h4 class="display-3 font-weight-bold hero-title">
            Manage your billings with us!
          </h4>
          <h6 class="title font-weight-bold hero-subtitle mt-0">
            Learn how to save your money.
          </h6>
          <v-btn
                  rounded
                  color="#02C39A"
                  elevation="3"
                  dark
          ><span class="font-weight-black">Join us!</span></v-btn
          >
          <v-btn
                  rounded
                  outlined
                  color="#02C39A"
                  style="margin-left: 1rem"
                  elevation="3"
                  dark
          ><span class="font-weight-black">Learn more</span></v-btn
          >
        </v-col>
        <v-col cols="12" md="5" class="mt-5">
          <v-img
                  src="../assets/svgs/main-banner.svg"
                  class="mr-5"
                  max-width="500px"
          ></v-img>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
export default {
  name: "Hero"
};
</script>

<style scoped>
  .hero-title {
    color: #02C39A;
  }

  .hero-subtitle {
    color: #00A896;
  }

  .header-container {
    background: #fff url("../assets/svgs/bg-hero.svg") no-repeat;
    /*background-position: 1--wh;*/
    /*background-size: contain;*/
    height: calc(100vh - 72px);
  }
</style>
