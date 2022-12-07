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
        @click="$event.stopPropagation()"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Chart from "primevue/chart";

export default defineComponent({
  name: "ChartsInfo",

  components: {
    Chart,
  },

  data() {
    return {
      chartsInfoTiles: [false] as Array<Boolean>,
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
    toggleChartsInfoTile(index: number) {
      for (let i = 0; i < this.chartsInfoTiles.length; i++) {
        if (i == index) {
          continue;
        }
        this.chartsInfoTiles[i] = false;
      }

      this.chartsInfoTiles[index] = !this.chartsInfoTiles[index];
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
