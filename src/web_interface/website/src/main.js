import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
Vue.use(VueCookies);

Vue.config.productionTip = false


new Vue({
  router,
  render: h => h(App),
  watch: {
    $route: {
        immediate: true,
        handler(to) {
            document.title = to.meta.title ? 'Sirius II - ' + to.meta.title : 'Sirius II';
        }
    },
  }
}).$mount('#app')
