<template>
  <div class="portfolio-dashboard">
    <div class="dashboard-header">
      <h4 class="mb-3">{{ portfolio.name }}</h4>
    </div>
    <div class="dashboard-content">
      <div class="d-inline-block">
        <ResourcesInfo :portfolio="portfolio" class="mr-4 mb-3" />
        <FeesInfo :portfolio="portfolio" class="mr-4 mb-3" />
        <ChartsInfo />
      </div>
      <div class="d-inline-block align-top">
        <PerformanceInfo :portfolio="portfolio" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ResourcesInfo from "./ResourcesInfo.vue";
import FeesInfo from "./FeesInfo.vue";
import ChartsInfo from "./ChartsInfo.vue";
import PerformanceInfo from "./PerformanceInfo.vue";
import { Portfolio } from "../../common/models";

export default defineComponent({
  name: "PortfolioDashboard",

  components: {
    ResourcesInfo,
    FeesInfo,
    ChartsInfo,
    PerformanceInfo
  },

  props: {
    portfolio: {
      type: Object as () => Portfolio,
      required: true,
      default: {}
    }
  },

  data() {
    return {
      items: [
        { label: "Home", icon: "bi bi-house" },
        { label: "Assets", icon: "bi bi-wallet2" },
        { label: "Transactions", icon: "bi bi-cash-coin" },
        { label: "Operations", icon: "bi bi-boxes" },
      ],
    };
  },

  methods: {
  },
});
</script>

<style>
.portoflio-dashboard {
  display: flex;
}
</style>
