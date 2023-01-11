<template>
  <div class="home-tab">
    <PortfolioDashboard :portfolio="$store.state.portfolio" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PortfolioDashboard from "./PortfolioDashboard.vue";
import { Portfolio } from "../../common/models";

export default defineComponent({
  name: "HomeTab",

  components: {
    PortfolioDashboard,
  },

  data() {
    return {
      portfolio: new Object() as Portfolio
    };
  },

  methods: {
  },
});
</script>

<style>
@media (min-width: 1200px) and (max-width: 1400px) {
  .tile {    
    width: 15.666rem;    
  }

  .resources {    
    width: 32.332em;    
  }

  .resources span.title {
    font-size: 1.2rem;
  }

  .resources span.value {
    font-size: 1.25rem;
  }

  .fees {    
    width: 15.66rem;
  }

  .fees span.title {
    font-size: 1.2rem;
  }

  .fees span.value {
    font-size: 1.25rem;
  }

  .performance {    
    width: 15.66rem;
  }

  .performance span.title {
    font-size: 1.2rem;
  }

  .performance span.value {
    font-size: 1.25rem;
  }
}

@media (min-width: 992px) and (max-width: 1199px) {
  .tile {    
    width: 12.666rem;    
  }

  .resources {    
    width: 26.332em;    
  }

  .resources span.title {
    font-size: 1rem;
  }

  .resources span.value {
    font-size: 1.2rem;
  }

  .fees {    
    width: 12.66rem;
  }

  .fees span.title {
    font-size: 1rem;
  }

  .fees span.value {
    font-size: 1.2rem;
  }

  .performance {    
    width: 12.66rem;
  }

  .performance span.title {
    font-size: 1rem;
  }

  .performance span.value {
    font-size: 1.2rem;
  }
}
@media (max-width: 992px) {
  .fees {    
    padding-left: 0.5rem;
  }
  .performance {
    padding-left: 0.5rem;
  }
}
</style>
