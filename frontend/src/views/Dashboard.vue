<template>
  <v-container>
    <v-row>
      <v-col :md="4" :sm="12" :xs="12">
        <Card>
          <template v-slot:icon>
            <v-btn class="mx-2 ml-4" fab dark color="teal">
              <v-icon dark>mdi-cash-usd</v-icon>
            </v-btn>
          </template>
          <template v-slot:content>
            <span class="font-weight-light display-2 mr-2">$200</span><span class="headline font-weight-light">My Ballance</span>
            <p class="font-weight-light">It's $20 below your limit!</p>
          </template>
        </Card>
      </v-col>
      <v-col :md="4" :sm="12" :xs="12">
        <Card>
          <template v-slot:icon>
            <v-btn class="mx-2 ml-4" fab dark color="teal">
              <v-icon dark>mdi-cash-usd</v-icon>
            </v-btn>
          </template>
          <template v-slot:content>
            <span class="font-weight-light display-2 mr-2">$200</span><span class="headline font-weight-light">My Ballance</span>
            <p class="font-weight-light">It's $20 below your limit!</p>
          </template>
        </Card>
      </v-col>
      <v-col :md="4" :sm="12" :xs="12">
        <Card>
          <template v-slot:icon>
            <v-btn class="mx-2 ml-4" fab dark color="teal">
              <v-icon dark>mdi-cash-usd</v-icon>
            </v-btn>
          </template>
          <template v-slot:content>
            <span class="font-weight-light display-2 mr-2">$200</span><span class="headline font-weight-light">My Ballance</span>
            <p class="font-weight-light">It's $20 below your limit!</p>
          </template>
        </Card>
      </v-col>
      <BillForm />
    </v-row>
  </v-container>
</template>

<script>
  import {mapGetters} from "vuex";
  import BillForm from "../components/BillForm";
  import Card from "../components/Card";

  export default {
    name: "Dashboard",
    components: {Card, BillForm},
    data: () => ({
      dialog: false,
    }),
    computed: {
      ...mapGetters({
        user: "getUser",
        loading: "loading",
        message: "getMessage",
        billing: "billing",
      }),

    },
  }
</script>

<style scoped>
</style>