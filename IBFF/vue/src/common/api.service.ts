const axios = require("axios");
axios.defaults.baseURL = "/";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export { axios };
