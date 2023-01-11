<template>
  <div>
    <v-app-bar elevation="2" color="white">
      <v-container>
        <v-row justify="center" align="center">
          <v-card flat>
            <v-card-actions>
              <v-btn
                :disabled="$store.state.portfolios.length === 0"
                text
                @click="deletePortfolio()"
              >
                Delete
              </v-btn>
            </v-card-actions>
          </v-card>
          <v-card v-if="portfolios.length > 4" flat width="400">
            <v-tabs show-arrows fixed-tabs v-model="selectedPortfolio">
              <v-tab
                v-for="portfolio in portfolios"
                :key="portfolio"
                width="100"
                @click="changePortfolio(portfolio)"
                :href="getPortfolioTabLink(portfolio)"
              >
                {{ portfolio.name }}
              </v-tab>
            </v-tabs>
          </v-card>
          <v-card v-else flat width="400">
            <v-tabs fixed-tabs v-model="selectedPortfolio">
              <v-tab
                v-for="portfolio in portfolios"
                :key="portfolio"
                width="100"
                @click="changePortfolio(portfolio)"
                :href="getPortfolioTabLink(portfolio)"
              >
                {{ portfolio.name }}
              </v-tab>
            </v-tabs>
          </v-card>
          <v-card flat>
            <v-card-actions>
              <v-btn text @click="addPortfolio()"> Add </v-btn>
            </v-card-actions>
          </v-card>
        </v-row>
      </v-container>
      <v-btn
        class="absolute right-0 pr-3"
        href="/accounts/logout/"
        @click="logout"
      >
        Logout
      </v-btn>
    </v-app-bar>
    <AddPortfolioDialog
      :addPortfolioDialog="addPortfolioDialog"
      @portfolioAdded="handlePortfolioAdded"
      @portfolioAddingCanceled="handlePortfolioAddingCanceled"
    />
    <DeletePortfolioDialog
      :portfolio="$store.state.portfolio"
      :deletePortfolioDialog="deletePortfolioDialog"
      @portfolioDeletionCanceled="handlePortfolioDeletionCanceled"
      @portfolioDeletionConfirmed="handlePortfolioDeletionConfirmed"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Portfolio } from "../common/models";
import AddPortfolioDialog from "./Home/AddPortfolioDialog.vue";
import DeletePortfolioDialog from "./Home/DeletePortfolioDialog.vue";
import { axios } from "../common/api.service";
import { toastError, toastSuccess } from "../common/api.toast";

export default defineComponent({
  name: "AppBar",

  components: {
    AddPortfolioDialog,
    DeletePortfolioDialog,
  },

  data: () => ({
    portfolios: [] as Array<Portfolio>,
    selectedPortfolio: -1 as number,
    addPortfolioDialog: false as Boolean,
    deletePortfolioDialog: false as Boolean,
  }),
  methods: {
    addPortfolio() {
      this.addPortfolioDialog = true;
    },

    deletePortfolio() {
      this.deletePortfolioDialog = true;
    },

    async handlePortfolioAdded(portfolio: Portfolio) {
      if (await this.performPortfolioCreateRequest(portfolio)) {
        this.$store.commit("setPortfolio", portfolio);
        this.portfolios = await this.$store.dispatch("getPortfolios");
        await this.$router.push(this.getPortfolioTabLink(portfolio));
        await this.$router.go(0);
      }
      this.addPortfolioDialog = false;
    },

    async performPortfolioCreateRequest(
      portfolio: Portfolio
    ): Promise<Boolean> {
      let endpoint = "/api/v1/portfolios/";
      let method = "POST";
      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: portfolio,
        });
        portfolio.id = response.data.uupid;
        portfolio.slug = response.data.slug;
        toastSuccess("Portfolio created.", 3000);

        return true;
      } catch (e: any) {
        console.error(e.response.statusText);
        toastError("Portfolio was not created.", 3000);

        return false;
      }
    },

    handlePortfolioAddingCanceled() {
      this.addPortfolioDialog = false;
    },

    async handlePortfolioDeletionConfirmed(portfolio: Portfolio) {
      if (await this.performPortfolioDeleteRequest(portfolio)) {
        this.portfolios = this.portfolios.filter(
          (val) => val.id !== portfolio.id
        );        
        await this.$store.commit("setPortfolios", this.portfolios);
        if (this.portfolios.length > 0) {
          let portfolio = this.portfolios[Math.max(this.selectedPortfolio - 1, 0)];
          await this.$store.commit("setPortfolio", portfolio);
          await this.$router.replace(this.getPortfolioTabLink(portfolio));
          await this.$router.go(0);
        } else {          
          await this.$store.commit("setPortfolio", {});
          await this.$router.replace(this.$route.path);
          await this.$router.go(0);          
        }
      }
      this.deletePortfolioDialog = false;
    },

    async performPortfolioDeleteRequest(
      portfolio: Portfolio
    ): Promise<Boolean> {
      let endpoint = `/api/v1/portfolios/${portfolio.slug}/`;
      let method = "DELETE";
      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: portfolio,
        });
        toastSuccess("Portfolio deleted.", 3000);

        return true;
      } catch (e: any) {
        console.error(e.response.statusText);
        toastError("Portfolio was not deleted.", 3000);

        return false;
      }
    },

    handlePortfolioDeletionCanceled() {
      this.deletePortfolioDialog = false;
    },

    getPortfolioTabLink(portfolio: Portfolio): string {
      if (this.$route.path === "/") {
        return this.$route.path + portfolio.slug + "/";
      } else {
        return (
          this.$route.path + "/" + portfolio.slug + "/"
        );
      }
    },

    changePortfolio(portfolio: Portfolio) {
      this.$store.commit("setPortfolio", portfolio);
    },

    logout() {
      this.$store.commit("setPortfolios", []);
      this.$store.commit("setPortfolio", {});
    },

    toastError,
    toastSuccess,
  },

  async created() {
    this.portfolios = await this.$store.state.portfolios;
    if (this.portfolios.length > 0) {
      if (this.$route.query.slug !== undefined) {
        this.selectedPortfolio = this.portfolios.findIndex(
          (portfolio) => portfolio.slug === this.$route.query.slug
        );
      } else {
        this.selectedPortfolio = 0;
      }
    } else {
      this.selectedPortfolio = -1;
    }
  },
});
</script>