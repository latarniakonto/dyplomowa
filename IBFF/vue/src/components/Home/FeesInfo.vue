<template>
  <div class="fees">
    <h5 class="mb-2 title">Fees</h5>
    <div
      class="tile mb-2"
      :class="{ 'tile-active': feesInfoTiles[0] }"
      @click="toggleFeesInfoTile(0)"
    >
      <div class="mb-2">
        <span class="title">Number of Transactions</span>
      </div>
      <div>
        <span class="text-bluegray-900 value">
          {{ getPrintableValue(portfolio.transactionsCounter, 0) }}
        </span>
      </div>
    </div>
    <div
      class="tile mb-2"
      :class="{ 'tile-active': feesInfoTiles[1] }"
      @click="toggleFeesInfoTile(1)"
    >
      <div class="mb-2">
        <span class="title">Transactions Cost</span>
      </div>
      <div>
        <span class="text-bluegray-900 value">
          {{ getPrintableValue(portfolio.transactionsCost, 2) }}
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { getPrintableValue } from "../../common/models";

export default defineComponent({
  name: "FeesInfo",

  components: {},

  props: {
    portfolio: {
      type: Object,
      required: true,
      default: {},
    },
  },

  data() {
    return {
      feesInfoTiles: [false, false] as Array<Boolean>,
    };
  },

  methods: {
    toggleFeesInfoTile(index: number) {
      for (let i = 0; i < this.feesInfoTiles.length; i++) {
        if (i == index) {
          continue;
        }
        this.feesInfoTiles[i] = false;
      }

      this.feesInfoTiles[index] = !this.feesInfoTiles[index];
    },

    getPrintableValue,
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

.fees {
  display: inline-block;
  width: 18.66rem;
}

.fees h5.title {
  border-bottom: solid 2px;
  border-bottom-color: #a4a4a4;
  padding-left: 0.5rem;
  padding-bottom: 0.5rem;
}

.fees span.title {
  font-weight: 500;
  font-size: 1.25rem;
}

.fees span.value {  
  font-size: 1.5rem;
}
</style>
