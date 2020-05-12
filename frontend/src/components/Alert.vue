<template>
  <v-alert border="right" colored-border type="error" elevation="2">
    <v-row>
      // TODO: Stylize ALERT box.
      <v-col class="grow">{{ error }}</v-col>
      <v-col class="shrink">
        <v-btn icon @click="clearError" class="float-right"
          ><v-icon>mdi-close</v-icon></v-btn
        >
      </v-col>
    </v-row>
  </v-alert>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Alert",
  computed: {
    ...mapGetters({
      error: "getError"
    })
  },
  methods: {
    clearError() {
      this.$store.dispatch("clearError");
    }
  }
};
</script>

<style scoped></style>
