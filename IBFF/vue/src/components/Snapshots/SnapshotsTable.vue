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
      <Column field="date" header="Date" headerClass="pr-6" bodyClass="pr-6">
        <template #body="slotProps">
          {{ getPrintableDate(slotProps.data.date) }}
        </template>
      </Column>
      <template #expansion="slotProps">
        <div class="snapshot-details">
          <div class="d-inline-block mr-4 p-1">
            <span class="title">Deposit</span>
            <span class="data">
              {{ getPrintableValue(slotProps.data.deposit, 2) }}
            </span>
          </div>
          <div class="d-inline-block mr-4 p-1">
            <span class="title">Cash on Hand</span>
            <span class="data">
              {{ getPrintableValue(slotProps.data.cashOnHand, 2) }}
            </span>
          </div>
          <div class="d-inline-block mr-4 p-1">
            <span class="title">Portfolio Value</span>
            <span class="data">
              {{ getPrintableValue(slotProps.data.value, 2) }}
            </span>
          </div>
          <div class="d-inline-block mr-4 p-1">
            <span class="title">No. of Transactions</span>
            <span class="data">{{ slotProps.data.transactionsCounter }}</span>
          </div>
          <div class="d-inline-block mr-4 p-1">
            <span class="title">Transactions Cost</span>
            <span class="data">
              {{ getPrintableValue(slotProps.data.transactionsCost, 2) }}
            </span>
          </div>
          <div class="d-inline-block mr-4 p-1">
            <span class="title">Total Annual Gain</span>
            <span class="data">
              {{ getPrintableValue(slotProps.data.annualGain, 2) }}
            </span>
          </div>
          <div class="d-inline-block mr-4 p-1">
            <span class="title">Total Annual Yield</span>
            <span class="data">
              {{ getPrintablePercantage(slotProps.data.annualYield, 2) }}
            </span>
          </div>
          <div class="d-inline-block p-1">
            <span class="title">Total Annual Dividends</span>
            <span class="data">
              {{ getPrintableValue(slotProps.data.annualDividends, 2) }}
            </span>
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
import {
  Snapshot,
  getPrintableValue,
  getPrintablePercantage,
} from "../../common/models";

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

  props: {
    snapshots: {
      type: Array as () => Array<Snapshot>,
      required: true,
      default: [],
    },
  },

  data() {
    return {
      expandedSnapshots: [] as Array<Snapshot>,
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

    getPrintableValue,
    getPrintablePercantage,
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

.snapshots-table .p-datatable .p-datatable-tbody .p-datatable-row-expansion td {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
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
