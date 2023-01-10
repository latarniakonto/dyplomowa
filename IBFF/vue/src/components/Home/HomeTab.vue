<template>
  <div class="home-tab">
    <PortfolioDashboard :portfolio="$store.state.portfolio" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";
import { Portfolio } from "../../common/models";

export default defineComponent({
  name: "HomeTab",

  components: {
    PortfolioDashboard,
  },

  data() {
    return {
      portfolio: new Object() as Portfolio
    };
  },

  methods: {
  },
});
</script>

<style>
</style>
