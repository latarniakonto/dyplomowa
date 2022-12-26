<template>
  <div class="transactions-table">
    <Panel :collapsed="transactionsTableCollapsed">
      <template #header>
        <div
          class="transactions-table-panel-header"
          @click="toggleTransactionsTable()"
        >
          <span class="p-panel-title">Transactions</span>
        </div>
      </template>
      <template #icons>
        <div
          class="transactions-table-panel-header"
          @click="toggleTransactionsTable()"
        >
          <div class="p-panel-header-icon p-link mr-2">
            <span v-if="transactionsTableCollapsed" class="pi pi-plus"></span>
            <span v-else class="pi pi-minus"></span>
          </div>
        </div>
      </template>
      <div class="card">
        <DataTable :value="transactions" :scrollable="true">
          <Column field="type" header="Type">
            <template #body="slotProps">
              {{ transactionType(slotProps.data.type) }}
            </template>
          </Column>
          <Column field="price" header="Price"> </Column>
          <Column field="amount" header="Amount"> </Column>
          <Column field="provision" header="Provision"> </Column>
          <Column
            headerClass="pr-6"
            bodyClass="pr-6"
            field="date"
            header="Date"
          >
            <template #body="slotProps">
              {{ getPrintableDate(slotProps.data.date) }}
            </template>
          </Column>
        </DataTable>
      </div>
    </Panel>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Row from "primevue/row";
import Panel from "primevue/panel";
import { Transaction, transactionType } from "../../common/models";

export default defineComponent({
  name: "TransactionsPanel",

  components: {
    Button,
    DataTable,
    Column,
    Row,
    Panel,
  },

  props: {
    transactions: {
      type: Array as () => Array<Transaction>,
      required: true,
      default: [],
    },
  },

  data() {
    return {
      transactionsTableCollapsed: true as Boolean,
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

    toggleTransactionsTable() {
      this.transactionsTableCollapsed = !this.transactionsTableCollapsed;
    },

    transactionType,
  },
});
</script>

<style>
.transactions-table .p-datatable-tbody {
  min-height: 27.2rem;
  max-height: 27.2rem;
}

.transactions-table .p-datatable .p-datatable-thead tr th {
  justify-content: end;
  background-color: #f6f6f6;
}

.transactions-table .p-datatable .p-datatable-tbody tr td {
  justify-content: end;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.transactions-table .card {
  border-color: #a4a4a4;
}

.transactions-table .p-panel .p-panel-header {
  padding: 0;
  background-color: #f6f6f6;
  cursor: pointer;
  border-bottom-style: solid;
  border-bottom-width: 0.1rem;
  border-bottom-color: #a4a4a4;
  align-items: stretch;
}

.transactions-table .p-panel .p-panel-header:hover {
  background-color: #ededed;
}

.transactions-table .p-panel .p-panel-header .p-panel-header-icon {
  pointer-events: none;
}

.transactions-table .p-panel .p-panel-content {
  padding: 0;
}

.transactions-table .transactions-table-panel-header {
  padding: 1rem;
  flex: 1;
}

.transactions-table .transactions-table-panel-header .p-panel-title {
  line-height: 2em;
}
</style>
