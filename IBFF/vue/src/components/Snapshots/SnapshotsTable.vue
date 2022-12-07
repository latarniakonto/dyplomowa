<template>
  <div class="snapshots-table">
    <DataTable
      :value="snapshots"
      dataKey="id"
      :scrollable="true"
      :paginator="true"
      :rows="5"
      paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
      :rowsPerPageOptions="[5, 10]"
      currentPageReportTemplate="Showing {first} to {last} of {totalRecords} snapshots"
      v-model:expandedRows="expandedSnapshots"
    >
      <Column class="expander" :expander="true"></Column>
      <Column field="date" header="Date">
        <template #body="slotProps">
          {{ getPrintableDate(slotProps.data.date) }}
        </template>
      </Column>
      <Column>
        <template #body="slotProps">
          <a
            :href="'snapshot' + slotProps.data.id"
            class="btn btn-sm mr-1"
            :class="{
              'btn-warning':
                currentSnapshot.id === undefined ||
                currentSnapshot.id !== slotProps.data.id,
              'btn-success':
                currentSnapshot.id !== undefined &&
                currentSnapshot.id === slotProps.data.id,
            }"
            @click="restoreSnapshot(slotProps.data)"
          >
            <i class="mdi mdi-history"></i>
          </a>
          <a
            v-if="
              currentSnapshot.id !== undefined &&
              currentSnapshot.id === slotProps.data.id
            "
            :href="'cancel/snapshot' + slotProps.data.id"
            class="btn btn-sm mr-1 btn-danger"
            @click="cancelSnapshot(slotProps.data)"
          >
            <i class="mdi mdi-close-circle-outline"></i>
          </a>
        </template>
      </Column>
      <template #expansion="slotProps">
        <div class="snapshot-details">
          <div class="d-inline-block mr-5 p-1">
            <span class="title">Deposit</span>
            <span class="data">{{ slotProps.data.deposit }}</span>
          </div>
          <div class="d-inline-block mr-5 p-1">
            <span class="title">Cash on Hand</span>
            <span class="data">{{ slotProps.data.cashOnHand }}</span>
          </div>
          <div class="d-inline-block mr-5 p-1">
            <span class="title">Portfolio Value</span>
            <span class="data">{{ slotProps.data.portfolioValue }}</span>
          </div>
          <div class="d-inline-block mr-5 p-1">
            <span class="title">No. of Transactions</span>
            <span class="data">{{ slotProps.data.transactionsCounter }}</span>
          </div>
          <div class="d-inline-block mr-5 p-1">
            <span class="title">Transactions Cost</span>
            <span class="data">{{ slotProps.data.transactionsCost }}</span>
          </div>
          <div class="d-inline-block mr-5 p-1">
            <span class="title">Total Annual Gain</span>
            <span class="data">{{ slotProps.data.annualGain }}</span>
          </div>
          <div class="d-inline-block mr-5 p-1">
            <span class="title">Total Annual Yield</span>
            <span class="data">{{ slotProps.data.annualYield }}</span>
          </div>
          <div class="d-inline-block p-1">
            <span class="title">Total Annual Yield</span>
            <span class="data">{{ slotProps.data.annualDividends }}</span>
          </div>
        </div>
      </template>
    </DataTable>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Row from "primevue/row";
import InputText from "primevue/inputtext";
import InputNumber from "primevue/inputnumber";
import Dropdown from "primevue/dropdown";
import Calendar from "primevue/calendar";

