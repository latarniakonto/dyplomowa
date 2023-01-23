const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    },
  },
  publicPath:
    process.env.NODE_ENV === "production"
      ? "/static/dist/"
      : "http://0.0.0.0:8080",
  outputDir: "../static/dist",
  indexPath: "../../templates/index.html",
  pages: {
    index: {
      entry: "src/main.ts",
      title: "IBFF",
    },
  },
  devServer: {
    devMiddleware: {
      publicPath: "http://0.0.0.0:8080",
      writeToDisk: (filePath) => filePath.endsWith("index.html"),
    },
    hot: "only",
    headers: { "Access-Control-Allow-Origin": "*" },
    client: {
      webSocketURL: "ws://0.0.0.0:8080/ws",
    }
  },  
});
