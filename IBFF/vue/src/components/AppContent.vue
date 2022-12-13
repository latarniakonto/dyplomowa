<template>
  <div class="container app-content mt-3">
    <TabMenu :model="items" class="mb-3" />
    <HomeTab :portfolio="portfolios[0]" v-if="content === 'Home'" />
    <AssetsTab v-if="content === 'Assets'" />
    <TransactionsTab v-if="content === 'Transactions'" />
    <OperationsTab v-if="content === 'Operations'" />
    <SnapshotsTab v-if="content === 'Snapshots'" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import TabMenu from "primevue/tabmenu";
import OperationsTab from "./Operations/OperationsTab.vue";
import TransactionsTab from "./Transactions/TransactionsTab.vue";
import SnapshotsTab from "./Snapshots/SnapshotsTab.vue";
import HomeTab from "./Home/HomeTab.vue";
import AssetsTab from "./Assets/AssetsTab.vue";
import { axios } from "../common/api.service";
import { Portfolio, PortfolioJSON } from "../common/models";

export default defineComponent({
  name: "AppContent",

  components: {
    TabMenu,
    OperationsTab,
    TransactionsTab,
    SnapshotsTab,
    HomeTab,
    AssetsTab,
  },

  props: {
    content: {
      type: String,
      required: true,
      default: "",
    },
  },

  data() {
    return {
      items: [
        { label: "Home", icon: "bi bi-house", to: "/" },
        { label: "Assets", icon: "bi bi-wallet2", to: "/assets" },
        { label: "Transactions", icon: "bi bi-cash-coin", to: "/transactions" },
        { label: "Operations", icon: "bi bi-boxes", to: "/operations" },
        { label: "Snapshots", icon: "bi bi-camera", to: "/snapshots" },
      ],
      portfolios: [] as Array<Portfolio>,
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
