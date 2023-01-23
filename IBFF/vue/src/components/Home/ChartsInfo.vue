<template>
  <div class="charts">
    <div class="charts-header">
      <h5 class="title mb-2">Allocation</h5>
    </div>
    <div
      class="charts-content tile"
      :class="{ 'tile-active': chartsInfoTiles[0] }"
      @click="toggleChartsInfoTile(0)"
    >
      <Chart
        type="pie"
        :data="chartData"
        :options="lightOptions"
        :plugins="plugins"
        @click="$event.stopPropagation()"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Chart from "primevue/chart";
import { Asset, AssetJSON, Portfolio } from "../../common/models";
import { axios } from "../../common/api.service";

export default defineComponent({
  name: "ChartsInfo",

  components: {
    Chart,
  },

  props: {
    portfolio: {
      type: Object as () => Portfolio,
      required: true,
      default: {},
    },
  },

  data() {
    return {
      assets: [] as Array<Asset>,
      chartsInfoTiles: [false] as Array<Boolean>,
      chartData: {
        labels: [] as Array<String>,
        datasets: [] as Array<any>,
      },
      plugins: {
        colors: {
          enabled: true
        }
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
    toggleChartsInfoTile(index: number) {
      for (let i = 0; i < this.chartsInfoTiles.length; i++) {
        if (i == index) {
          continue;
        }
        this.chartsInfoTiles[i] = false;
      }

      this.chartsInfoTiles[index] = !this.chartsInfoTiles[index];
    },

    async getAssets() {
      if (this.portfolio.slug === undefined) {
        return;
      }
  
      let endpoint = `api/v1/portfolios/${this.portfolio.slug}/assets/`;

      try {
        let response = await axios.get(endpoint);

        let jsons = response.data;
        jsons.forEach((json: any) => {
          this.assets.push(new Asset(json as AssetJSON));
        });
      } catch (e: any) {
        console.error(e.response);
      }
    },

    drawChart() {      
      if (this.assets.length === 0) {
        this.chartData.labels = ["NO ASSETS"];
        this.chartData.datasets = [{ data: [100] }];
        return;
      }

      this.chartData.labels = [];
      this.chartData.datasets = [];
      let allocation: number[] = [];
      this.assets.forEach((asset: Asset) => {
        this.chartData.labels.push(asset.ticker);
        allocation.push(Math.round(asset.currentWeight * 1000) / 10);
      });
      this.chartData.datasets = [{
        data: allocation
      }];
    },
  },

  async created() {
    await this.getAssets();
    this.drawChart();
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

.tile:hover {
  background-color: #ededed;
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
