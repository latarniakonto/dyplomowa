<template>
  <div class="operations-tab mb-2">
    <div class="card">
      <div class="table-toolbar">
        <Toolbar class="mb-4">
          <template #start>
            <Button
              label="Dividend"
              icon="pi pi-plus"
              class="p-button-success mr-2"
              @click="addDividend()"
            />
          </template>
        </Toolbar>
      </div>
      <DividendsTable
        :dividends="dividends"
        @dividendDeleted="handleDividendDeleted"
      />
    </div>
    <AddDividendDialog
      :addDividendDialog="addDividendDialog"
      :assets="assets"
      @dividendAdded="handleDividendAdded($event)"
      @dividendAddingCanceled="handleDividendAddingCanceled()"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import Toolbar from "primevue/toolbar";
import RadioButton from "primevue/radiobutton";
import DividendsTable from "./DividendsTable.vue";
import AddDividendDialog from "./AddDividendDialog.vue";
import { Asset, AssetJSON, Dividend, DividendJSON } from "../../common/models";
import { axios } from "../../common/api.service";
import { toastSuccess, toastError } from "../../common/api.toast";

export default defineComponent({
  name: "OperationsTab",

  components: {
    Button,
    Toolbar,
    RadioButton,
    DividendsTable,
    AddDividendDialog,
  },

  data() {
    return {
      addDividendDialog: false as Boolean,
      assets: [] as Array<Asset>,      
      dividends: [] as Array<Dividend>,
    };
  },

  methods: {
    addDividend() {
      this.addDividendDialog = true;
    },

    async handleDividendAdded(dividend: Dividend) {
      dividend.asset = this.assets.find(
        (asset: Asset) => asset.ticker === dividend.ticker
      ) as Asset;      
      if (await this.performDividendCreateRequest(dividend)) {
        this.dividends.push(dividend);
      }
      this.addDividendDialog = false;
    },

    async handleDividendDeleted(dividend: Dividend, index: number) {
      if (await this.performDividendDeleteRequest(dividend)) {
        this.dividends.splice(index, 1);
      }
    },

    handleDividendAddingCanceled() {
      this.addDividendDialog = false;
    },

    async getDividends() {
      let endpoint = `api/v1/portfolios/${this.$store.state.portfolio.slug}/dividends/`;

      try {
        let response = await axios.get(endpoint);
        let jsons = response.data;
        jsons.forEach((json: any) => {
          this.dividends.push(new Dividend(json as DividendJSON));
        });
      } catch (e: any) {
        console.error(e.response);
      }
    },

    async getAssets() {
      let endpoint = `api/v1/portfolios/${this.$store.state.portfolio.slug}/assets/`;

      try {
        let response = await axios.get(endpoint);
        let jsons = response.data;

        jsons = response.data;
        jsons.forEach((json: any) => {
          this.assets.push(new Asset(json as AssetJSON));
        });
      } catch (e: any) {
        console.error(e.response);
      }
    },

    async performDividendCreateRequest(dividend: Dividend): Promise<Boolean> {
      let endpoint = "/api/v1/dividends/";
      let method = "POST";            
      try {        
        const response = await axios({
          method: method,
          url: endpoint,
          data: dividend
        });        
        dividend.id = response.data.uuoid;
        dividend.slug = response.data.slug;
        toastSuccess("Dividend created.", 3000);

        return true;
      } catch (e: any) {
        console.error(e.response.statusText);
        toastError("Dividend was not created.", 3000);

        return false;
      }
    },

    async performDividendDeleteRequest(dividend: Dividend): Promise<Boolean> {
      let endpoint = `/api/v1/dividends/${dividend.slug}/`;
      let method = "DELETE";      
      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: dividend
        });        
        toastSuccess("Dividend deleted.", 3000);

        return true;
      } catch (e: any) {
        console.error(e.response.statusText);
        toastError("Dividend was not deleted.", 3000);

        return false;
      }
    },
  },

  async created() {
    await this.getDividends();
    this.getAssets();
  },
});
</script>

<style>
.operations-tab .table-toolbar {
  background-color: #f6f6f6;
  height: 60px;
}

.operations-tab .table-toolbar .p-toolbar {
  background-color: #f6f6f6;
  border-color: #a4a4a4;
  padding: 0.3rem 0 0 0.3rem;
}

.operations-tab .toolbar-tile {
  cursor: pointer;
  padding: 0.714rem 1rem;
  border-radius: 4px;
  box-shadow: 0 2px 1px -1px rgba(0, 0, 0, 0.2), 0 1px 1px 0 rgba(0, 0, 0, 0.14),
    0 1px 3px 0 rgba(92, 76, 76, 0.12);
  background-color: #f6f6f6;
  border-bottom-style: solid;
  border-bottom-width: 0rem;
  border-bottom-color: #a4a4a4;
}

.operations-tab .toolbar-tile.tile-active {
  background-color: #ededed;
  box-shadow: inset 0px 0px 6px #d3d3d3;
}

.operations-tab .toolbar-tile:hover {
  background-color: #ededed;
}
</style>
