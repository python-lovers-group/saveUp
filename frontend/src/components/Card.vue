<template>
  <div class="card text-white mb-1 info-card my-card">
    <div class="card-header">
      <h4 class="text-white text-center text-capitalize title">{{title}}</h4>
    </div>
    <div class="card-body text-center">
      <h2 class="font-weight-bold display-1">{{value}}</h2>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Card",
    props: {
      title: {
        type: String,
        required: true,
        default: "Title"
      },
      value: {
        type: String,
        required: true,
        default: "Value"
      }
    }
  }
</script>

<style scoped>
.my-card {
  background: linear-gradient(192.9deg, #00A896 -4.02%, rgba(255, 255, 255, 0) 119.96%), #02C39A;
  box-shadow: 8px 8px 8px rgba(0, 0, 0, 0.25);
  border-radius: 21px;
  margin-left: 1rem;
  margin-right: 1rem;
  max-width: 400px;
}
</style>