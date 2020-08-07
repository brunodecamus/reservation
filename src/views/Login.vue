<template>
  <div id="login">
    <div class="login-form">
      <h2 class="text-center">Log in</h2>
      <div class="form-group">
        <input
          type="text"
          name="username"
          v-model="input.username"
          placeholder="Username"
          class="form-control"
          required="required"
        />
      </div>
      <div class="form-group">
        <input
          type="password"
          name="password"
          v-model="input.password"
          placeholder="Password"
          class="form-control"
          required="required"
        />
      </div>
      <div class="form-group">
        <button type="button" class="btn btn-primary btn-block" v-on:click="login()">Login</button>
      </div>

      <div v-for="error in errors" :key="error">{{ error }}</div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

export default {
  name: "Login",

  data() {
    return {
      input: {
        username: "bdecamus",
        password: "a",
      },
      errors: [],
    };
  },
  methods: {
    login() {
      console.log(
        "Login. Appel service REST http://localhost:5000/api/v1.0/user"
      );

      Vue.axios
        .get("http://localhost:5000/api/v1.0/user", {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods":
              "GET, POST, PATCH, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers":
              "Origin, Content-Type, X-Auth-Token",
            username: this.input.username,
            password: this.input.password,
          },
        })
        .then((response) => {
          console.log("L'utilisateur existe : ", response);
          this.$emit("authenticated", true);
          this.$emit("user", response.data);
          this.$router.replace({ name: "Home" });
        })
        .catch((e) => {
          console.log("Aucune info sur l utilisateur ou erreur: ", e);
          this.errors = [];
          this.errors.push("Unknown username or bad password.");
        });
    },
  },
};
</script>

<style scoped>
#login {
  width: 500px;
  border: 1px solid #cccccc;
  background-color: #ffffff;
  margin: auto;
  margin-top: 200px;
  padding: 20px;
}
</style>