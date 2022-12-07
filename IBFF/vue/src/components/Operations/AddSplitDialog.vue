<template>
  <Dialog
    :visible="addSplitDialog"
    :style="{ width: '450px' }"
    :modal="true"
    class="p-fluid"
    @update:visible="cancelSplitAdding()"
  >
    <template #header>
      <h4>Split Details</h4>
    </template>
    <div class="split-core mb-3">
      <div
        class="ticker mb-3"
        :class="{
          'p-invalid': splitAdded && !split.ticker,
        }"
      >
        <h6 class="mb-2">Asset Ticker</h6>
        <Dropdown
          v-model="split.ticker"
          :options="tickers"
          optionLabel="name"
          optionValue="name"
          placeholder="Select a Ticker"
          :class="{
            'p-invalid': splitAdded && !split.ticker,
          }"
        />
        <small class="p-error" v-if="splitAdded && !split.ticker"
          >You need to specify an asset ticker.</small
        >
      </div>
      <div
        class="factor mb-3"
        :class="{
          'p-invalid': splitAdded && !split.factor,
        }"
      >
        <h6 class="mb-2">Split factor</h6>
        <InputNumber
          id="perShare"
          v-model="split.factor"
          integeronly
          autofocus
          required="true"
          :min="2"
          :class="{
            'p-invalid': splitAdded && !split.factor,
          }"
          @input="updateSplitFactor($event)"
        />
        <small class="p-error" v-if="splitAdded && !split.factor"
          >You need to specify a split factor.</small
        >
      </div>
      <h6 class="mb-2">Split Day</h6>
      <div class="split-day">
        <div
          class="d-flex"
          :class="{
            'p-invalid': splitAdded && !split.date,
          }"
        >
          <Calendar
            v-model="split.date"
            dateFormat="dd.mm.yy"
            autofocus
            :class="{
              'p-invalid': splitAdded && !split.date,
            }"
          />
        </div>
        <small class="p-error" v-if="splitAdded && !split.date"
          >You need to specify a split day.</small
        >
      </div>
    </div>
    <template #footer>
      <Button
        label="Cancel"
        icon="pi pi-times"
        class="p-button-text"
        @click="cancelSplitAdding()"
      />
      <Button
        label="Save"
        icon="pi pi-check"
        class="p-button-text"
        @click="addSplit()"
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
  name: "AddSplitDialog",

  components: {
    Button,
    Dialog,
    InputNumber,
    Calendar,
    Dropdown,
  },

  props: {
    addSplitDialog: {
      type: Boolean,
      required: true,
      default: false,
    },
  },

  emits: {
    splitAdded: (split: any) => true,
    splitAddingCanceled: () => true,
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
      splitAdded: false as Boolean,
      split: {} as any,
    };
  },

  methods: {
    cancelSplitAdding() {
      this.split = {};
      this.splitAdded = false;
      this.$emit("splitAddingCanceled");
    },

    addSplit() {
      this.splitAdded = true;
      if (this.split.factor && this.split.date && this.split.ticker) {
        this.$emit("splitAdded", this.split);

        this.split = {};
        this.splitAdded = false;
      }
    },

    updateSplitFactor(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.split.factor = e.value;
    },
  },
});
</script>

<style>
.p-togglebutton.p-button.p-invalid {
  border-color: #b00020;
}
</style>
