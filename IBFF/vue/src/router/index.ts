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
    path: "/:slug",    
    redirect: to => {
      return { path: "/", query: { slug: to.params.slug }};
    }
  },
  {
    path: "/assets",
    name: "assets",
    component: AppView,
    props: { content: "Assets" }
  },
  {
    path: "/assets/:slug",    
    redirect: to => {
      return { path: "/assets", query: { slug: to.params.slug }};
    }
  },
  {
    path: "/transactions",
    name: "transactions",
    component: AppView,
    props: { content: "Transactions" }
  },
  {
    path: "/transactions/:slug",
    redirect: to => {
      return { path: "/transactions", query: { slug: to.params.slug }};
    }
  },
  {
    path: "/operations",
    name: "operations",
    component: AppView,
    props: { content: "Operations" }
  },
  {
    path: "/operations/:slug",    
    redirect: to => {
      return { path: "/operations", query: { slug: to.params.slug }};
    }
  },
  {
    path: "/snapshots",
    name: "snapshots",
    component: AppView,
    props: { content: "Snapshots" }
    
  },
  {
    path: "/snapshots/:slug",
    redirect: to => {
      return { path: "/snapshots", query: { slug: to.params.slug }};
    }
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
