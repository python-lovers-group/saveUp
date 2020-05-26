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
        <v-col cols="12">
          <div class="ml-5">
            <slot></slot>
          </div>
        </v-col>
      </v-row>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: "Card"
};
</script>

<style scoped></style>
