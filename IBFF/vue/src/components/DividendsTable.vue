<template>
  <div class="dividends-table">
    <DataTable
      :value="dividends"
      editMode="row"
      dataKey="id"
      v-model:editingRows="editingDividends"
      :scrollable="true"
      :paginator="true"
      :rows="5"
      paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
      :rowsPerPageOptions="[5, 10]"
      currentPageReportTemplate="Showing {first} to {last} of {totalRecords} dividends"
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
      <Column field="perShare" header="Per Share">
        <template #editor="{ data, field }">
          <InputNumber
            id="dividend"
            v-model="data[field]"
            mode="decimal"
            :min="0.01"
            :maxFractionDigits="2"
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
            @click="editDividend(slotProps.data)"
          >
            <i class="bi bi-pencil-fill"></i>
          </button>
          <button
            type="button"
            class="btn btn-danger btn-sm"
            @click="deleteDividend(slotProps.data)"
          >
            <i class="bi bi-trash3-fill"></i>
          </button>
        </template>
        <template #editor="slotProps">
          <button
            type="button"
            class="btn btn-warning btn-sm mr-1"
            @click="submitDividend(slotProps.data, slotProps.index)"
          >
            <i class="bi bi-check"></i>
          </button>
          <button
            type="button"
            class="btn btn-warning btn-sm"
            @click="revertDividend(slotProps.data)"
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
  name: "DividendsTable",

  expose: ["addDividend"],

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
      dividends: [
        {
          id: "1000",
          date: new Date("2020-01-30") as Date,
          perShare: 1 as Number,
          yield: "3%" as String,
          ticker: "$ITEM1" as String,
        },
        {
          id: "1002",
          date: new Date("2020-08-12") as Date,
          perShare: 3 as Number,
          yield: "3%" as String,
          ticker: "$ITEM1" as String,
        },
        {
          id: "1004",
          date: new Date("2021-10-26") as Date,
          perShare: 2 as Number,
          yield: "4%" as String,
          ticker: "$ITEM1" as String,
        },
        {
          id: "1005",
          date: new Date("2022-02-24") as Date,
          perShare: 3 as Number,
          yield: "7%" as String,
          ticker: "$ITEM1" as String,
        },
      ] as Array<any>,
      editingDividends: [] as Array<any>,
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

    editDividend(dividend: any) {
      this.editingDividends = [dividend];
    },

    deleteDividend(dividend: any) {
      this.dividends = this.dividends.filter((val) => val.id !== dividend.id);
      this.editingDividends = [];

      this.$toast.add({
        severity: "success",
        summary: "Successful",
        detail: "Dividend Deleted",
        life: 3000,
      });
    },

    submitDividend(dividend: any, index: number) {
      this.dividends[index] = dividend;
      this.editingDividends = [];

      this.$toast.add({
        severity: "success",
        summary: "Successful",
        detail: "Dividend Modified",
        life: 3000,
      });
    },

    revertDividend(dividend: any) {
      this.editingDividends = [];
    },

    addDividend(dividend: any) {
      this.dividends.push(dividend);
    }
  },
});

</script>

<style>
.dividends-table .p-datatable-tbody {
  min-height: 27.2rem;
  max-height: 27.2rem;
}

.dividends-table .p-datatable .p-datatable-thead tr th {
  justify-content: end;
  background-color: #f6f6f6;
  width: 1rem;
}

.dividends-table .p-datatable .p-datatable-tbody .p-datatable-row-expansion {
  background-color: #f6f6f6;
}

.dividends-table .p-datatable .p-datatable-tbody tr td {
  justify-content: end;
  padding-top: 0.7rem;
  padding-bottom: 0.7rem;
}

.dividends-table .card {
  border-color: #a4a4a4;
}

.dividends-table .p-inputnumber .p-inputnumber-input {
  width: 7rem;
  height: 3rem;
  padding: 0.5rem;
}

.dividends-table .p-calendar .p-inputtext {
  width: 6.5rem;
  height: 3rem;
  padding: 0.5rem;
}

.dividends-table .p-inputtext {
  width: 7rem;
  height: 3rem;
  padding: 0.5rem;
}
</style>
