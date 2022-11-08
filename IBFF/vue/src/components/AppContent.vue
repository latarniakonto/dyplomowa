<template>
  <v-container color="white">
    <v-row no-gutters align="start">
      <v-col cols="3">
        <v-sheet height="470" rounded class="ma-3 pa-3">
          <portfolio-dashboard/>
        </v-sheet>
      </v-col>
      <v-col cols="9">
        <v-sheet height="700" rounded class="ma-3 pa-3">
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
                <tr>
                  <th scope="row">1</th>
                  <td>$ITEM1</td>
                  <td>93</td>
                  <td>$</td>
                  <td>22.68%</td>
                  <td>$</td>
                  <td>-16.42%</td>
                  <td>17.42%</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>$ITEM2</td>
                  <td>150</td>
                  <td>$</td>
                  <td>20.28%</td>
                  <td>$</td>
                  <td>-12.01%</td>
                  <td>16.41%</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>$ITEM3</td>
                  <td>86</td>
                  <td>$</td>
                  <td>5.62%</td>
                  <td>$</td>
                  <td>-16.84%</td>
                  <td>4.3%</td>
                </tr>
                <tr>
                  <th scope="row">4</th>
                  <td>$ITEM4</td>
                  <td>55</td>
                  <td>$</td>
                  <td>16.87%</td>
                  <td>$</td>
                  <td>1.91%</td>
                  <td>15.82%</td>
                </tr>
                <tr>
                  <th scope="row">5</th>
                  <td>$ITEM5</td>
                  <td>84</td>
                  <td>$</td>
                  <td>5.15%</td>
                  <td>$</td>
                  <td>24.72%</td>
                  <td>5.91%</td>
                </tr>
                <tr>
                  <th scope="row">6</th>
                  <td>$ITEM6</td>
                  <td>80</td>
                  <td>$</td>
                  <td>8.08%</td>
                  <td>$</td>
                  <td>-16.42%</td>
                  <td>6.76%</td>
                </tr>                
                <tr>
                  <th scope="row">7</th>
                  <td>$ITEM7</td>
                  <td>9</td>
                  <td>$</td>
                  <td>1.75%</td>
                  <td>$</td>
                  <td>39.53%</td>
                  <td>2.25%</td>
                </tr>
                <tr>
                  <th scope="row">8</th>
                  <td>$ITEM8</td>
                  <td>350</td>
                  <td>$</td>
                  <td>19.57%</td>
                  <td>$</td>
                  <td>70.15%</td>
                  <td>30.78%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue"

export default defineComponent({
  name: "AppContent",

  components: {
    PortfolioDashboard
  },

  data() {
    return {
      //
    };
  },
});
</script>

<style>
tbody tr {
   line-height: 30px;
   min-height: 30px;
   height: 30px;
}
</style>
