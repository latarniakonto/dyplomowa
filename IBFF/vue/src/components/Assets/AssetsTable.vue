<template>
  <div class="assets-table">
    <div class="card" style="">
      <div class="table-data">
        <DataTable
          ref="dt"
          :value="assets"
          dataKey="id"
          :paginator="true"
          :rows="5"
          paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rowsPerPageOptions="[5, 10]"
          currentPageReportTemplate="Showing {first} to {last} of {totalRecords} assets"
          :scrollable="true"
        >
          <Column
            field="ticker"
            header="Ticker"
            :sortable="true"
            style="min-width: 2rem"
          ></Column>
          <Column
            field="total"
            header="Total"
            :sortable="true"
            style="min-width: 2rem"
          ></Column>
          <Column
            field="initialPrice"
            header="Initial Price"
            :sortable="true"
            style="min-width: 3rem"
          >
          </Column>
          <Column
            field="currentPrice"
            header="Current Price"
            :sortable="true"
            style="min-width: 3rem"
          ></Column>
          <Column
            field="gain"
            header="Profit/Loss"
            :sortable="true"
            style="min-width: 8rem"
          >
            <template #body="slotProps">
              {{ getPrintablePercantage(slotProps.data.gain) }}
            </template>
          </Column>
          <Column
            field="initialWeight"
            header="Initial Weight"
            :sortable="true"
            style="min-width: 3rem"
          >
            <template #body="slotProps">
              {{ getPrintablePercantage(slotProps.data.initialWeight) }}
            </template>
          </Column>
          <Column
            field="currentWeight"
            header="Current Weight"
            :sortable="true"
            style="min-width: 3rem"
          >
            <template #body="slotProps">
              {{ getPrintablePercantage(slotProps.data.currentWeight) }}
            </template>
          </Column>
          <Column style="min-width: 1rem">
            <template #body="slotProps">
              <button
                type="button"
                class="btn btn-warning btn-sm mr-1"
                @click="analazyAsset(slotProps.data, slotProps.index)"
              >
                <i class="bi bi-info-circle"></i>
              </button>
            </template>
          </Column>
        </DataTable>
      </div>
    </div>
    <div class="table-crud">
      <AnalyzeAssetDialog
        :analyzeAssetDialog="analazyAssetDialog"
        :asset="asset"
        :transactions="assetTransactions"
        @asset-analysis-canceled="handleAssetAnalysisCanceled()"
        v-bind="$attrs"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Row from "primevue/row";
import Button from "primevue/button";
import Toolbar from "primevue/toolbar";
import AnalyzeAssetDialog from "./AnalyzeAssetDialog.vue";
import {
  Asset,
  Transaction,
  TransactionJSON,
  getPrintablePercantage
} from "../../common/models";
import { axios } from "../../common/api.service";

export default defineComponent({
  name: "AssetsTable",

  components: {
    DataTable,
    Column,
    Row,
    Button,
    Toolbar,
    AnalyzeAssetDialog,
  },

  props: {
    assets: {
      type: Array as () => Array<Asset>,
      required: true,
      default: [],
    },
  },

  data() {
    return {
      analazyAssetDialog: false as Boolean,
      asset: {} as Asset,
      assetTransactions: [] as Array<Transaction>,
    };
  },

  methods: {
    analazyAsset(asset: Asset, index?: number) {
      this.asset = asset;
      this.asset.index = index;
      this.getAssetTransactions();
      this.analazyAssetDialog = true;
    },

    handleAssetAnalysisCanceled() {
      this.analazyAssetDialog = false;
    },

    async getAssetTransactions() {
      let endpoint = `api/v1/assets/${this.asset.slug}/transactions/`;
      this.assetTransactions = [];

      try {
        let response = await axios.get(endpoint);
        let jsons = response.data;
        jsons.forEach((json: any) => {
          this.assetTransactions.push(new Transaction(json as TransactionJSON));
        });
      } catch (e: any) {
        console.error(e.response);
      }
    },

    getPrintablePercantage
  },
});
</script>

<style>
.assets-table .table-toolbar {
  background-color: #f6f6f6;
  height: 60px;
}

.table-toolbar .p-toolbar {
  background-color: #f6f6f6;
  border-color: #a4a4a4;
  padding: 0.3rem 0 0 0.3rem;
}

.p-datatable-tbody {
  min-height: 27.2rem;
  max-height: 27.2rem;
}

.table-data .p-datatable .p-datatable-thead tr th {
  justify-content: end;
  background-color: #f6f6f6;
}

.table-data .p-datatable .p-datatable-tbody tr td {
  justify-content: end;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.assets-table .card {
  border-color: #a4a4a4;
}

.p-datatable .p-paginator {
  background: #f6f6f6;
}
</style>
