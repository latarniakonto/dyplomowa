<template>
  <v-container color="white">
    <v-row no-gutters align="start">
      <v-col cols="3">
        <v-sheet height="470" rounded class="ma-3 pa-3">
          <portfolio-dashboard/>
        </v-sheet>
      </v-col>
      <v-col cols="9">
        <v-sheet height="700" rounded class="ma-3 pa-3"> </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue"

export default defineComponent({
  name: "AppContent",

  components: {
    PortfolioDashboard
  },

  data() {
    return {
      //
    };
  },
});
</script>

<style>
</style>
