<template>
  <div class="portfolio-dashboard">
    <div class="dashboard-header">
      <h4 class="mb-3">Portfolio name</h4>
    </div>
    <div class="dashboard-content">
      <div class="d-inline-block">
        <ResourcesInfo class="mr-4 mb-3" />
        <div class="fees mr-4 mb-3">
          <h5 class="mb-2 title">Fees</h5>
          <div
            class="tile mb-2"
            :class="{ 'tile-active': assetInfoTiles[2] }"
            @click="toggleAssetInfoTile(2)"
          >
            <div class="mb-2">
              <span class="font-medium text-xl">Number of Transactions</span>
            </div>
            <div>
              <span class="text-bluegray-900 text-2xl">9</span>
            </div>
          </div>
          <div
            class="tile mb-2"
            :class="{ 'tile-active': assetInfoTiles[3] }"
            @click="toggleAssetInfoTile(3)"
          >
            <div class="mb-2">
              <span class="font-medium text-xl">Transactions Cost</span>
            </div>
            <div>
              <span class="text-bluegray-900 text-2xl">120</span>
            </div>
          </div>
        </div>
        <div class="charts">
          <div class="charts-header">
            <h5 class="title mb-2">Allocation</h5>
          </div>
          <div
            class="charts-content tile"
            :class="{ 'tile-active': assetInfoTiles[8] }"
            @click="toggleAssetInfoTile(8)"
          >
            <Chart
              type="pie"
              :data="chartData"
              :options="lightOptions"
              @click="$event.stopPropagation()"
            />
          </div>
        </div>
      </div>
      <div class="d-inline-block align-top">
        <div class="performance">
          <h5 class="mb-2 title">Performance</h5>
          <div
            class="tile mb-2"
            :class="{ 'tile-active': assetInfoTiles[6] }"
            @click="toggleAssetInfoTile(6)"
          >
            <div class="mb-2">
              <span class="font-medium text-xl">Annual Gain</span>
            </div>
            <div>
              <span class="text-bluegray-900 text-2xl">47000</span>
            </div>
          </div>
          <div
            class="tile mb-2"
            :class="{ 'tile-active': assetInfoTiles[5] }"
            @click="toggleAssetInfoTile(5)"
          >
            <div class="mb-2">
              <span class="font-medium text-xl">Annual Yield</span>
            </div>
            <div>
              <span class="text-bluegray-900 text-2xl">156.67%</span>
            </div>
          </div>
          <div
            class="tile mb-2"
            :class="{ 'tile-active': assetInfoTiles[7] }"
            @click="toggleAssetInfoTile(7)"
          >
            <div class="mb-2">
              <span class="font-medium text-xl">Total Annual Dividends</span>
            </div>
            <div>
              <span class="text-bluegray-900 text-2xl">1200</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Chart from "primevue/chart";
import ResourcesInfo from "./ResourcesInfo.vue";

export default defineComponent({
  name: "PortfolioDashboard",

  components: {
    Chart,
    ResourcesInfo
  },

  data() {
    return {
      items: [
        { label: "Home", icon: "bi bi-house" },
        { label: "Assets", icon: "bi bi-wallet2" },
        { label: "Transactions", icon: "bi bi-cash-coin" },
        { label: "Operations", icon: "bi bi-boxes" },
      ],
      assetInfoTiles: [
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
      ] as Array<Boolean>,
      chartData: {
        labels: ["A", "B", "C"],
        datasets: [
          {
            data: [20, 1, 79],
            backgroundColor: ["#42A5F5", "#66BB6A", "#FFA726"],
            hoverBackgroundColor: ["#64B5F6", "#81C784", "#FFB74D"],
          },
        ],
      },
      lightOptions: {
        plugins: {
          legend: {
            labels: {
              color: "#495057",
            },
          },
        },
      },
    };
  },

  methods: {
    toggleAssetInfoTile(index: number) {
      for (let i = 0; i < this.assetInfoTiles.length; i++) {
        if (i == index) {
          continue;
        }
        this.assetInfoTiles[i] = false;
      }

      this.assetInfoTiles[index] = !this.assetInfoTiles[index];
    },
  },
});
</script>

<style>
.tile {
  cursor: pointer;
  height: 7rem;
  width: 18.666rem;
  padding: 1rem;
  border-radius: 4px;
  box-shadow: 0 2px 1px -1px rgba(0, 0, 0, 0.2), 0 1px 1px 0 rgba(0, 0, 0, 0.14),
    0 1px 3px 0 rgba(92, 76, 76, 0.12);
  background-color: #f6f6f6;
  border-bottom-style: solid;
  border-bottom-width: 0.1rem;
  border-bottom-color: #a4a4a4;
  display: inline-block;
}

.tile.tile-active {
  background-color: #ededed;
  box-shadow: inset 0px 0px 6px #d3d3d3;
}

.tile .p-inputnumber .p-inputnumber-input {
  width: 7rem;
  padding: 0.5rem;
}

.tile .p-inputnumber.input-blocked .p-inputnumber-input {
  border: 1px solid rgba(0, 0, 0, 0.38);
  cursor: default;
  background: rgba(255, 255, 255, 0.38);
  color: rgba(0, 0, 0, 0.38);
}

.tile .p-inputnumber.input-blocked .p-inputnumber-input:focus {
  border: 1px solid rgba(0, 0, 0, 0.38);
  background: rgba(255, 255, 255, 0.38);
  color: rgba(0, 0, 0, 0.38);
  box-shadow: none;
}

.tile .p-inputgroup-addon {
  width: 3rem;
  padding: 0.5rem;
  background-color: #ededed;
}

.tile:hover {
  background-color: #ededed;
}

.fees {
  display: inline-block;
  width: 18.66rem;
}

.fees .title {
  border-bottom: solid 2px;
  border-bottom-color: #a4a4a4;
  padding-left: 0.5rem;
  padding-bottom: 0.5rem;
}

.performance {
  display: inline-block;
  width: 18.66rem;
}

.performance .title {
  border-bottom: solid 2px;
  border-bottom-color: #a4a4a4;
  padding-left: 0.5rem;
  padding-bottom: 0.5rem;
}

.portoflio-dashboard {
  display: flex;
}

.charts {
  width: 19.16rem;
  display: block;
  padding-left: 0.5rem;
}

.charts .charts-content {
  width: 18.66rem;
  height: 18.66rem;
}

.charts .title {
  border-bottom: solid 2px;
  border-bottom-color: #a4a4a4;
  padding-left: 0.5rem;
  padding-bottom: 0.5rem;
}
</style>
