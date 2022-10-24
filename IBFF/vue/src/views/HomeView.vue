<template>
  <app-bar/>
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import AppBar from "../components/AppBar.vue";

export default defineComponent({
  name: "HomeView",

  components: {
    AppBar,
  },
});
</script>
