<template>
  <v-app-bar elevation="2" color="white">
    <v-container>
      <v-row justify="center" align="center">
        <v-card flat>
          <v-card-actions>
            <v-btn :disabled="tabs.length <= 1" text @click="removeTab()">
              Remove
            </v-btn>
          </v-card-actions>
        </v-card>
        <v-card v-if="tabs.length > 4" flat width="400">
          <v-tabs show-arrows fixed-tabs v-model="selectedTab">
            <v-tab v-for="i in tabs" :key="i" :href="'#tab-' + i" width="100">
              Item {{ i }}
            </v-tab>
          </v-tabs>
        </v-card>
        <v-card v-else flat width="400">
          <v-tabs fixed-tabs v-model="selectedTab">
            <v-tab v-for="i in tabs" :key="i" :href="'#tab-' + i" width="100">
              Item {{ i }}
            </v-tab>
          </v-tabs>
        </v-card>
        <v-card flat>
          <v-card-actions>
            <v-btn text @click="addTab()"> Add </v-btn>
          </v-card-actions>
        </v-card>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "AppBar",
  data: () => ({
    tabs: [1] as Array<number>,
    selectedTab: 1 as number,
  }),
  methods: {
    addTab: function () {
      this.tabs.push(this.tabs.length + 1);
      this.selectedTab = this.tabs.length - 1;
    },
    removeTab: function () {
      this.tabs.splice(this.selectedTab, 1);
      this.tabs.forEach((tab, index) => {
        this.tabs[index] = index + 1;
      });
      this.selectedTab--;
    },
  },
});
</script>
