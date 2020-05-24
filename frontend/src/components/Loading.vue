<template>
  <div>Loading</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Loading",
  computed: {
    ...mapGetters({
      loading: "loading"
    })
  }
};
</script>

<style scoped></style>
