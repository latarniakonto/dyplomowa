import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import AppView from "../views/AppView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: AppView,
    props: { content: "Home" }
  },
  {
    path: "/assets",
    name: "assets",
    component: AppView,
    props: { content: "Assets" }
  },
  {
    path: "/transactions",
    name: "transactions",
    component: AppView,
    props: { content: "Transactions" }
  },
  {
    path: "/operations",
    name: "operations",
    component: AppView,
    props: { content: "Operations" }
  },
  {
    path: "/snapshots",
    name: "snapshots",
    component: AppView,
    props: { content: "Snapshots" }
    
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;
