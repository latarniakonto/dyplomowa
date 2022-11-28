<template>
  <div class="tiles">
    <div class="asset-info-tile mb-2 mr-2" @click="toggleAssetInfoTile(0)">
      <div class="mb-2">
        <span class="font-medium text-xl">Current Price</span>
      </div>
      <div v-if="!assetInfoTiles[0]">
        <span class="text-bluegray-900 text-2xl">
          {{ asset.currentPrice }}</span
        >
      </div>
      <div v-else class="p-inputgroup" @click="$event.stopPropagation()">
        <InputNumber
          id="price"
          v-bind:modelValue="asset.currentPrice"
          mode="decimal"
          :min="0.001"
          :maxFractionDigits="3"
          autofocus
          required="true"
        />
        <span class="p-inputgroup-addon">PLN</span>
      </div>
    </div>
    <div class="asset-info-tile mb-2 mr-2" @click="toggleAssetInfoTile(1)">
      <div class="mb-2">
        <span class="font-medium text-xl">Total</span>
      </div>
      <div v-if="!assetInfoTiles[1]">
        <span class="text-bluegray-900 text-2xl"> {{ asset.total }}</span>
      </div>
      <div v-else class="p-inputgroup" @click="$event.stopPropagation()">
        <InputNumber
          id="total"
          v-bind:modelValue="asset.total"
          integeronly
          autofocus
          required="true"
        />
        <span class="p-inputgroup-addon">No.</span>
      </div>
    </div>
    <div class="asset-info-tile mb-2" @click="toggleAssetInfoTile(2)">
      <div class="mb-2">
        <span class="font-medium text-xl">Profit/Loss</span>
      </div>
      <div v-if="!assetInfoTiles[2]">
        <span class="text-bluegray-900 text-2xl"> {{ asset.gain }}</span>
      </div>
      <div v-else class="p-inputgroup" @click="$event.stopPropagation()">
        <InputNumber
          id="gain"
          v-bind:modelValue="asset.gain"
          mode="decimal"
          autofocus
          required="true"
        />
        <span class="p-inputgroup-addon">%</span>
      </div>
    </div>
    <div class="asset-info-tile mb-2 mr-2" @click="toggleAssetInfoTile(3)">
      <div class="mb-2">
        <span class="font-medium text-xl">Initial Weight</span>
      </div>
      <div v-if="!assetInfoTiles[3]">
        <span class="text-bluegray-900 text-2xl">
          {{ asset.initialWeight }}</span
        >
      </div>
      <div v-else class="p-inputgroup" @click="$event.stopPropagation()">
        <InputNumber
          id="init-weight"
          v-bind:modelValue="asset.initialWeight"
          autofocus
          required="true"
        />
        <span class="p-inputgroup-addon">%</span>
      </div>
    </div>
    <div class="asset-info-tile mb-2 mr-2" @click="toggleAssetInfoTile(4)">
      <div class="mb-2">
        <span class="font-medium text-xl">Current Weight</span>
      </div>
      <div v-if="!assetInfoTiles[4]">
        <span class="text-bluegray-900 text-2xl">
          {{ asset.currentWeight }}</span
        >
      </div>
      <div v-else class="p-inputgroup" @click="$event.stopPropagation()">
        <InputNumber
          id="curr-weight"
          v-bind:modelValue="asset.currentWeight"
          autofocus
          required="true"
        />
        <span class="p-inputgroup-addon">%</span>
      </div>
    </div>
    <div class="asset-info-tile mb-2" @click="toggleAssetInfoTile(5)">
      <div class="mb-2">
        <span class="font-medium text-xl">Buy Price</span>
      </div>
      <div v-if="!assetInfoTiles[5]">
        <span class="text-bluegray-900 text-2xl"> {{ asset.buyPrice }}</span>
      </div>
      <div v-else class="p-inputgroup" @click="$event.stopPropagation()">
        <InputNumber
          id="init-price"
          v-bind:modelValue="asset.buyPrice"
          mode="decimal"
          :min="0.001"
          :maxFractionDigits="3"
          autofocus
          required="true"
        />
        <span class="p-inputgroup-addon">PLN</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import InputNumber from "primevue/inputnumber";

export default defineComponent({
  name: "AssetInfo",

  components: {
    InputNumber,
  },

  props: {
    asset: {
      required: true,
      type: Object,
      default: {},
    },
  },

  data() {
    return {
      assetInfoTiles: [
        false,
        false,
        false,
        false,
        false,
        false,
      ] as Array<Boolean>,
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
.asset-info-tile {
  cursor: pointer;
  height: 7rem;
  width: 18.666rem;
  padding: 1rem;
  border-radius: 4px;
  box-shadow: 0 2px 1px -1px rgba(0, 0, 0, 0.2), 0 1px 1px 0 rgba(0, 0, 0, 0.14),
    0 1px 3px 0 rgba(0, 0, 0, 0.12);
  background-color: #f6f6f6;
  border-bottom-style: solid;
  border-bottom-width: 0.1rem;
  border-bottom-color: #a4a4a4;
  display: inline-block;
}

.asset-info-tile .p-inputnumber .p-inputnumber-input {
  width: 7rem;
  padding: 0.5rem;
}

.asset-info-tile .p-inputgroup-addon {
  width: 3rem;
  padding: 0.5rem;
  background-color: #ededed;
}

.asset-info-tile:hover {
  background-color: #ededed;
}

.asset-info-tile:active {
  background-color: #ededed;
  box-shadow: inset 0px 0px 6px #d3d3d3;
}
</style>
