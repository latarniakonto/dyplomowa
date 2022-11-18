<template>
  <Dialog
    :visible="addTransactionDialog"
    :style="{ width: '450px' }"
    header="Transaction Details"
    :modal="true"
    class="p-fluid"
    @update:visible="hideAddTransactionDialog()"
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
                  transactionSubmitted && !transaction.buy && !transaction.sell,
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
                  transactionSubmitted && !transaction.sell && !transaction.buy,
              }"
              @change="transaction.sell = setTransactionType()"
            />
          </div>
        </div>
        <small
          class="p-error"
          v-if="transactionSubmitted && !transaction.buy && !transaction.sell"
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
          transactionSubmitted && (!transaction.price || !transaction.amount)
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
        @click="hideAddTransactionDialog()"
      />
      <Button
        label="Save"
        icon="pi pi-check"
        class="p-button-text"
        @click="saveTransaction()"
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

export default defineComponent({
  name: "AddTransactionDialog",

  components: {
    Button,
    InputText,
    Dialog,
    InputNumber,
    ToggleButton,
  },

  props: {
    addTransactionDialog: {
      required: true,
      type: Boolean,
      default: false,
    },
  },

  emits: {
    transactionSubmitted: (asset: any) => true,
    transactionCanceled: () => true,
  },

  data() {
    return {
      transactionSubmitted: false as Boolean,
      transaction: {} as any,
      asset: {} as any,
    };
  },

  methods: {
    hideAddTransactionDialog() {
      this.asset = {};
      this.transaction = {};
      this.transactionSubmitted = false;
      this.$emit("transactionCanceled");
    },

    saveTransaction() {
      this.transactionSubmitted = true;
      if (
        this.transaction.ticker &&
        this.transaction.price &&
        this.transaction.amount &&
        (this.transaction.buy || this.transaction.sell)
      ) {
        this.asset.ticker = this.transaction.ticker.trim();
        this.asset.buyPrice = this.transaction.price;
        this.asset.total = this.transaction.amount;

        this.$emit("transactionSubmitted", this.asset);

        this.asset = {};
        this.transaction = {};
        this.transactionSubmitted = false;
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

.p-dialog-content .transaction-type .grid.p-invalid {
  height: 3rem;
}

.p-dialog-content .transaction-parameters .grid.p-invalid {
  height: 5.6rem;
}
</style>
