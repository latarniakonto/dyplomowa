<template>
  <div class="operations-table mb-2">
    <Panel :collapsed="operationsTableCollapsed">
      <template #header>
        <div
          class="operations-table-panel-header"
          @click="toggleOperationsTable()"
        >
          <span class="p-panel-title">Operations</span>
        </div>
      </template>
      <template #icons>
        <div
          class="operations-table-panel-header"
          @click="toggleOperationsTable()"
        >
          <div class="p-panel-header-icon p-link mr-2">
            <span v-if="operationsTableCollapsed" class="pi pi-plus"></span>
            <span v-else class="pi pi-minus"></span>
          </div>
        </div>
      </template>
      <div class="card">
        <DataTable
          :value="operations"
          editMode="row"
          dataKey="id"
          v-model:expandedRows="expandedOperations"
          :scrollable="true"
        >
          <Column class="expander" :expander="true"></Column>
          <Column field="type" header="Type"> </Column>
          <Column field="date" header="Date">
            <template #body="slotProps">
              {{ getPrintableDate(slotProps.data.date) }}
            </template>
          </Column>
          <Column>
            <template #body="slotProps">
              <button
                type="button"
                class="btn btn-warning btn-sm mr-1"                
              >
                <a :href="'test' + slotProps.data.id">
                    <i class="bi bi-pencil-fill"></i>
                </a>
              </button>              
            </template>
          </Column>
          <template #expansion="slotProps">
            <div v-if="slotProps.data.type === 'Dividend'" class="operation-details">
                <span class="title">Dividend per Share</span>
                <span class="data">{{ slotProps.data.perShare }}</span>
            </div>            
          </template>
        </DataTable>
      </div>
    </Panel>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Row from "primevue/row";
import InputText from "primevue/inputtext";
import InputNumber from "primevue/inputnumber";
import Dropdown from "primevue/dropdown";
import Calendar from "primevue/calendar";
import Panel from "primevue/panel";

export default defineComponent({
  name: "OperationsPanel",

  components: {
    Button,
    DataTable,
    Column,
    Row,
    InputText,
    Dropdown,
    InputNumber,
    Calendar,
    Panel,
  },

  data() {
    return {
      operationsTypes: [        
        { label: "Dividend", value: "Dividend" },
      ] as Array<any>,
      operations: [
        {
          id: "1000",
          date: new Date("2020-01-30") as Date,
          type: "Dividend" as String,
          perShare: 1 as Number,
          yield: "3%" as String,
        },
        {
          id: "1002",
          date: new Date("2020-08-12") as Date,
          type: "Dividend" as String,
          perShare: 3 as Number,
          yield: "3%" as String,
        },
        {
          id: "1004",
          date: new Date("2021-10-26") as Date,
          type: "Dividend" as String,
          perShare: 2 as Number,
          yield: "4%" as String,
        },
        {
          id: "1005",
          date: new Date("2022-02-24") as Date,
          type: "Dividend" as String,
          perShare: 3 as Number,
          yield: "7%" as String,
        },        
      ] as Array<any>,
      expandedOperations: [] as Array<any>,
      operationsTableCollapsed: true as Boolean,
    };
  },

  methods: {
    getPrintableDate(date: Date) {
      return (
        date.getDate().toString() +
        "." +
        (date.getMonth() + 1).toString() +
        "." +
        date.getFullYear().toString()
      );
    },

    toggleOperationsTable() {
      this.operationsTableCollapsed = !this.operationsTableCollapsed;
    },
  },
});
</script>

<style>
.operations-table .p-datatable-tbody {
  min-height: 27.2rem;
  max-height: 27.2rem;
}

.operations-table .p-datatable .p-datatable-thead tr th {
  justify-content: end;
  background-color: #f6f6f6;
  width: 1rem;
}

.operations-table .p-datatable .p-datatable-tbody .p-datatable-row-expansion {
  background-color: #f6f6f6;
}

.operations-table .p-datatable .p-datatable-tbody tr td:not(.expander) {
  justify-content: end;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.operations-table .p-datatable .p-datatable-tbody tr td.expander {
  justify-content: start;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.operations-table .p-datatable .p-datatable-tbody tr td a {
  color: inherit;
}

.operations-table .operation-details {
    flex: 1;
}

.operations-table .operation-details .title {
    font-weight: 500;
    float: left;
}

.operations-table .operation-details .data {
    float: right;
}

.operations-table .card {
  border-color: #a4a4a4;
}

.operations-table .p-panel .p-panel-header {
  padding: 0;
  background-color: #f6f6f6;
  cursor: pointer;
  border-bottom-style: solid;
  border-bottom-width: 0.1rem;
  border-bottom-color: #a4a4a4;
  align-items: stretch;
}

.operations-table .p-panel .p-panel-header:hover {
  background-color: #ededed;
}

.operations-table .p-panel .p-panel-header .p-panel-header-icon {
  pointer-events: none;
}

.operations-table .p-panel .p-panel-content {
  padding: 0;
}

.operations-table .operations-table-panel-header {
  padding: 1rem;
  flex: 1;
}

.operations-table .operations-table-panel-header .p-panel-title {
  line-height: 2em;
}
</style>
