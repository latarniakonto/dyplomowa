<template>
  <div class="home-tab">
    <PortfolioDashboard :portfolio="portfolio" />
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

  props: {
    portfolio: {
      type: Object as () => Portfolio,
      required: true,
      default: {}
    }
  },

  data() {
    return {};
  },

  methods: {},
});
</script>

<style>
</style>
