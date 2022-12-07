<template>
  <Dialog
    :visible="deleteAssetDialog"
    :style="{ width: '450px' }"
    header="Confirm"
    :modal="true"
    @update:visible="cancelAssetDeletion()"
  >
    <div class="confirmation-content">
      <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
      <span v-if="asset"
        >Are you sure you want to delete <b>{{ asset.ticker }}</b
        >?</span
      >
    </div>
    <template #footer>
      <Button
        label="No"
        icon="pi pi-times"
        class="p-button-text"
        @click="cancelAssetDeletion()"
      />
      <Button
        label="Yes"
        icon="pi pi-check"
        class="p-button-text"
        @click="confirmAssetDeletion()"
      />
    </template>
  </Dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";

export default defineComponent({
  name: "DeleteAssetDialog",

  components: {
    Button,
    Dialog,
  },

  props: {
    deleteAssetDialog: {
      required: true,
      type: Boolean,
      default: false,
    },
    asset: {
      required: true,
      type: Object,
      default: {}
    }
  },

  emits: {
    assetDeletionConfirmed: (asset: any) => true,
    assetDeletionCanceled: () => true,
  },

  data() {
    return {
      //
    };
  },

  methods: {
    cancelAssetDeletion() {
      this.$emit("assetDeletionCanceled");
    },

    confirmAssetDeletion() {
      this.$emit("assetDeletionConfirmed", this.asset);
    },
  },
});
</script>

<style>
</style>
