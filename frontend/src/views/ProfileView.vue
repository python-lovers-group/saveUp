<template>
  <v-app>
    <v-app-bar app color="#02c39a" dark elevation="0">
      <v-app-bar-nav-icon
        @click.stop="sidebarMenu = !sidebarMenu"
      ></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-icon>mdi-account</v-icon>
    </v-app-bar>
    <v-navigation-drawer
      v-model="sidebarMenu"
      color="#385F73"
      hide-overlay
      app
      floating
      :permanent="sidebarMenu"
      :mini-variant.sync="mini"
    >
      <v-list-item class="px-2" @click="toggleMini = !toggleMini">
        <v-list-item-avatar>
          <v-icon dark>mdi-account-outline</v-icon>
        </v-list-item-avatar>
        <v-list-item-content class="text-white">
          {{ user.username }}
        </v-list-item-content>
        <v-btn icon small>
          <v-icon dark color="white">mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.href"
        >
          <v-list-item-icon>
            <v-icon dark v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title
              class="text-white"
              v-text="item.title"
            ></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <v-container fluid>
        <v-row class="fill-height">
          <v-col>
            <transition name="slide">
              <router-view></router-view>
            </transition>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
    <v-footer>
      Footer
    </v-footer>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "ProfileView",
  data() {
    return {
      sidebarMenu: true,
      toggleMini: false,
      items: [
        { title: "Dashboard", href: "/profile", icon: "mdi-home-outline" },
        {
          title: "Detections",
          href: "/detections",
          icon: "mdi-shield-account"
        },
        { title: "Components", href: "/comp", icon: "mdi-palette-swatch" },
        { title: "Customers", href: "/customers", icon: "mdi-account" },
        { title: "Orders", href: "/orders", icon: "mdi-bus-clock" },
        { title: "Settings", href: "/settings", icon: "mdi-settings-outline" }
      ]
    };
  },
  beforeCreate() {
    this.$store.dispatch("getBilling");
  },
  watch: {
    message(value) {
      window.Swal.fire({
        icon: "success",
        text: value
      });
    },

    error(value) {
      window.Swal.fire({
        icon: "error",
        text: value
      });
    }
  },
  computed: {
    ...mapGetters({
      user: "getUser",
      loading: "loading",
      message: "getMessage",
      billing: "billing",
      error: "getError"
    }),

    mini() {
      return this.$vuetify.breakpoint.smAndDown || this.toggleMini;
    }
  }
};
</script>

<style scoped></style>
