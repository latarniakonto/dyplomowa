<template>
  <div class="">
    <h5>
      Portfolio name
      <small class="text-muted">Year</small>
    </h5>
    <v-select
      label="Year"
      :items="[2022, 2021, 2020]"
      model-value="2022"
      class="mb-2"
      style="height: 60px"
    ></v-select>
    <div class="nav-tabs-container">
      <ul
        class="nav nav-tabs mb-2 dashboard-nav"
        id="dashboard-nav-tabs"
        role="tablist"
      >
        <li class="nav-item dashboard-tab" role="presentation">
          <button
            class="nav-link"
            :class="{ active: resourcesTabActive }"
            @click="resourcesTabActive = toggleTabs()"
            id="resources-tab"
            data-bs-toggle="tab"
            data-bs-target="#resources"
            type="button"
            role="tab"
            aria-controls="resources"
            :aria-selected="resourcesTabActive"
          >
            Resources
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link dashboard-tab"
            :class="{ active: performanceTabActive }"
            @click="performanceTabActive = toggleTabs()"
            id="performance-tab"
            data-bs-toggle="tab"
            data-bs-target="#performance"
            type="button"
            role="tab"
            aria-controls="performance"
            :aria-selected="performanceTabActive"
          >
            Performance
          </button>
          <button
            class="nav-link dashboard-tab"
            :class="{ active: otherTabActive }"
            @click="otherTabActive = toggleTabs()"
            id="other-tab"
            data-bs-toggle="tab"
            data-bs-target="#other"
            type="button"
            role="tab"
            aria-controls="other"
            :aria-selected="otherTabActive"
          >
            Other
          </button>
        </li>
      </ul>
    </div>
    <div class="tab-content" id="dashboard-tabs-content">
      <div
        class="tab-pane fade show"
        :class="{ active: resourcesTabActive }"
        id="resources"
        role="tabpanel"
        aria-labelledby="resources-tab"
      >
        <resources-tab />
      </div>
      <div
        class="tab-pane fade show"
        :class="{ active: performanceTabActive }"
        id="performance"
        role="tabpanel"
        aria-labelledby="performance-tab"
      >
      </div>
      <div
        class="tab-pane fade show"
        :class="{ active: otherTabActive }"
        id="other"
        role="tabpanel"
        aria-labelledby="other-tab"
      ></div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ResourcesTab from "./ResourcesTab.vue";

export default defineComponent({
  name: "PortfolioDashboard",

  components: {
    ResourcesTab,
  },

  data() {
    return {
      resourcesTabActive: true as Boolean,
      performanceTabActive: false as Boolean,
      otherTabActive: false as Boolean,
    };
  },

  methods: {
    toggleTabs: function (newActiveTab: Boolean): Boolean {
      this.resourcesTabActive = false;
      this.performanceTabActive = false;
      this.otherTabActive = false;
      return true;
    },
  },
});
</script>

<style>
.dashboard-nav .nav-item .nav-link.active {
  background-color: #f6f6f6;
  color: rgba(0, 0, 0, 0.87);
  border-color: #a4a4a4;
  border-bottom-color: white;
}

.dashboard-nav .nav-item .nav-link {
  /* background-color: white; */
  color: gray;
  border-bottom-color: #a4a4a4;
}

.nav-tabs-container
.nav-tabs
.nav-link:hover:not(.dashboard-nav .nav-item .nav-link.active) {
  background-color: #f6f6f6;
  border-bottom-color: #a4a4a4;
}

.nav-tabs-container .nav-tabs {
  border-bottom-color: #a4a4a4;
  justify-content: space-between;
}

.nav  li  button {
  padding-top: 6px;
  padding-bottom: 6px;
  padding-left: 4px;
  padding-right: 4px;
  text-align: center;
  display: inline-flex;
  
}
</style>
