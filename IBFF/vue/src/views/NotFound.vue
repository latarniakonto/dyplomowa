<template>
    <div>
        <h1 class="not-found">{{ message }}</h1>
    </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
    name: "NotFound",

    data() {
        return {
            message: "404 - Not Found"
        }
    },

    created() {
        document.title = this.message;
    }
})
</script>

<style>
.not-found {
    color: black;
    text-align: center;
}
</style>