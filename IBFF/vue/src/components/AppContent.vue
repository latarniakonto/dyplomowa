<template>
  <div class="container app-content mt-3">
    <TabMenu :model="items" class="mb-3" />
    <TransactionsTab />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";
import AssetsTable from "./AssetsTable.vue";
import TabMenu from "primevue/tabmenu";
import OperationsTab from "./OperationsTab.vue";
import TransactionsTab from "./Transactions/TransactionsTab.vue";

export default defineComponent({
  name: "AppContent",

  components: {
    PortfolioDashboard,
    AssetsTable,
    TabMenu,
    OperationsTab,
    TransactionsTab,
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
  height: 48rem;
  background: white;
  padding: 1rem;
  padding-top: 0rem;
  padding-bottom: 0rem;
  border-radius: 4px;
  overflow: auto;
}
</style>
