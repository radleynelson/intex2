<template>
  <div class="app">
    <div class="homepage">
      <b-jumbotron bg-variant="dark" text-variant="white" border-variant="dark">
        <template slot="header">Group 2-13 Intex</template>

        <template slot="lead">
          Welcome {{userName}}, we hope that you enjoy our Intex 2 Project that we have worked very hard on! Let us know what you think
        </template>

        <hr class="my-4">

        <p>
          It uses utility classes for typography and spacing to space content out within the larger
          container.
        </p>
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
export default {
  name: 'HomePage',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
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
