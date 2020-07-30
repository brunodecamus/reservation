<template>
  <div id="app">
    <!--
    <div v-if="authenticated" id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/login">Login</router-link>|
      <router-link to="/about">About</router-link>| | |
      <router-link to="/login" v-on:click.native="logout()" replace>Logout</router-link>
    </div>
    -->

    <!-- Menu toujours au TOP -->
    <nav
      id="nav"
      v-if="authenticated"
      class="navbar navbar-expand-lg fixed-top navbar-dark bg-primary"
    >
      <a class="navbar-brand" href="#">Study</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about" class="nav-link">About</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" v-on:click.native="logout()" replace class="nav-link">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <!-- Cette div pour que les vue commencent a la bonne hauteur -->
    <div style="height:56px"></div>
    <router-view @authenticated="setAuthenticated" />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      authenticated: false,
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
