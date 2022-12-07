<template>
  <div class="assets-tab">
    <AssetsTable />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AssetsTable from "./AssetsTable.vue";

export default defineComponent({
  name: "HomeTab",

  components: {
    AssetsTable,
  },

  data() {
    return {};
  },

  methods: {},
});
</script>

<style>
</style>
