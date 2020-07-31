<template>
  <div id="app" class="container">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary" v-if="authenticated">
      <a class="navbar-brand" href="#">Study</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#main_nav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="main_nav">
        <ul class="navbar-nav">
          <li class="nav-item" v-bind:class="{'active':(menu === 0)}">
            <router-link to="/" class="nav-link" v-on:click.native="menu=0">Home</router-link>
          </li>
          <li class="nav-item" v-bind:class="{'active':(menu === 1)}">
            <router-link to="/about" class="nav-link" v-on:click.native="menu=1">About</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link to="/login" v-on:click.native="logout()" replace class="nav-link">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <br />
    <router-view @authenticated="setAuthenticated" />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      authenticated: false,
      // Selectionne le menu
      menu: 0,
      mockAccount: {
        username: "a",
        password: "a",
      },
    };
  },
  mounted() {
    console.log("mounted ...");
    console.log(this.$router);
    if (!this.authenticated) {
      this.$router.replace({ name: "Login" });
    }
  },
  methods: {
    setAuthenticated(status) {
      console.log("setAuthenticated ...");
      this.authenticated = status;
    },
    logout() {
      console.log("logout ...");
      this.authenticated = false;
    },
    say(message) {
      console.log(message);
      console.log(this);
    },
  },
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
