import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios';

Vue.prototype.$http = axios;

Vue.config.productionTip = false

new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app')