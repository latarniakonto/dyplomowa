<template>
  <v-container color="white">
    <v-row no-gutters align="start">
      <v-col cols="2">
        <v-sheet height="450" rounded class="ma-3 pa-3"> </v-sheet>
      </v-col>
      <v-col cols="10">
        <v-sheet height="700" rounded class="ma-3 pa-3"> </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "AppContent",
});
</script>
