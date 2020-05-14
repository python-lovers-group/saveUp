<template>
  <v-content>
    <v-container fluid class="header-container">
      <v-row>
        <v-col cols="12" md="1"></v-col>
        <v-col cols="12" md="3">
          <Card title="My Balance" value="$821.47" />
        </v-col>
        <v-col cols="12" md="3">
          <Card title="My Balance" value="$821.47" />
        </v-col>
        <v-col cols="12" md="3">
          <Card title="My Balance" value="$821.47" />
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
  import {mapGetters} from "vuex";
  import Card from "../components/Card";

  export default {
    name: "ProfileView",
    components: {Card},
    data() {
      return {}
    },
    computed: {
      ...mapGetters({
        user: "getUser",
        loading: "loading",
        message: "getMessage"
      })
    }
  }
</script>

<style scoped>

</style>