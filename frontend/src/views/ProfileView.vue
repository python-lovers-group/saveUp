<template>
  <v-content>
    <v-container fluid class="header-container">
      <v-row>
        <v-spacer></v-spacer>
        <v-col cols="12" md="3">
          <Logo />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="1"></v-col>
        <v-col cols="12" md="3">
          <span class="font-weight-bold title">{{user.username}}</span>
          <br>
          <span class="subtitle-2 text-secondary">{{user.email}}</span>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="1"></v-col>
        <v-col cols="12" md="3">
          <Card title="My Balance" value="$821.47" />
        </v-col>
        <v-col cols="12" md="3">
          <Card title="Total spent" value="$13.25" />
        </v-col>
        <v-col cols="12" md="3">
          <Card title="Daily limit" value="$350" />
        </v-col>
      </v-row>

    </v-container>


    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on }">
          <v-btn class="mx-2 add-icon" fab dark color="#02C39A" v-on="on">
            <v-icon dark>mdi-plus</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">Add new bill</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field label="Price*" required></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field label="Description" required></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field label="Where" required></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-autocomplete
                          :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                          label="Categories"
                          multiple
                  ></v-autocomplete>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
            <v-btn rounded color="#02C39A" elevation="3" dark text @click="addBill">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

  </v-content>
</template>

<script>
  import {mapGetters} from "vuex";
  import Card from "../components/Card";
  import Logo from "../components/Logo";

  export default {
    name: "ProfileView",
    components: {Card, Logo},
    data() {
      return {
        dialog: false,
      }
    },
    computed: {
      ...mapGetters({
        user: "getUser",
        loading: "loading",
        message: "getMessage"
      })
    },
    methods: {
      addBill() {
        this.dialog = false;
      }
    }

  }
</script>

<style scoped>
.add-icon {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
}
</style>