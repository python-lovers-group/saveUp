<template>
  <section class="green-wave">
    <v-row class="pt-12">
      <v-col cols="12" md="1"></v-col>
      <v-col cols="12" md="6" class="getting-started-icons">
        <v-img
          src="../assets/svgs/getting-started-icons-1.svg"
          max-width="600px"
        ></v-img>
        <v-img
          src="../assets/svgs/getting-started-icons-2.svg"
          max-width="600px"
        ></v-img>
      </v-col>
      <v-col cols="12" md="5" class="getting-started-text">
        <h4 class="display-1 font-weight-bold white--text ml-5 mt-5">
          Getting started
        </h4>
        <h6 class="subtitle-1 font-weight-bold text-white ml-5">
          <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
          Class aptent taciti sociosqu ad litora torquent per conubia nostra.
        </h6>
        <h6 class="subtitle-1 font-weight-bold text-white ml-5">
          <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
          per inceptos himenaeos. Interdum et malesuada fames ac ante.
        </h6>
        <h6 class="subtitle-1 font-weight-bold text-white ml-5">
          <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
          per inceptos himenaeos. Interdum et malesuada fames ac ante.
        </h6>
      </v-col>
    </v-row>
  </section>
</template>

<script>
export default {
  name: "GetStarted"
};
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

.getting-started-icons {
  top: 12rem;
}

.getting-started-text {
  top: 18rem;
  right: 0;
}
</style>
