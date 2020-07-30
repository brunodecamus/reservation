<template>
  <div id="app">
    authenticated : {{authenticated}}
    <div v-if="authenticated" id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/login">Login</router-link>|
      <router-link to="/about">About</router-link>| | |
      <router-link to="/login" v-on:click.native="logout()" replace>Logout</router-link>
    </div>

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

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
