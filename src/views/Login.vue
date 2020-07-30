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
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      input: {
        username: "a",
        password: "a",
      },
    };
  },
  methods: {
    login() {
      console.log("login ...");
      if (this.input.username != "" && this.input.password != "") {
        if (
          this.input.username == this.$parent.mockAccount.username &&
          this.input.password == this.$parent.mockAccount.password
        ) {
          this.$emit("authenticated", true);
          this.$router.replace({ name: "Home" });
        } else {
          console.log("The username and / or password is incorrect");
        }
      } else {
        console.log("A username and password must be present");
      }
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