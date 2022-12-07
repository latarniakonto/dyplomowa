<template>
  <div class="container app-content mt-3">
    <TabMenu :model="items" class="mb-3" />
    <SnapshotsTab />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AssetsTable from "./AssetsTable.vue";
import TabMenu from "primevue/tabmenu";
import OperationsTab from "./OperationsTab.vue";
import TransactionsTab from "./Transactions/TransactionsTab.vue";
import SnapshotsTab from "./Snapshots/SnapshotsTab.vue";
import HomeTab from "./Home/HomeTab.vue";

export default defineComponent({
  name: "AppContent",

  components: {
    AssetsTable,
    TabMenu,
    OperationsTab,
    TransactionsTab,
    SnapshotsTab,
    HomeTab
  },

  data() {
    return {
      items: [
        { label: "Home", icon: "bi bi-house" },
        { label: "Assets", icon: "bi bi-wallet2" },
        { label: "Transactions", icon: "bi bi-cash-coin" },
        { label: "Operations", icon: "bi bi-boxes" },
        { label: "Snapshots", icon: "bi bi-camera" },
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
