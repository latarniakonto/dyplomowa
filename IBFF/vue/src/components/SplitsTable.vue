<template>
  <div class="splits-table">
    <DataTable
      :value="splits"
      editMode="row"
      dataKey="id"
      v-model:editingRows="editingSplits"
      :scrollable="true"
      :paginator="true"
      :rows="5"
      paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
      :rowsPerPageOptions="[5, 10]"
      currentPageReportTemplate="Showing {first} to {last} of {totalRecords} splits"
    >
      <Column field="ticker" header="Ticker">
        <template #editor="{ data, field }">
          <InputText
            id="ticker"
            v-model.trim="data[field]"
            required="true"
            autofocus
          />
        </template>
      </Column>
      <Column field="factor" header="Split Factor">
        <template #editor="{ data, field }">
          <InputNumber
            id="split"
            v-model="data[field]"
            integeronly
            autofocus
            required="true"
          />
        </template>
      </Column>
      <Column field="date" header="Date">
        <template #body="slotProps">
          {{ getPrintableDate(slotProps.data.date) }}
        </template>
        <template #editor="{ data, field }">
          <Calendar v-model="data[field]" dateFormat="dd.mm.yy" autofocus />
        </template>
      </Column>
      <Column>
        <template #body="slotProps">
          <button
            type="button"
            class="btn btn-warning btn-sm mr-1"
            @click="editSplit(slotProps.data)"
          >
            <i class="bi bi-pencil-fill"></i>
          </button>
          <button
            type="button"
            class="btn btn-danger btn-sm"
            @click="deleteSplit(slotProps.data)"
          >
            <i class="bi bi-trash3-fill"></i>
          </button>
        </template>
        <template #editor="slotProps">
          <button
            type="button"
            class="btn btn-warning btn-sm mr-1"
            @click="submitSplit(slotProps.data, slotProps.index)"
          >
            <i class="bi bi-check"></i>
          </button>
          <button
            type="button"
            class="btn btn-warning btn-sm"
            @click="revertSplit(slotProps.data)"
          >
            <i class="bi bi-x"></i>
          </button>
        </template>
      </Column>
    </DataTable>
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
import Toolbar from "primevue/toolbar";
import RadioButton from "primevue/radiobutton";

export default defineComponent({
  name: "SplitsTable",

  components: {
    Button,
    DataTable,
    Column,
    Row,
    InputText,
    Dropdown,
    InputNumber,
    Calendar,
    Toolbar,
    RadioButton,
  },

  data() {
    return {
      splits: [
        {
          id: "1000",
          date: new Date("2020-01-30") as Date,
          factor: 1 as Number,
          ticker: "$ITEM1" as String,
        },
        {
          id: "1001",
          date: new Date("2020-08-12") as Date,
          factor: 4 as Number,
          ticker: "$ITEM1" as String,
        },
        {
          id: "1003",
          date: new Date("2021-04-07") as Date,
          ticker: "$ITEM1" as String,
          factor: 15 as Number,
        },
        {
          id: "1006",
          date: new Date("2022-02-24") as Date,
          ticker: "$ITEM1" as String,
          factor: 15 as Number,
        },
      ] as Array<any>,
      editingSplits: [] as Array<any>,
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

    editSplit(split: any) {
      this.editingSplits = [split];
    },

    deleteSplit(split: any) {
      this.splits = this.splits.filter((val) => val.id !== split.id);
      this.editingSplits = [];

      this.$toast.add({
        severity: "success",
        summary: "Successful",
        detail: "Split Deleted",
        life: 3000,
      });
    },

    submitSplit(split: any, index: number) {
      this.splits[index] = split;
      this.editingSplits = [];

      this.$toast.add({
        severity: "success",
        summary: "Successful",
        detail: "Dividend Modified",
        life: 3000,
      });
    },

    revertSplit(split: any) {
      this.editingSplits = [];
    },

    addSplit(split: any) {
      this.splits.push(split);
    }
  },
});
</script>

<style>
.splits-table .p-datatable-tbody {
  min-height: 27.2rem;
  max-height: 27.2rem;
}

.splits-table .p-datatable .p-datatable-thead tr th {
  justify-content: end;
  background-color: #f6f6f6;
  width: 1rem;
}

.splits-table .p-datatable .p-datatable-tbody .p-datatable-row-expansion {
  background-color: #f6f6f6;
}

.splits-table .p-datatable .p-datatable-tbody tr td {
  justify-content: end;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.splits-table .card {
  border-color: #a4a4a4;
}

.splits-table .p-inputnumber .p-inputnumber-input {
  width: 7rem;
  height: 3rem;
  padding: 0.5rem;
}

.splits-table .p-calendar .p-inputtext {
  width: 6.5rem;
  height: 3rem;
  padding: 0.5rem;
}

.splits-table .p-inputtext {
  width: 7rem;
  height: 3rem;
  padding: 0.5rem;
}
</style>
