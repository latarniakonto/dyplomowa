<template>
  <v-app class="app-main">
    <v-main>
      <Toast/>
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Toast from 'primevue/toast';

export default defineComponent({
  name: "App",

  components: {
    Toast
  },

  data() {
    return {
      //
    };
  },
});
</script>

<style>
  .app-main {
    background-color: gainsboro;
  }
</style>