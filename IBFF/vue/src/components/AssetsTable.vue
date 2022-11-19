<template>
  <div class="assets-table mt-5">
    <div class="card" style="">
      <div class="table-toolbar">
        <Toolbar class="mb-4">
          <template #start>
            <Button
              label="New"
              icon="pi pi-plus"
              class="p-button-success mr-2"
              @click="createTransaction()"
            />
          </template>
        </Toolbar>
      </div>
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
            field="buyPrice"
            header="Buy Price"
            :sortable="true"
            style="min-width: 3rem"
          >
            <!-- <template #body="slotProps">
              {{ formatCurrency(slotProps.data.price) }}
            </template> -->
          </Column>
          <Column
            field="initialWeight"
            header="Initial Weight"
            :sortable="true"
            style="min-width: 3rem"
          ></Column>
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
          ></Column>
          <Column
            field="currentWeight"
            header="Current Weight"
            :sortable="true"
            style="min-width: 3rem"
          ></Column>
          <Column style="min-width: 1rem">
            <template #body="slotProps">
              <button type="button" class="btn btn-warning btn-sm mr-1">
                <i class="bi bi-pencil-fill"></i>
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="deleteAsset(slotProps.data)"
              >
                <i class="bi bi-trash3-fill"></i>
              </button>
            </template>
          </Column>
        </DataTable>
      </div>
    </div>
    <div class="table-crud">
      <CreateTransactionDialog
        :createTransactionDialog="createTransactionDialog"
        @transactionCanceled="handleTransactionCanceled()"
        @transactionSubmitted="handleTransactionSubmitted($event)"
      />
      <DeleteAssetDialog
        :deleteAssetDialog="deleteAssetDialog"
        :asset="asset"
        @assetDeletionCanceled="handleAssetDeletionCanceled()"
        @assetDeletionConfirmed="handleAssetDeletionConfirmed($event)"
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
import CreateTransactionDialog from "./CreateTransactionDialog.vue";
import DeleteAssetDialog from "./DeleteAssetDialog.vue";

export default defineComponent({
  name: "AssetsTable",

  components: {
    DataTable,
    Column,
    Row,
    Button,
    Toolbar,
    CreateTransactionDialog,
    DeleteAssetDialog,
  },

  data() {
    return {
      createTransactionDialog: false as Boolean,
      deleteAssetDialog: false as Boolean,
      asset: {} as any,
      assets: [
        {
          ticker: "$ITEM1" as String,
          total: "93" as String,
          buyPrice: "$" as String,
          initialWeight: "22.68%" as String,
          currentPrice: "$" as String,
          gain: "-16.42%" as String,
          currentWeight: "17.42%" as String,
        },
        {
          ticker: "$ITEM2" as String,
          total: "150" as String,
          buyPrice: "$" as String,
          initialWeight: "20.28%" as String,
          currentPrice: "$" as String,
          gain: "-12.01%" as String,
          currentWeight: "16.41%" as String,
        },
        {
          ticker: "$ITEM3" as String,
          total: "86" as String,
          buyPrice: "$" as String,
          initialWeight: "5.62%" as String,
          currentPrice: "$" as String,
          gain: "-16.84%" as String,
          currentWeight: "4.3%" as String,
        },
        {
          ticker: "$ITEM4" as String,
          total: "55" as String,
          buyPrice: "$" as String,
          initialWeight: "16.87%" as String,
          currentPrice: "$" as String,
          gain: "1.91%" as String,
          currentWeight: "15.82%" as String,
        },
        {
          ticker: "$ITEM5" as String,
          total: "84" as String,
          buyPrice: "$" as String,
          initialWeight: "5.15%" as String,
          currentPrice: "$" as String,
          gain: "24.72%" as String,
          currentWeight: "5.91%" as String,
        },
        {
          ticker: "$ITEM6" as String,
          total: "80" as String,
          buyPrice: "$" as String,
          initialWeight: "8.08%" as String,
          currentPrice: "$" as String,
          gain: "-16.42%" as String,
          currentWeight: "6.76%" as String,
        },
        {
          ticker: "$ITEM7" as String,
          total: "9" as String,
          buyPrice: "$" as String,
          initialWeight: "1.75%" as String,
          currentPrice: "$" as String,
          gain: "39.53%" as String,
          currentWeight: "2.25%" as String,
        },
        {
          ticker: "$ITEM8" as String,
          total: "350" as String,
          buyPrice: "$" as String,
          initialWeight: "19.57%" as String,
          currentPrice: "$" as String,
          gain: "70.15%" as String,
          currentWeight: "30.78%" as String,
        },
      ] as Array<any>,
    };
  },

  methods: {
    deleteAsset(asset: any) {
      this.asset = asset;
      this.deleteAssetDialog = true;
    },

    handleAssetDeletionCanceled() {
      this.deleteAssetDialog = false;
      this.asset = {};
    },

    handleAssetDeletionConfirmed(asset: any) {
      this.assets = this.assets.filter((val) => val.ticker !== asset.ticker);
      this.deleteAssetDialog = false;

      this.asset = {};
      this.$toast.add({
        severity: "success",
        summary: "Successful",
        detail: "Asset Deleted",
        life: 3000,
      });
    },

    createTransaction() {
      this.createTransactionDialog = true;
    },

    handleTransactionCanceled() {
      this.createTransactionDialog = false;
    },

    handleTransactionSubmitted(asset: any) {
      this.createTransactionDialog = false;
      this.assets.push(asset);
      this.$toast.add({
        severity: "success",
        summary: "Successful",
        detail: "Transaction Submitted",
        life: 3000,
      });
    },
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
