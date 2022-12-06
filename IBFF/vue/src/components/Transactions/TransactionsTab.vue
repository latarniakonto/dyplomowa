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
            />
          </template>
        </Toolbar>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Toolbar from "primevue/toolbar";
export default defineComponent({
  name: "TransactionsTab",

  components: {
    Button,
    Toolbar,
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
