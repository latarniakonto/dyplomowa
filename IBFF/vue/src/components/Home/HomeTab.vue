<template>
  <div class="home-tab">
    <PortfolioDashboard />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";

export default defineComponent({
  name: "HomeTab",

  components: {
    PortfolioDashboard,
  },

  data() {
    return {};
  },

  methods: {},
});
</script>

<style>
</style>
