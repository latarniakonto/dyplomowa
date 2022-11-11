<template>
  <div class="assets-table">
    <div class="table-responsive">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Ticker</th>
            <th scope="col">Total</th>
            <th scope="col">Average Price</th>
            <th scope="col">Initial Weight</th>
            <th scope="col">Current Price</th>
            <th scope="col">Profit/Loss</th>
            <th scope="col">Current Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(stock, idx) in stocksToShow" :key="stock.ticker">
            <th scope="row">{{ firstStockNumber + idx }}</th>
            <td>{{ stock.ticker }}</td>
            <td>{{ stock.total }}</td>
            <td>{{ stock.buyPrice }}</td>
            <td>{{ stock.initialWeight }}</td>
            <td>{{ stock.currentPrice }}</td>
            <td>{{ stock.gain }}</td>
            <td>{{ stock.currentWeight }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="table-tools">
      <div class="container-select">
        <p class="text-select mt-3 mr-6">Rows per page:</p>
        <select
          @change="refreshStocksToShow()"
          v-model="rowsPerPage"
          class="form-select form-select-md mt-1 mr-6"
        >
          <option value="5" selected>5</option>
          <option value="10">10</option>
        </select>
        <p v-if="lastStockNumber < stocks.length" class="text-select mt-3 mr-6">{{ firstStockNumber }}-{{ lastStockNumber }} of {{ stocks.length }}</p>
        <p v-else class="text-select mt-3 mr-6">{{ firstStockNumber }}-{{ stocks.length }} of {{ stocks.length }}</p>
        <button
          id="app-content"
          class="btn btn-outline-secondary btn-icon mr-6"
          :class="{ disabled: currentPagination === 1 }"
          @click="refreshStocksToShow(--currentPagination)"
        >
          <i class="bi bi-chevron-left"></i>
        </button>
        <button
          id="app-content"
          class="btn btn-outline-secondary btn-icon"
          :class="{ disabled: lastStockNumber > stocks.length }"
          @click="refreshStocksToShow(++currentPagination)"
        >
          <i class="bi bi-chevron-right"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";

export default defineComponent({
  name: "AssetsTable",

  components: {
    PortfolioDashboard,
  },

  data() {
    return {
      rowsPerPage: "5" as String,
      currentPagination: 1 as number,
      firstStockNumber: 1 as number,
      lastStockNumber: 5 as number,
      stocksToShow: [] as Array<Object>,
      stocks: [
        {
          ticker: "$ITEM1" as String,
          total: "93" as String,
          buyPrice: "$" as String,
          initialWeight: "22.68%" as String,
          currentPrice: "$" as String,
          gain: "-16.42%" as String,
          currentWeight: "17.42%" as String,
        },
        {
          ticker: "$ITEM2" as String,
          total: "150" as String,
          buyPrice: "$" as String,
          initialWeight: "20.28%" as String,
          currentPrice: "$" as String,
          gain: "-12.01%" as String,
          currentWeight: "16.41%" as String,
        },
        {
          ticker: "$ITEM3" as String,
          total: "86" as String,
          buyPrice: "$" as String,
          initialWeight: "5.62%" as String,
          currentPrice: "$" as String,
          gain: "-16.84%" as String,
          currentWeight: "4.3%" as String,
        },
        {
          ticker: "$ITEM4" as String,
          total: "55" as String,
          buyPrice: "$" as String,
          initialWeight: "16.87%" as String,
          currentPrice: "$" as String,
          gain: "1.91%" as String,
          currentWeight: "15.82%" as String,
        },
        {
          ticker: "$ITEM5" as String,
          total: "84" as String,
          buyPrice: "$" as String,
          initialWeight: "5.15%" as String,
          currentPrice: "$" as String,
          gain: "24.72%" as String,
          currentWeight: "5.91%" as String,
        },
        {
          ticker: "$ITEM6" as String,
          total: "80" as String,
          buyPrice: "$" as String,
          initialWeight: "8.08%" as String,
          currentPrice: "$" as String,
          gain: "-16.42%" as String,
          currentWeight: "6.76%" as String,
        },
        {
          ticker: "$ITEM7" as String,
          total: "9" as String,
          buyPrice: "$" as String,
          initialWeight: "1.75%" as String,
          currentPrice: "$" as String,
          gain: "39.53%" as String,
          currentWeight: "2.25%" as String,
        },
        {
          ticker: "$ITEM1" as String,
          total: "350" as String,
          buyPrice: "$" as String,
          initialWeight: "19.57%" as String,
          currentPrice: "$" as String,
          gain: "70.15%" as String,
          currentWeight: "30.78%" as String,
        },
      ] as Array<Object>,
    };
  },

  methods: {
    refreshStocksToShow: function (pagination: number = 1) {
      this.currentPagination = pagination;
      this.stocksToShow = [];
      let index = Number(this.rowsPerPage) * (pagination - 1);

      this.firstStockNumber = index + 1;
      this.lastStockNumber = index + Number(this.rowsPerPage);            

      for (let first = index; index < this.stocks.length && index < first + Number(this.rowsPerPage); index++) {
        this.stocksToShow.push(this.stocks[index]);
      }
    },
  },

  created() {
    this.refreshStocksToShow();
  },
});
</script>

<style>
tbody tr {
  line-height: 30px;
  min-height: 30px;
  height: 30px;
}

.table-tools {
  float: right;
}

.container-select {
  display: inline-flex;
}

.container-select .text-select {
  color: grey;
}

.container-select .form-select {
  width: 40px;
  height: 40px;
  border-radius: 0%;
  border-top: none;
  border-right: none;
  border-left: none;
  border-bottom-color: #a4a4a4;
  cursor: pointer;
  background: url("https://api.iconify.design/mdi/menu-down.svg?color=%23757575&width=24&height=24")
    no-repeat center center / contain;
  background-size: 50%;
  background-color: #f6f6f6;
  background-position-x: 1.3rem;
  text-indent: 7px;
  padding-right: 0px;
  direction: rtl;
}

.container-select .form-select:hover {
  background-color: #ededed;
  border-bottom-color: #393939;
}

.container-select .form-select:focus {
  background-color: #ededed;
  box-shadow: none;
  border-color: white;
  border-bottom-color: #393939;
}

.container-select .text-select {
  line-height: 12px;
}

#app-content.btn-icon {
  background-color: white;
  border: none;
}

#app-content.btn-icon:hover {
  background-color: #ededed;
  border-color: #393939;
}
</style>
