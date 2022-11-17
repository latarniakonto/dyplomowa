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
              @click="addTransaction"
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
            field="gain"
            header="Profit/Loss"
            :sortable="true"
            style="min-width: 3rem"
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
                @click="confirmDeleteAsset(slotProps.data)"
              >
                <i class="bi bi-trash3-fill"></i>
              </button>
            </template>
          </Column>
        </DataTable>
      </div>
    </div>
    <div class="table-crud">
      <Dialog
        v-model:visible="addTransactionDialog"
        :style="{ width: '450px' }"
        header="Transaction Details"
        :modal="true"
        class="p-fluid"
      >
        <div class="transaction-core">
          <div class="field">
            <label for="name">Ticker</label>
            <InputText
              id="ticker"
              v-model.trim="transaction.ticker"
              required="true"
              autofocus
              :class="{
                'p-invalid': transactionSubmitted && !transaction.ticker,
              }"
            />
            <small
              class="p-error"
              v-if="transactionSubmitted && !transaction.ticker"
              >Ticker is required.</small
            >
          </div>
          <div class="transaction-type">
            <div
              class="formgrid grid"
              :class="{
                'p-invalid':
                  transactionSubmitted && !transaction.buy && !transaction.sell,
              }"
            >
              <div class="field col">
                <ToggleButton
                  id="buy"
                  v-model="transaction.buy"
                  onLabel="Buy"
                  offLabel="Buy transaction"
                  onIcon="pi pi-check"
                  offIcon="pi pi-times"
                  :class="{
                    'p-invalid':
                      transactionSubmitted &&
                      !transaction.buy &&
                      !transaction.sell,
                  }"
                  @change="transaction.buy = setTransactionType()"
                />
              </div>
              <div class="field col">
                <ToggleButton
                  id="sell"
                  v-model="transaction.sell"
                  onLabel="Sell"
                  offLabel="Sell transaction"
                  onIcon="pi pi-check"
                  offIcon="pi pi-times"
                  :class="{
                    'p-invalid':
                      transactionSubmitted &&
                      !transaction.sell &&
                      !transaction.buy,
                  }"
                  @change="transaction.sell = setTransactionType()"
                />
              </div>
            </div>
            <small
              class="p-error"
              v-if="
                transactionSubmitted && !transaction.buy && !transaction.sell
              "
              >You need to specify transaction type.</small
            >
          </div>
        </div>
        <div class="transaction-parameters">
          <div
            class="formgrid grid"
            :class="{
              'p-invalid':
                transactionSubmitted && (!transaction.price || !transaction.amount),
            }"
          >
            <div class="field col">
              <label for="price">Price</label>
              <InputNumber
                id="price"
                v-model="transaction.price"
                mode="currency"
                currency="PLN"
                :min="0.001"
                :maxFractionDigits="3"
                autofocus
                required="true"
                :class="{
                  'p-invalid': transactionSubmitted && !transaction.price,
                }"
                @input="updateTransactionPrice($event)"
              />
            </div>
            <div class="field col">
              <label for="quantity">Amount</label>
              <InputNumber
                id="amount"
                v-model="transaction.amount"
                integeronly
                :min="1"
                autofocus
                required="true"
                :class="{
                  'p-invalid': transactionSubmitted && !transaction.amount,
                }"
                @input="updateTransactionAmount($event)"
              />
            </div>
          </div>
          <small
            class="p-error"
            v-if="
              transactionSubmitted &&
              (!transaction.price || !transaction.amount)
            "
            >You need to specify transaction price and amount.</small
          >
          <div class="formgrid grid">
            <div class="field col-6">
              <label for="provision">Provision</label>
              <InputNumber
                id="provision"
                v-model="transaction.provision"
                mode="currency"
                currency="PLN"
                :min="0"
                :maxFractionDigits="2"
              />
            </div>
          </div>
        </div>
        <template #footer>
          <Button
            label="Cancel"
            icon="pi pi-times"
            class="p-button-text"
            @click="hideAddTransactionDialog"
          />
          <Button
            label="Save"
            icon="pi pi-check"
            class="p-button-text"
            @click="saveTransaction"
          />
        </template>
      </Dialog>
      <Dialog
        v-model:visible="deleteAssetDialog"
        :style="{ width: '450px' }"
        header="Confirm"
        :modal="true"
      >
        <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
          <span v-if="asset"
            >Are you sure you want to delete <b>{{ asset.ticker }}</b
            >?</span
          >
        </div>
        <template #footer>
          <Button
            label="No"
            icon="pi pi-times"
            class="p-button-text"
            @click="deleteAssetDialog = false"
          />
          <Button
            label="Yes"
            icon="pi pi-check"
            class="p-button-text"
            @click="deleteasset()"
          />
        </template>
      </Dialog>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Row from "primevue/row";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Dialog from "primevue/dialog";
import Toolbar from "primevue/toolbar";
import InputNumber from "primevue/inputnumber";
import ToggleButton from "primevue/togglebutton";

export default defineComponent({
  name: "AssetsTable",

  components: {
    PortfolioDashboard,
    DataTable,
    Column,
    Row,
    Button,
    InputText,
    Dialog,
    Toolbar,
    InputNumber,
    ToggleButton,
  },

  data() {
    return {
      addTransactionDialog: false as Boolean,
      transactionSubmitted: false as Boolean,
      deleteAssetDialog: false as Boolean,
      transaction: {} as any,
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
    confirmDeleteAsset(asset: any) {
      this.asset = asset;
      this.deleteAssetDialog = true;
    },

    deleteasset() {
      this.assets = this.assets.filter(
        (val) => val.ticker !== this.asset.ticker
      );
      this.deleteAssetDialog = false;
      this.asset = {};
      this.$toast.add({
        severity: "success",
        summary: "Successful",
        detail: "Asset Deleted",
        life: 3000,
      });
    },

    hideAddTransactionDialog() {
      this.addTransactionDialog = false;
      this.transactionSubmitted = false;
    },

    saveTransaction() {
      this.transactionSubmitted = true;

      if (this.transaction.ticker.trim()) {
        this.asset.ticker = this.transaction.ticker.trim();
        this.asset.buyPrice = this.transaction.price;
        this.asset.total = this.transaction.amount;
        this.assets.push(this.asset);
        this.$toast.add({
          severity: "success",
          summary: "Successful",
          detail: "Transaction Submitted",
          life: 3000,
        });
      }

      this.addTransactionDialog = false;
      this.transaction = {};
      this.asset = {};
    },

    addTransaction() {
      this.asset = {};
      this.transaction = {};
      this.transactionSubmitted = false;
      this.addTransactionDialog = true;
    },

    setTransactionType(): Boolean {
      this.transaction.buy = false;
      this.transaction.sell = false;

      return true;
    },

    updateTransactionPrice(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.transaction.price = e.value;
    },

    updateTransactionAmount(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.transaction.amount = e.value;
    }
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

#buy.p-togglebutton.p-button.p-highlight {
  background: green;
}

#sell.p-togglebutton.p-button.p-highlight {
  background: red;
}

.p-togglebutton.p-button.p-invalid {
  border-color: #b00020;
}

.p-dialog-content .transaction-type .grid.p-invalid {
  height: 3rem;
}

.p-dialog-content .transaction-parameters .grid.p-invalid {
  height: 5.6rem;
}
</style>
