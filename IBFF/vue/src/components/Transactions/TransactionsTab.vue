<template>
  <div class="resources-tab mb-2">
    <div class="card">
      <div class="table-toolbar">
        <Toolbar class="mb-4">
          <template #start>
            <Button
              label="Transaction"
              icon="pi pi-plus"
              class="p-button-success mr-2"
              @click="addTransaction()"
            />
          </template>
        </Toolbar>
      </div>
      <TransactionsTable ref="transactionsTable" />
    </div>
    <AddTransactionDialog
      :addTransactionDialog="addTransactionDialog"
      @transactionAdded="handleTransactionAdded($event)"
      @transactionAddingCanceled="handleTransactionAddingCanceled()"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Toolbar from "primevue/toolbar";
import TransactionsTable from "./TransactionsTable.vue";
import AddTransactionDialog from "./AddTransactionDialog.vue";

export default defineComponent({
  name: "TransactionsTab",

  components: {
    Button,
    Toolbar,
    TransactionsTable,
    AddTransactionDialog,
  },

  data() {
    return {
      addTransactionDialog: false as Boolean,
    };
  },

  methods: {
    addTransaction() {
      this.addTransactionDialog = true;
    },

    handleTransactionAdded(transaction: any) {
      let child = this.$refs.transactionsTable as typeof TransactionsTable;
      if (child) {        
        child.addTransaction(transaction);
      }

      this.addTransactionDialog = false;
    },

    handleTransactionAddingCanceled() {
      this.addTransactionDialog = false;
    }
  },
});
</script>

<style>
.resources-tab .table-toolbar {
  background-color: #f6f6f6;
  height: 60px;
}

.resources-tab .table-toolbar .p-toolbar {
  background-color: #f6f6f6;
  border-color: #a4a4a4;
  padding: 0.3rem 0 0 0.3rem;
}
</style>
