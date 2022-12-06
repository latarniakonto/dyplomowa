<template>
  <Dialog
    :visible="addTransactionDialog"
    :style="{ width: '450px' }"
    :modal="true"
    class="p-fluid"
    @update:visible="cancelTransactionAdding()"
  >
    <template #header>
      <h4>Transaction Details</h4>
    </template>
    <div class="transaction-core mb-3">
      <h6 class="mb-2">Asset Ticker</h6>
      <div class="ticker mb-3">
        <InputText
          id="ticker"
          v-model.trim="transaction.ticker"
          required="true"
          autofocus
          :class="{
            'p-invalid': transactionAdded && !transaction.ticker,
          }"
        />
        <small class="p-error" v-if="transactionAdded && !transaction.ticker"
          >Ticker is required.</small
        >
      </div>
      <h6 class="mb-2">Transaction Type</h6>
      <div class="transaction-type mb-3">
        <div class="d-flex">
          <ToggleButton
            id="buy"
            v-model="transaction.buy"
            onLabel="Buy"
            offLabel="Buy transaction"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            class="mr-2"
            :class="{
              'p-invalid':
                transactionAdded && !transaction.buy && !transaction.sell,
            }"
            @change="transaction.buy = setTransactionType()"
          />
          <ToggleButton
            id="sell"
            v-model="transaction.sell"
            onLabel="Sell"
            offLabel="Sell transaction"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            :class="{
              'p-invalid':
                transactionAdded && !transaction.sell && !transaction.buy,
            }"
            @change="transaction.sell = setTransactionType()"
          />
        </div>
        <small
          class="p-error"
          v-if="transactionAdded && !transaction.buy && !transaction.sell"
          >You need to specify a transaction type.</small
        >
      </div>
    </div>
    <div class="d-inline-flex">
      <div class="price mb-2 mr-2">
        <h6 class="mb-2">Price</h6>
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
            'p-invalid': transactionAdded && !transaction.price,
          }"
          @input="updateTransactionPrice($event)"
        />
        <small class="p-error" v-if="transactionAdded && !transaction.price"
          >You need to specify a transaction price.</small
        >
      </div>
      <div class="amount mb-2">
        <h6 class="mb-2">Amount</h6>
        <InputNumber
          id="amount"
          v-model="transaction.amount"
          integeronly
          :min="1"
          autofocus
          required="true"
          :class="{
            'p-invalid': transactionAdded && !transaction.amount,
          }"
          @input="updateTransactionAmount($event)"
        />
        <small class="p-error" v-if="transactionAdded && !transaction.amount"
          >You need to specify a transaction amount.</small
        >
      </div>
    </div>
    <div class="d-inline-flex">
      <div class="provision mr-2 w-6">
        <h6 class="mb-2">Provision</h6>
        <InputNumber
          id="provision"
          v-model="transaction.provision"
          mode="currency"
          currency="PLN"
          :min="0"
          :maxFractionDigits="2"
          :class="{
            'p-invalid':
              transactionAdded &&
              !transaction.provision &&
              transaction.provision !== 0,
          }"
          @input="updateTransactionProvision($event)"
        />
        <small
          class="p-error"
          v-if="
            transactionAdded &&
            !transaction.provision &&
            transaction.provision !== 0
          "
          >You need to specify a transaction provision.</small
        >
      </div>
      <div class="date w-6">
        <h6 class="mb-2">Date</h6>
        <Calendar
          v-model="transaction.date"
          dateFormat="dd.mm.yy"
          autofocus
          :class="{
            'p-invalid': transactionAdded && !transaction.date,
          }"
        />
        <small class="p-error" v-if="transactionAdded && !transaction.date"
          >You need to specify a transaction date.</small
        >
      </div>
    </div>
    <template #footer>
      <Button
        label="Cancel"
        icon="pi pi-times"
        class="p-button-text"
        @click="cancelTransactionAdding()"
      />
      <Button
        label="Save"
        icon="pi pi-check"
        class="p-button-text"
        @click="addTransaction()"
      />
    </template>
  </Dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Dialog from "primevue/dialog";
import InputNumber from "primevue/inputnumber";
import ToggleButton from "primevue/togglebutton";
import Calendar from "primevue/calendar";

export default defineComponent({
  name: "AddTransactionDialog",

  components: {
    Button,
    InputText,
    Dialog,
    InputNumber,
    ToggleButton,
    Calendar,
  },

  props: {
    addTransactionDialog: {
      required: true,
      type: Boolean,
      default: false,
    },
  },

  emits: {
    transactionAdded: (transaction: any) => true,
    transactionAddingCanceled: () => true,
  },

  data() {
    return {
      transactionAdded: false as Boolean,
      transaction: {} as any,
    };
  },

  methods: {
    cancelTransactionAdding() {
      this.transaction = {};
      this.transactionAdded = false;
      this.$emit("transactionAddingCanceled");
    },

    addTransaction() {
      this.transactionAdded = true;
      if (
        this.transaction.ticker &&
        this.transaction.price &&
        this.transaction.amount &&
        this.transaction.date &&
        (this.transaction.provision ||
        this.transaction.provision === 0) &&
        (this.transaction.buy || this.transaction.sell)
      ) {
        this.transaction.type = this.transaction.buy ? "Buy" : "Sell";

        this.$emit("transactionAdded", this.transaction);

        this.transaction = {};
        this.transactionAdded = false;
      }
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
    },

    updateTransactionProvision(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.transaction.provision = e.value;
    },
  },
});
</script>

<style>
#buy.p-togglebutton.p-button.p-highlight {
  background: green;
}

#sell.p-togglebutton.p-button.p-highlight {
  background: red;
}

.p-togglebutton.p-button.p-invalid {
  border-color: #b00020;
}
</style>
