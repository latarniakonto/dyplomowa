<template>
  <Dialog
    :visible="analyzeAssetDialog"
    :style="{ width: '60rem' }"
    :modal="true"
    @update:visible="cancelAssetAnalysis()"
  >
    <template #header>
      <h3>{{ asset.ticker }}</h3>
    </template>
    <AssetInfo :asset="asset"/>
    <OperationsTable/>
    <TransactionsTable/>
  </Dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import InputNumber from "primevue/inputnumber";
import TransactionsTable from "./TransactionsTable.vue";
import OperationsTable from "./OperationsTable.vue";
import AssetInfo from "./AssetInfo.vue";

export default defineComponent({
  name: "AnalyzeAssetDialog",

  components: {
    Button,
    Dialog,
    InputNumber,
    TransactionsTable,
    OperationsTable,
    AssetInfo
  },

  props: {
    analyzeAssetDialog: {
      required: true,
      type: Boolean,
      default: false,
    },
    asset: {
      required: true,
      type: Object,
      default: {},
    },
  },

  emits: {
    assetAnalysisCanceled: () => true,
  },

  data() {
    return {
    };
  },

  methods: {
    cancelAssetAnalysis() {
      this.$emit("assetAnalysisCanceled");
    },
  },
});
</script>

<style>
</style>
