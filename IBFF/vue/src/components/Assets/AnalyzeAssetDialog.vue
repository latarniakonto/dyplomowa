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
    <AssetInfo :asset="asset" v-bind="$attrs" />
    <OperationsPanel :operations="operations" />
    <TransactionsPanel :transactions="transactions" />
  </Dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import InputNumber from "primevue/inputnumber";
import TransactionsPanel from "./TransactionsPanel.vue";
import OperationsPanel from "./OperationsPanel.vue";
import AssetInfo from "./AssetInfo.vue";
import { Asset, Transaction, Dividend } from "../../common/models";

export default defineComponent({
  name: "AnalyzeAssetDialog",

  components: {
    Button,
    Dialog,
    InputNumber,
    TransactionsPanel,
    OperationsPanel,
    AssetInfo,
  },

  props: {
    analyzeAssetDialog: {
      required: true,
      type: Boolean,
      default: false,
    },
    asset: {
      type: Object as () => Asset,
      required: true,
      default: {},
    },
    transactions: {
      type: Array as () => Array<Transaction>,
      required: true,
      default: {}
    },
    operations: {
      type: Array as () => Array<Dividend>,
      required: true,
      default: {}
    }
  },

  emits: {
    assetAnalysisCanceled: () => true,
  },

  data() {
    return {};
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
