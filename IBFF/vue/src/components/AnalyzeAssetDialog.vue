<template>
  <Dialog
    :visible="analyzeAssetDialog"
    :style="{ width: '60rem' }"
    :header="asset.ticker"
    :modal="true"
    @update:visible="cancelAssetAnalysis()"
  >
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

export default defineComponent({
  name: "AnalyzeAssetDialog",

  components: {
    Button,
    Dialog,
    InputNumber,
    TransactionsTable,
    OperationsTable,
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
