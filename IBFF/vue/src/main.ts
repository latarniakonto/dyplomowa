import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import PrimeVue from "primevue/config";
import "primevue/resources/themes/md-light-indigo/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import ToastService from "primevue/toastservice";
import "primeflex/primeflex.css";

loadFonts();

const app = createApp(App);

app.use(router);
app.use(store);
app.use(vuetify);
app.use(PrimeVue);
app.use(ToastService);

app.mount("#app");

export const appToast = app.config.globalProperties.$toast;
