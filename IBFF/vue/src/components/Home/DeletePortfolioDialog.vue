<template>
  <Dialog
    :visible="deletePortfolioDialog"
    :style="{ width: '450px' }"
    header="Confirm"
    :modal="true"
    @update:visible="cancelPortfolioDeletion()"
  >
    <div class="confirmation-content">
      <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
      <span v-if="portfolio"
        >Are you sure you want to delete <b>{{ portfolio.name }}</b
        >?</span
      >
    </div>
    <template #footer>
      <Button
        label="No"
        icon="pi pi-times"
        class="p-button-text"
        @click="cancelPortfolioDeletion()"
      />
      <Button
        label="Yes"
        icon="pi pi-check"
        class="p-button-text"
        @click="confirmPortfolioDeletion()"
      />
    </template>
  </Dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import { Portfolio } from "../../common/models";

export default defineComponent({
  name: "DeletePortfolioDialog",

  components: {
    Button,
    Dialog,
  },

  props: {
    deletePortfolioDialog: {
      required: true,
      type: Boolean,
      default: false,
    },
    portfolio: {
      required: true,
      type: Object as () => Portfolio,
      default: {}
    }
  },

  emits: {
    portfolioDeletionConfirmed: (portfolio: Portfolio) => true,
    portfolioDeletionCanceled: () => true,
  },

  data() {
    return {
      //
    };
  },

  methods: {
    cancelPortfolioDeletion() {
      this.$emit("portfolioDeletionCanceled");
    },

    confirmPortfolioDeletion() {
      this.$emit("portfolioDeletionConfirmed", this.portfolio);
    },
  },
});
</script>

<style>
</style>
