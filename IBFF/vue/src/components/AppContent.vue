<template>
  <div class="container app-content mt-3">
    <TabMenu :model="items" class="mb-3"/>
    <AssetsTable/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";
import AssetsTable from "./AssetsTable.vue";
import TabMenu from "primevue/tabmenu";

export default defineComponent({
  name: "AppContent",

  components: {
    PortfolioDashboard,
    AssetsTable,
    TabMenu,
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
});
</script>

<style>
.app-content {
  display: block;
  height: 47rem;
  background: white;
  padding: 1rem;
  border-radius: 4px;
}
</style>
