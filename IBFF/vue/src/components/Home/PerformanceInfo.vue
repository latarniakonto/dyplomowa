<template>
  <div class="performance">
    <h5 class="mb-2 title">Performance</h5>
    <div
      class="tile mb-2"
      :class="{ 'tile-active': performanceInfoTiles[0] }"
      @click="togglePerformanceInfoTile(0)"
    >
      <div class="mb-2">
        <span class="font-medium text-xl">Annual Gain</span>
      </div>
      <div>
        <span class="text-bluegray-900 text-2xl">{{ portfolio.annualGain }}</span>
      </div>
    </div>
    <div
      class="tile mb-2"
      :class="{ 'tile-active': performanceInfoTiles[1] }"
      @click="togglePerformanceInfoTile(1)"
    >
      <div class="mb-2">
        <span class="font-medium text-xl">Annual Yield</span>
      </div>
      <div>
        <span class="text-bluegray-900 text-2xl">{{ portfolio.annualYield }}</span>
      </div>
    </div>
    <div
      class="tile mb-2"
      :class="{ 'tile-active': performanceInfoTiles[2] }"
      @click="togglePerformanceInfoTile(2)"
    >
      <div class="mb-2">
        <span class="font-medium text-xl">Total Annual Dividends</span>
      </div>
      <div>
        <span class="text-bluegray-900 text-2xl">{{ portfolio.annualDividends }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "PerformanceInfo",

  components: {},

  props: {
    portfolio: {
      type: Object,
      required: true,
      default: {}
    }
  },

  data() {
    return {
      performanceInfoTiles: [false, false, false] as Array<Boolean>,
    };
  },

  methods: {
    togglePerformanceInfoTile(index: number) {
      for (let i = 0; i < this.performanceInfoTiles.length; i++) {
        if (i == index) {
          continue;
        }
        this.performanceInfoTiles[i] = false;
      }

      this.performanceInfoTiles[index] = !this.performanceInfoTiles[index];
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
</style>
