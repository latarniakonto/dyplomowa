<template>
  <div class="dividends-table">
    <DataTable
      :value="dividends"      
      dataKey="id"      
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
            class="btn btn-danger btn-sm"
            @click="deleteDividend(slotProps.data, slotProps.index)"
          >
            <i class="bi bi-trash3-fill"></i>
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
import { Dividend } from "../../common/models";

export default defineComponent({
  name: "DividendsTable",

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

  props: {
    dividends: {
      type: Array as () => Array<Dividend>,
    }
  },

  emits: {
    dividendDeleted: (dividend: Dividend, index: number) => true,
  },

  data() {
    return {      
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

    deleteDividend(dividend: Dividend, index: number) {
      this.$emit("dividendDeleted", dividend, index);
    },
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
