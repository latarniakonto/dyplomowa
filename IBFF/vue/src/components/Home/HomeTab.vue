<template>
  <div class="home-tab">
    <PortfolioDashboard :portfolio="portfolios[0]" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";
import { Portfolio, PortfolioJSON } from "../../common/models";
import { axios } from "../../common/api.service";

export default defineComponent({
  name: "HomeTab",

  components: {
    PortfolioDashboard,
  },

  props: {
  },

  data() {
    return {
      portfolios: [] as Array<Portfolio>
    };
  },

  methods: {
    async getPortfolios() {
      let endpoint = "api/v1/portfolios/";

      try {
        let response = await axios.get(endpoint);
        let jsons = response.data as PortfolioJSON[];
        this.portfolios.push(new Portfolio(jsons[0]));
      } catch (e: any) {
        console.error(e.response);
      }
    },
  },

  created() {
    this.getPortfolios();
  },
});
</script>

<style>
</style>
