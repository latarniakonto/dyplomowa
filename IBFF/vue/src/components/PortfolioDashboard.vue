<template>
  <div class="portfolio-dashboard">
    <div class="dashboard-header">
      <h4 class="mb-3">Portfolio name</h4>
    </div>
    <div class="dashboard-content">
      <div class="d-inline-block">
        <ResourcesInfo class="mr-4 mb-3" />
        <FeesInfo class="mr-4 mb-3" />
        <ChartsInfo />
      </div>
      <div class="d-inline-block align-top">
        <PerformanceInfo />
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

export default defineComponent({
  name: "PortfolioDashboard",

  components: {
    ResourcesInfo,
    FeesInfo,
    ChartsInfo,
    PerformanceInfo
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
