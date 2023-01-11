<template>
  <div>
    <AppBar />
    <AppContent :content="content" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import AppBar from "../components/AppBar.vue";
import AppContent from "../components/AppContent.vue";

export default defineComponent({
  name: "AppView",

  components: {
    AppBar,
    AppContent
  },

  props: {
    content: {
      type: String,
      required: true,
      default: ""
    }
  },
});
</script>
