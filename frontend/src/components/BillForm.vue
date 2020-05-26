<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <transition name="slide-up" appear>
        <v-form class="pr-2 mx-10" ref="billForm" @submit.prevent="addBill">
          <v-row>
            <v-col>
              <v-text-field
                v-model="where"
                label="Localization"
                type="text"
                :rules="whereRules"
                required
              ></v-text-field>
              <v-text-field
                v-model="price"
                label="Price"
                type="number"
                :rules="priceRules"
                required
              ></v-text-field>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  type="submit"
                  class="ma-2"
                  color="#02C39A"
                  style="color: white"
                  rounded
                >
                  <span class="font-weight-black">Add</span>
                </v-btn>
              </v-card-actions>
            </v-col>
          </v-row>
        </v-form>
      </transition>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "BillForm",
  data: () => ({
    dialog: false,
    where: "",
    whereRules: [value => !!value || "You must specify localization."],
    price: 0,
    priceRules: [value => value > 0 || "Price must be greater than 0!"]
  }),
  computed: {
    ...mapGetters({
      user: "getUser",
      loading: "loading",
      message: "getMessage",
      billing: "billing"
    })
  },
  methods: {
    addBill() {
      this.dialog = false;
    }
  }
};
</script>

<style scoped></style>
