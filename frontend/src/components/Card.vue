<template>
  <v-hover v-slot:default="{ hover }">
    <v-card
            color="#385F73"
            max-width="400px"
            :elevation="hover ? 15 : 3"
            :class="{ 'on-hover': hover }"
            dark
    >
      <v-row class="align-center">
        <v-col cols="2">
          <slot name="icon"></slot>
        </v-col>
        <v-col cols="9">
          <div class="pt-3 pl-3 pr-3 pb-1">
            <slot name="content"></slot>
          </div>
        </v-col>
      </v-row>

    </v-card>
  </v-hover>
</template>

<script>
  export default {
    name: "Card"
  }
</script>

<style scoped>
</style>