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
            <router-link to="/home" class="nav-link" v-on:click.native="menu=0">Home</router-link>
          </li>
          <li class="nav-item" v-bind:class="{'active':(menu === 1)}">
            <router-link to="/create" class="nav-link" v-on:click.native="menu=1">Create</router-link>
          </li>
          <li class="nav-item" v-bind:class="{'active':(menu === 2)}">
            <router-link to="/pendingItem" class="nav-link" v-on:click.native="menu=2">Pending Items</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto">
          <li class="nav-link disabled" style="font-weight: bold;">{{user.displayName}}</li>
          <li class="nav-item">
            <router-link to="/login" v-on:click.native="logout()" replace class="nav-link">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <br />
    <router-view @authenticated="setAuthenticated" @user="setUser" />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      authenticated: false,
      user: {
        id: 0,
        username: "-",
        password: "-",
        displayName: "-",
      },
      // Selectionne le menu (0.,1,2, ...)
      menu: 0,
    };
  },
  mounted() {
    console.log("App.mounted()");
    if (!this.authenticated) {
      this.$router.replace({ name: "Login" });
    }
  },
  methods: {
    setAuthenticated(status) {
      console.log("App.setAuthenticated()");
      this.authenticated = status;
    },
    setUser(user) {
      console.log("App.setUser()");
      this.user = JSON.parse(user);
    },
    logout() {
      console.log("logout ...");
      this.authenticated = false;
      this.user = null;
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
