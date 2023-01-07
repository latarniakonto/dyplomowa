<template>
  <div class="card">
    <AssetsTable
      :assets="assets"
      @currentPriceChanged="handleCurrentPriceChanged"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AssetsTable from "./AssetsTable.vue";
import { Asset, AssetJSON } from "../../common/models";
import { axios } from "../../common/api.service";

export default defineComponent({
  name: "HomeTab",

  components: {
    AssetsTable,
  },

  data() {
    return {
      assets: [] as Array<Asset>,      
    };
  },

  methods: {
    async getAssets() {
      let endpoint = `api/v1/portfolios/${this.$store.state.portfolio.slug}/assets/`;

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

    handleCurrentPriceChanged(asset: number, currentPrice: number) {
      if (asset === undefined) {
        return;
      }
      this.performCurrentPriceChangedRequest(asset, currentPrice)
      this.assets[asset].currentPrice = currentPrice;

      this.assets[asset].currentValue =
        this.assets[asset].currentPrice * this.assets[asset].total;
      this.assets[asset].gain =
        this.assets[asset].currentPrice / this.assets[asset].initialPrice - 1;

      let totalCurrentValue = 0;
      for (let i = 0; i < this.assets.length; i++) {
        totalCurrentValue += this.assets[i].currentValue;
      }

      for (let i = 0; i < this.assets.length; i++) {
        this.assets[i].currentWeight =
          this.assets[i].currentValue / totalCurrentValue;
      }
    },

    async performCurrentPriceChangedRequest(asset: number, currentPrice: number) {
      let assetSlug = this.assets[asset].slug;
      let endpoint = `/api/v1/assets/${assetSlug}/`;
      let method = "PATCH";

      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: { currentPrice: currentPrice },
        });
        return true;
      } catch (e: any) {
        console.error(e.response.statusText);
        return false;
      }
    },
  },

  created() {
    this.getAssets();
  },
});
</script>

<style>
</style>
