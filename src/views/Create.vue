<template>
  <div class="container">
    <div class="row">
      <div class="col-12 text-primary bg-light border border-primary rounded">
        Creation d'un Study
        <form action="#">
          <!-- Name -->
          <div class="form-group row">
            <label for="idName" class="col-3 col-form-label">Name</label>
            <div class="col-9">
              <input
                id="idName"
                name="idName"
                type="text"
                required="required"
                class="form-control"
                v-model="name"
              />
            </div>
          </div>

          <!-- Validation -->
          <div class="form-group row">
            <label for="idValidation" class="col-3 col-form-label">Validation threshold</label>
            <div class="col-9">
              <input
                id="idValidation"
                name="idValidation"
                type="range"
                class="form-control"
                v-model="validation"
              />
            </div>
          </div>

          <!-- Domain -->
          <div class="form-group row">
            <label class="col-3 col-form-label">Domain</label>
            <div class="col-9">
              <select
                id="idDomain"
                name="idDomain"
                class="custom-select"
                multiple="multiple"
                v-model="domain"
              >
                <option value="Dev">Dev</option>
                <option value="Math">Math</option>
                <option value="Anglais">Anglais</option>
                <option value="Sport">Sport</option>
              </select>
            </div>
          </div>

          <!-- Items -->
          <div class="form-group row">
            <label for="idItems" class="col-3 col-form-label">Items</label>
            <div class="col-9">
              <input id="idItems" name="idItems" type="text" class="form-control" v-model="items" />
            </div>
          </div>

          <!-- Participants -->
          <div class="form-group row">
            <label for="idParticipants" class="col-3 col-form-label">Participants threshold</label>
            <div class="col-9">
              <input
                id="idParticipants"
                name="idParticipants"
                type="text"
                class="form-control"
                v-model="participants"
              />
            </div>
          </div>

          <!-- Submit -->
          <div class="form-group row">
            <div class="offset-3 col-9">
              <button name="submit" type="submit" class="btn btn-primary" @click="submit">Create</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

export default {
  name: "Create",
  components: {
    //CreateStudyForm,
  },
  data: function () {
    return {
      name: "Mon test 1",
      validation: 50,
      domain: ["Sport"],
      items: "",
      participants: "Jean, Paul",
    };
  },
  methods: {
    submit() {
      console.log("Submit form ...");

      // Pas de validation pour le moment
      console.log(this.$data);

      const study = {
        name: this.$data.name,
        validation: this.$data.validation,
        domain: this.$data.domain,
        items: this.$data.items,
        participants: this.$data.participants,
      };

      Vue.axios
        .post("http://localhost:5000/api/v1.0/study", study, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods":
              "GET, POST, PATCH, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers":
              "Origin, Content-Type, X-Auth-Token",
          },
        })
        .then((response) => {
          console.log("OK : ", response);
          //this.$router.replace({ name: "Home" });
        })
        .catch((e) => {
          console.log("ERR : ", e);
        });
    },
  },
};
</script>




<style>
zone {
  border-block-color: black;
  color: #2c3e50;
}
</style>
