<template>
  <Dialog
    :visible="addPortfolioDialog"
    :style="{ width: '450px' }"
    :modal="true"
    class="p-fluid"
    @update:visible="cancelPortfolioAdding()"
  >
    <template #header>
      <h4>New Portfolio</h4>
    </template>
    <div class="portfolio-core mb-3">
      <div
        class="portfolio-name mb-3"
        :class="{
          'p-invalid': portfolioAdded && !portfolio.name,
        }"
      >
        <h6 class="mb-2">Portfolio Name</h6>
        <InputText
          id="name"
          v-model="portfolio.name"
          autofocus
          required="true"
          :class="{
            'p-invalid': portfolioAdded && !portfolio.name,
          }"
        />
        <small class="p-error" v-if="portfolioAdded && !portfolio.name"
          >You need to specify a portfolio deposit.</small
        >
      </div>
      <div
        class="portfolio-deposit mb-3"
        :class="{
          'p-invalid': portfolioAdded && !portfolio.deposit,
        }"
      >
        <h6 class="mb-2">Starting Deposit</h6>
        <InputNumber
          id="deposit"
          v-model="portfolio.deposit"
          mode="currency"
          currency="PLN"
          :min="0.01"
          :maxFractionDigits="2"
          autofocus
          required="true"
          :class="{
            'p-invalid': portfolioAdded && !portfolio.deposit,
          }"
          @input="updatePortfolioDeposit($event)"
        />
        <small class="p-error" v-if="portfolioAdded && !portfolio.deposit"
          >You need to specify a starting portfolio deposit.</small
        >
      </div>
    </div>
    <template #footer>
      <Button
        label="Cancel"
        icon="pi pi-times"
        class="p-button-text"
        @click="cancelPortfolioAdding()"
      />
      <Button
        label="Save"
        icon="pi pi-check"
        class="p-button-text"
        @click="addPortfolio()"
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
import { Portfolio } from "../../common/models";

export default defineComponent({
  name: "AddPortfolioDialog",

  components: {
    Button,
    InputText,
    Dialog,
    InputNumber,
  },

  props: {
    addPortfolioDialog: {
      type: Boolean,
      required: true,
      default: false,
    },
  },

  emits: {
    portfolioAdded: (portfolio: Portfolio) => true,
    portfolioAddingCanceled: () => true,
  },

  data() {
    return {
      portfolioAdded: false as Boolean,
      portfolio: new Portfolio(),
    };
  },

  methods: {
    cancelPortfolioAdding() {
      this.portfolio = new Portfolio();
      this.portfolioAdded = false;
      this.$emit("portfolioAddingCanceled");
    },

    addPortfolio() {
      this.portfolioAdded = true;
      if (
        this.portfolio.name &&
        (this.portfolio.deposit || this.portfolio.deposit === 0)
      ) {
        this.portfolio.cashOnHand = this.portfolio.deposit;
        this.portfolio.value = this.portfolio.deposit;        
        this.$emit("portfolioAdded", this.portfolio);

        this.portfolio = new Portfolio();
        this.portfolioAdded = false;
      }
    },

    updatePortfolioDeposit(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.portfolio.deposit = e.value;
    },    
  },
});
</script>

<style>
</style>
