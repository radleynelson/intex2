// homepage/scripts/index.js
import Vue from 'vue'
import App from './src/App.vue'
import router from './src/router'

Vue.config.productionTip = false
export default function(context) {
    // utc_epoch comes from index.py
    console.log('Current epoch in UTC is ' + context.utc_epoch);
      
}

window.addEventListener('load', function () {
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })
  
  console.log(Vue);
})

