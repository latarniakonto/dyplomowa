<template>
  <Dialog
    :visible="addDividendDialog"
    :style="{ width: '450px' }"
    :modal="true"
    class="p-fluid"
    @update:visible="cancelDividendAdding()"
  >
    <template #header>
      <h4>Dividend Details</h4>
    </template>
    <div class="dividend-core mb-3">
      <div
        class="ticker mb-3"
        :class="{
          'p-invalid': dividendAdded && !dividend.ticker,
        }"
      >
        <h6 class="mb-2">Asset Ticker</h6>
        <Dropdown
          v-model="dividend.ticker"
          :options="tickers"
          optionLabel="name"
          optionValue="name"
          placeholder="Select a Ticker"
          :class="{
            'p-invalid': dividendAdded && !dividend.ticker,
          }"
        />
        <small class="p-error" v-if="dividendAdded && !dividend.ticker"
          >You need to specify an asset ticker.</small
        >
      </div>
      <div
        class="per-share mb-3"
        :class="{
          'p-invalid': dividendAdded && !dividend.perShare,
        }"
      >
        <h6 class="mb-2">Dividend per Share</h6>
        <InputNumber
          id="perShare"
          v-model="dividend.perShare"
          mode="currency"
          currency="PLN"
          :min="0.01"
          :maxFractionDigits="2"
          autofocus
          required="true"
          :class="{
            'p-invalid': dividendAdded && !dividend.perShare,
          }"
          @input="updateDividendPerShare($event)"
        />
        <small class="p-error" v-if="dividendAdded && !dividend.perShare"
          >You need to specify a dividend per share.</small
        >
      </div>
      <h6 class="mb-2">Dividend Day</h6>
      <div class="dividend-day">
        <div
          class="d-flex"
          :class="{
            'p-invalid': dividendAdded && !dividend.date,
          }"
        >
          <Calendar
            v-model="dividend.date"
            dateFormat="dd.mm.yy"
            autofocus
            :class="{
              'p-invalid': dividendAdded && !dividend.date,
            }"
          />
        </div>
        <small class="p-error" v-if="dividendAdded && !dividend.date"
          >You need to specify a dividend day.</small
        >
      </div>
    </div>
    <template #footer>
      <Button
        label="Cancel"
        icon="pi pi-times"
        class="p-button-text"
        @click="cancelDividendAdding()"
      />
      <Button
        label="Save"
        icon="pi pi-check"
        class="p-button-text"
        @click="addDividend()"
      />
    </template>
  </Dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import InputNumber from "primevue/inputnumber";
import Calendar from "primevue/calendar";
import Dropdown from "primevue/dropdown";

export default defineComponent({
  name: "AddDividendDialog",

  components: {
    Button,
    Dialog,
    InputNumber,
    Calendar,
    Dropdown,
  },

  props: {
    addDividendDialog: {
      type: Boolean,
      required: true,
      default: false,
    },
  },

  emits: {
    dividendAdded: (dividend: any) => true,
    dividendAddingCanceled: () => true,
  },

  data() {
    return {
      tickers: [
        { name: "$ITEM1", code: "id1" },
        { name: "$ITEM2", code: "id2" },
        { name: "$ITEM3", code: "id3" },
        { name: "$ITEM4", code: "id4" },
        { name: "$ITEM5", code: "id5" },
        { name: "$ITEM6", code: "id6" },
        { name: "$ITEM7", code: "id7" },
        { name: "$ITEM8", code: "id8" },
      ] as Array<any>,
      dividendAdded: false as Boolean,
      dividend: {} as any,
    };
  },

  methods: {
    cancelDividendAdding() {
      this.dividend = {};
      this.dividendAdded = false;
      this.$emit("dividendAddingCanceled");
    },

    addDividend() {
      this.dividendAdded = true;
      if (this.dividend.perShare && this.dividend.date && this.dividend.ticker) {
        this.$emit("dividendAdded", this.dividend);

        this.dividend = {};
        this.dividendAdded = false;
      }
    },

    updateDividendPerShare(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.dividend.perShare = e.value;
    },
  },
});
</script>

<style>
.p-togglebutton.p-button.p-invalid {
  border-color: #b00020;
}
</style>
