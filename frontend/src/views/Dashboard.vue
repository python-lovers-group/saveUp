<template>
  <v-container>
    <v-row>
      <v-col :md="6" :sm="12" :xs="12">
        <v-card
                color="#385F73"
                max-width="500px"
                elevation="5"
                dark
        >
          <v-card-title class="display-1 font-weight-bold justify-content-center">My ballance</v-card-title>

          <div class="display-2 font-weight-medium text-center">
            ${{billing.total_bills}}
          </div>

          <v-card-actions>
            <v-btn class="overline" text>Details</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col :md="6" :sm="12" :xs="12">
        <v-card
                color="#385F73"
                max-width="500px"
                elevation="5"
                dark
        >
          <v-card-title class="display-1 font-weight-bold justify-content-center">Daily total</v-card-title>

          <div class="display-2 font-weight-medium text-center">
            ${{dailyTotal}}
          </div>

          <v-card-actions>
            <v-btn class="overline" text>Details</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import {mapGetters} from "vuex";

  export default {
    name: "Dashboard",
    computed: {
      ...mapGetters({
        user: "getUser",
        loading: "loading",
        message: "getMessage",
        billing: "billing",
      }),

      dailyTotal() {
        let result = 0;
        this.billing.total_daily.forEach(item => result += item.price);
        return result;
      },
    },
  }
</script>

<style scoped>

</style>