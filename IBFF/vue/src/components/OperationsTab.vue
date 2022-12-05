<template>
  <div class="operations-tab mb-2">
    <div class="card">
      <div class="table-toolbar">
        <Toolbar class="mb-4">
          <template #start>
            <Button
              label="Dividend"
              icon="pi pi-plus"
              class="p-button-success mr-2"
              @click="addDividend()"
            />
            <Button
              label="Split"
              icon="pi pi-plus"
              class="p-button-success mr-2"
              @click="addSplit()"
            />
          </template>
          <template #end>
            <div
              class="toolbar-tile mr-2"
              :class="{ 'tile-active': operationsTable === 'Dividends' }"
              @click="operationsTable = 'Dividends'"
            >
              <RadioButton
                aria-labelledby="dividends-label"
                class="mr-2"
                name="operationsTable"
                value="Dividends"
                v-model="operationsTable"
              />
              <span id="dividends-label" class="font-medium">Dividends</span>
            </div>
            <div
              class="toolbar-tile mr-2"
              :class="{ 'tile-active': operationsTable === 'Splits' }"
              @click="operationsTable = 'Splits'"
            >
              <RadioButton
                aria-labelledby="splits-label"
                class="mr-2"
                name="operationsTable"
                value="Splits"
                v-model="operationsTable"
                aria-label="Splits"
              />
              <span id="splits-label" class="font-medium">Splits</span>
            </div>
          </template>
        </Toolbar>
      </div>
      <DividendsTable
        v-show="operationsTable === 'Dividends'"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Toolbar from "primevue/toolbar";
import RadioButton from "primevue/radiobutton";
import DividendsTable from "./DividendsTable.vue";

export default defineComponent({
  name: "OperationsTab",

  components: {
    Button,
    Toolbar,
    RadioButton,
    DividendsTable,
  },

  data() {
    return {
      operationsTable: "" as String,
    };
  },

  methods: {
  },
});
</script>

<style>
.operations-tab .table-toolbar {
  background-color: #f6f6f6;
  height: 60px;
}

.operations-tab .table-toolbar .p-toolbar {
  background-color: #f6f6f6;
  border-color: #a4a4a4;
  padding: 0.3rem 0 0 0.3rem;
}

.operations-tab .toolbar-tile {
  cursor: pointer;
  padding: 0.714rem 1rem;
  border-radius: 4px;
  box-shadow: 0 2px 1px -1px rgba(0, 0, 0, 0.2), 0 1px 1px 0 rgba(0, 0, 0, 0.14),
    0 1px 3px 0 rgba(92, 76, 76, 0.12);
  background-color: #f6f6f6;
  border-bottom-style: solid;
  border-bottom-width: 0rem;
  border-bottom-color: #a4a4a4;
}

.operations-tab .toolbar-tile.tile-active {
  background-color: #ededed;
  box-shadow: inset 0px 0px 6px #d3d3d3;
}

.operations-tab .toolbar-tile:hover {
  background-color: #ededed;
}
</style>
