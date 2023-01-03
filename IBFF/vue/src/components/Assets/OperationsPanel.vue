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
          <Column field="type" header="Type">
            <template #body="slotProps">
              {{ operationType(slotProps.data.type) }}
            </template>
          </Column>
          <Column
            headerClass="pr-6"
            bodyClass="pr-6"
            field="date"
            header="Date"
          >
            <template #body="slotProps">
              {{ getPrintableDate(slotProps.data.date) }}
            </template>
          </Column>
          <template #expansion="slotProps">
            <div v-if="operationType(slotProps.data.type) === 'Dividend'" class="operation-details">
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
import { Dividend, operationType } from "../../common/models";

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

  props: {
    operations: {
      type: Array as () => Array<Dividend>
    }
  },

  data() {
    return {        
      expandedOperations: [] as Array<Dividend>,
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

    operationType
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

.operations-table .p-datatable .p-datatable-tbody .p-datatable-row-expansion td {
  padding-right: 3rem;
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
