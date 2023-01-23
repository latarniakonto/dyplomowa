import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import { Portfolio, PortfolioJSON } from "../common/models";
import { axios } from "../common/api.service";

export default createStore({
  plugins: [createPersistedState({
    storage: window.sessionStorage
  })],

  state: {
    portfolio: {} as Portfolio,
    portfolios: [] as Array<Portfolio>,
    selectedPortfolio: -1 as number,
  },

  getters: {},

  mutations: {
    setPortfolio(state: any, portfolio: Portfolio) {
      state.portfolio = portfolio;
      state.selectedPortfolio = state.portfolios.indexOf(state.portfolio);      
    },

    setPortfolios(state: any, portfolios: Array<Portfolio>) {
      state.portfolios = portfolios;
    },
  },

  actions: {
    async getPortfolios({ commit }, slug: String): Promise<Boolean> {
      let endpoint = "api/v1/portfolios/";

      try {
        let response = await axios.get(endpoint);
        let jsons = response.data as PortfolioJSON[];

        let portfolios: Array<Portfolio> = [];
        jsons.forEach((json: any) => {
          portfolios.push(new Portfolio(json));
        });        
        if (portfolios.length > 0) {
          commit("setPortfolios", portfolios);
          if (slug === undefined) {            
            commit("setPortfolio", portfolios[0]);
          } else {
            commit(
              "setPortfolio",
              portfolios[
                portfolios.findIndex(
                  (portfolio: Portfolio) => portfolio.slug === slug
                )
              ]
            );
          }
        } else {
          commit("setPortfolio", {});
        }

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

        let portfolio: Portfolio = {} as Portfolio;
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
