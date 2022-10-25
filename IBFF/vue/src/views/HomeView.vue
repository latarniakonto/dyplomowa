<template>
  <app-bar/>
  <app-content/>
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import AppBar from "../components/AppBar.vue";
import AppContent from "../components/AppContent.vue";

export default defineComponent({
  name: "HomeView",

  components: {
    AppBar,
    AppContent
  },
});
</script>
