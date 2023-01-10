import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import { Portfolio, PortfolioJSON } from "../common/models";
import { axios } from "../common/api.service";

export default createStore({
  plugins: [createPersistedState()],

  state: {
    portfolio: new Object() as Portfolio,
    portfolios: [] as Array<Portfolio>
  },

  getters: {},
  
  mutations: {
    setPortfolio(state: any, portfolio: Portfolio) {
      state.portfolio = portfolio;
    },
    
    setPortfolios(state: any, portfolios: Array<Portfolio>) {
      state.portfolios = portfolios;
    }
  },

  actions: {
    async getPortfolios({ commit }): Promise<Boolean> {
      let endpoint = "api/v1/portfolios/";

      try {
        let response = await axios.get(endpoint);
        let jsons = response.data as PortfolioJSON[];

        let portfolios: Array<Portfolio> = [];
        portfolios.push(new Portfolio(jsons[0]));
        commit("setPortfolios", portfolios);
        commit("setPortfolio", portfolios[0]);

        return true;
      } catch (e: any) {
        console.error(e.response);

        return false;
      }
    },

    async getPortfolio({ commit, state }): Promise<Boolean> {
      let endpoint = `api/v1/portfolios/${state.portfolio.slug}/`;

      try {
        let response = await axios.get(endpoint);
        let json = response.data as PortfolioJSON;

        let portfolio: Portfolio = new Object() as Portfolio;
        portfolio = new Portfolio(json);
        commit("setPortfolio", portfolio);

        return true;
      } catch (e: any) {
        console.error(e.response);

        return false;
      }
    },
  },

  modules: {},
});