export default defineComponent({
  name: "SnapshotsTable",

  components: {
    Button,
    DataTable,
    Column,
    Row,
    InputText,
    Dropdown,
    InputNumber,
    Calendar,
  },

  data() {
    return {
      snapshots: [
        {
          id: "1000",
          date: new Date("2020-01-30") as Date,
          deposit: "30000" as String,
          cashOnHand: "2000" as String,
          portfolioValue: "77000",
          transactionsCounter: 9 as Number,
          transactionsCost: "120" as String,
          annualGain: "47000" as String,
          annualYield: "156.67%" as String,
          annualDividends: "1200" as String,
        },
        {
          id: "1001",
          date: new Date("2020-08-12") as Date,
          deposit: "30000" as String,
          cashOnHand: "2000" as String,
          portfolioValue: "77000",
          transactionsCounter: 9 as Number,
          transactionsCost: "120" as String,
          annualGain: "47000" as String,
          annualYield: "156.67%" as String,
          annualDividends: "1200" as String,
        },
        {
          id: "1002",
          date: new Date("2020-08-12") as Date,
          deposit: "30000" as String,
          cashOnHand: "2000" as String,
          portfolioValue: "77000",
          transactionsCounter: 9 as Number,
          transactionsCost: "120" as String,
          annualGain: "47000" as String,
          annualYield: "156.67%" as String,
          annualDividends: "1200" as String,
        },
        {
          id: "1003",
          date: new Date("2021-04-07") as Date,
          deposit: "30000" as String,
          cashOnHand: "2000" as String,
          portfolioValue: "77000",
          transactionsCounter: 9 as Number,
          transactionsCost: "120" as String,
          annualGain: "47000" as String,
          annualYield: "156.67%" as String,
          annualDividends: "1200" as String,
        },
        {
          id: "1004",
          date: new Date("2021-10-26") as Date,
          deposit: "30000" as String,
          cashOnHand: "2000" as String,
          portfolioValue: "77000",
          transactionsCounter: 9 as Number,
          transactionsCost: "120" as String,
          annualGain: "47000" as String,
          annualYield: "156.67%" as String,
          annualDividends: "1200" as String,
        },
        {
          id: "1005",
          date: new Date("2022-02-24") as Date,
          deposit: "30000" as String,
          cashOnHand: "2000" as String,
          portfolioValue: "77000",
          transactionsCounter: 9 as Number,
          transactionsCost: "120" as String,
          annualGain: "47000" as String,
          annualYield: "156.67%" as String,
          annualDividends: "1200" as String,
        },
        {
          id: "1006",
          date: new Date("2022-02-24") as Date,
          deposit: "30000" as String,
          cashOnHand: "2000" as String,
          portfolioValue: "77000",
          transactionsCounter: 9 as Number,
          transactionsCost: "120" as String,
          annualGain: "47000" as String,
          annualYield: "156.67%" as String,
          annualDividends: "1200" as String,
        },
      ] as Array<any>,
      expandedSnapshots: [] as Array<any>,
      currentSnapshot: {} as Object,
    };
  },

  methods: {
    getPrintableDate(date: Date) {
      return (
        date.getDate().toString() +
        "." +
        (date.getMonth() + 1).toString() +
        "." +
        date.getFullYear().toString()
      );
    },

    restoreSnapshot(snapshot: any) {
      this.currentSnapshot = snapshot;
    },

    cancelSnapshot(snapshot: any) {
      this.currentSnapshot = {};
    },
  },
});
</script>

<style>
.snapshots-table .p-datatable-tbody {
  min-height: 27.2rem;
  max-height: 27.2rem;
}

.snapshots-table .p-datatable .p-datatable-thead tr th {
  justify-content: end;
  background-color: #f6f6f6;
  width: 1rem;
}

.snapshots-table .p-datatable .p-datatable-tbody .p-datatable-row-expansion {
  background-color: #f6f6f6;
}

.snapshots-table .p-datatable .p-datatable-tbody tr td:not(.expander) {
  justify-content: end;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.snapshots-table .p-datatable .p-datatable-tbody tr td.expander {
  justify-content: start;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.snapshots-table
  .p-datatable
  .p-datatable-tbody
  tr.p-datatable-row-expansion
  td {
  justify-content: center;
}

.snapshots-table .snapshot-details .title {
  font-weight: 500;
  display: block;
  text-align: right;
  margin-bottom: 0.5rem;
}

.snapshots-table .snapshot-details .data {
  display: block;
  text-align: right;
}

.snapshots-table .card {
  border-color: #a4a4a4;
}

.snapshots-table .p-datatable .p-datatable-tbody tr td a {
  color: inherit;
}
</style>
