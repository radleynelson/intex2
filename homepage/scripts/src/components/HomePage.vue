<template>
  <div class="app">
    <div class="homepage">
      <b-jumbotron bg-variant="dark" text-variant="white" border-variant="dark">
        <template slot="header">
          <div style="width: 35%; margin: auto;">
            <img style="width: 100%" src='/static/homepage/media/logo2White.png' alt="Our Logo">
          </div>
        </template>

        <template slot="lead">
         
        </template>

        <hr class="my-4">

        <div style="width: 75%; margin: auto;">
          <h5>
            First class business consulting services, using cutting edge technologies to solve unstructured business problems.
          </h5>
        </div>
      </b-jumbotron>

      <b-card-group deck>
        <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top>
          <b-card-text>
            This is a wider card with supporting text below as a natural lead-in to additional content.
            This content is a little bit longer.
          </b-card-text>
          <div slot="footer"><small class="text-muted">Last updated 3 mins ago</small></div>
        </b-card>

        <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top>
          <b-card-text>
            This card has supporting text below as a natural lead-in to additional content.
          </b-card-text>
          <div slot="footer"><small class="text-muted">Last updated 3 mins ago</small></div>
        </b-card>

        <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top>
          <b-card-text>
            This is a wider card with supporting text below as a natural lead-in to additional content.
            This card has even longer content than the first to show that equal height action.
          </b-card-text>
          <div slot="footer"><small class="text-muted">Last updated 3 mins ago</small></div>
        </b-card>
      </b-card-group>
    </div>
  </div>
</template>

<script>
import logo from '../images/logo2White.png'
export default {
  name: 'HomePage',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
    }
  },
  computed: {
    userName() {
      return this.$store.getters.userName
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
