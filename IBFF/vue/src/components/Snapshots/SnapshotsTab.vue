<template>
  <div class="snapshots-tab">
    <div class="card">
      <SnapshotsTable />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SnapshotsTable from "./SnapshotsTable.vue";

export default defineComponent({
  name: "TransactionsTab",

  components: {
    SnapshotsTable
  },

  data() {
    return {
    };
  },

  methods: {
  },
});
</script>

<style>
</style>
