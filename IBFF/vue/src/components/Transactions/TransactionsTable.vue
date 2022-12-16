<template>
  <div class="transactions-table">
    <DataTable
      :value="transactions"
      editMode="row"
      dataKey="id"
      v-model:editingRows="editingTransactions"
      :scrollable="true"
      :paginator="true"
      :rows="5"
      paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
      :rowsPerPageOptions="[5, 10]"
      currentPageReportTemplate="Showing {first} to {last} of {totalRecords} transactions"
    >
      <Column field="ticker" header="Ticker">
        <template #editor="{ data, field }">
          <InputText v-model.trim="data[field]" required="true" autofocus>
          </InputText>
        </template>
      </Column>
      <Column field="type" header="Type">
        <template #body="slotProps">
          {{ transactionType(slotProps.data.type) }}
        </template>
        <template #editor="{ data, field }">
          <Dropdown
            v-model="data[field]"
            :options="transactionTypes"
            optionLabel="label"
            optionValue="value"
            :placeholder="data[field]"
          >
          </Dropdown>
        </template>
      </Column>
      <Column field="price" header="Price">
        <template #editor="{ data, field }">
          <InputNumber
            id="price"
            v-model="data[field]"
            mode="decimal"
            :min="0.001"
            :maxFractionDigits="3"
            autofocus
            required="true"
          />
        </template>
      </Column>
      <Column field="amount" header="Amount">
        <template #editor="{ data, field }">
          <InputNumber
            id="amount"
            v-model="data[field]"
            integeronly
            :min="1"
            autofocus
            required="true"
          />
        </template>
      </Column>
      <Column field="provision" header="Provision">
        <template #editor="{ data, field }">
          <InputNumber
            id="provision"
            v-model="data[field]"
            mode="decimal"
            :min="0"
            :maxFractionDigits="2"
            required="true"
          />
        </template>
      </Column>
      <Column field="date" header="Date">
        <template #body="slotProps">
          {{ getPrintableDate(slotProps.data.date) }}
        </template>
        <template #editor="{ data, field }">
          <Calendar v-model="data[field]" dateFormat="dd.mm.yy" autofocus />
        </template>
      </Column>
      <Column bodyStyle="text-align:center">
        <template #body="slotProps">
          <button
            type="button"
            class="btn btn-warning btn-sm mr-1"
            @click="editTransaction(slotProps.data)"
          >
            <i class="bi bi-pencil-fill"></i>
          </button>
          <button
            type="button"
            class="btn btn-danger btn-sm"
            @click="deleteTransaction(slotProps.data)"
          >
            <i class="bi bi-trash3-fill"></i>
          </button>
        </template>
        <template #editor="slotProps">
          <button
            type="button"
            class="btn btn-warning btn-sm mr-1"
            @click="submitTransaction(slotProps.data, slotProps.index)"
          >
            <i class="bi bi-check"></i>
          </button>
          <button
            type="button"
            class="btn btn-warning btn-sm"
            @click="revertTransaction(slotProps.data)"
          >
            <i class="bi bi-x"></i>
          </button>
        </template>
      </Column>
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
import { Transaction, transactionType } from "@/common/models";

export default defineComponent({
  name: "TransactionsTable",

  expose: ["addTransaction"],

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
    transactions: {
      type: Array as () => Array<Transaction>,
      required: true,
      default: [],
    },
  },

  data() {
    return {
      transactionTypes: [
        { label: "Buy", value: 1 },
        { label: "Sell", value: 2 },
      ] as Array<any>,
      editingTransactions: [] as Array<Transaction>,
    };
  },

  emits: {
    transactionDeleted: (transaction: Transaction) => true,
    transactionEdited: (transaction: Transaction, index: number) => true,
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

    transactionType,

    editTransaction(transaction: Transaction) {
      this.editingTransactions = [transaction];
    },

    async deleteTransaction(transaction: Transaction) {
      this.editingTransactions = [];
      this.$emit("transactionDeleted", transaction);
    },

    submitTransaction(transaction: any, index: number) {
      this.editingTransactions = [];
      if (
        this.transactions[index].ticker !== transaction.ticker ||
        this.transactions[index].type !== transaction.type ||
        this.transactions[index].price !== transaction.price ||
        this.transactions[index].amount !== transaction.amount ||
        this.transactions[index].provision !== transaction.provision ||
        this.transactions[index].date !== transaction.date
      )
        this.$emit("transactionEdited", transaction, index);
    },

    revertTransaction(transaction: Transaction) {
      this.editingTransactions = [];
    },
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

.transactions-table .p-inputnumber .p-inputnumber-input {
  width: 7rem;
  height: 3rem;
  padding: 0.5rem;
}

.transactions-table .p-inputtext {
  width: 7rem;
  height: 3rem;
  padding: 0.5rem;
}

.transactions-table .p-calendar .p-inputtext {
  width: 6.5rem;
  height: 3rem;
  padding: 0.5rem;
}

.transactions-table .p-dropdown .p-dropdown-label {
  width: 3rem;
  height: 3rem;
  padding: 0.5rem;
}
</style>
