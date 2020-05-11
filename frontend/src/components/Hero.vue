<template>
  <v-content>
    <v-container fill-height fluid>
      <v-row class="pt-12">
        <v-col cols="12" sm="2"></v-col>
        <v-col cols="12" sm="4" class="mt-auto">
          <h4 class="display-2 font-weight-bold hero-title pt-12">Manage your billings with us!</h4>
          <h6 class="title font-weight-bold hero-subtitle">
            Keep in touch with your friends.
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
</style>
