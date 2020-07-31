<template>
  <div class="container">
    <div class="row">
      <div class="col-12 text-primary bg-light border border-primary rounded">
        Creation d'un Study
        <form>
          <!-- Name -->
          <div class="form-group row">
            <label for="idName" class="col-3 col-form-label">Name</label>
            <div class="col-9">
              <input id="idName" name="idName" type="text" required="required" class="form-control" />
            </div>
          </div>

          <!-- Validation -->
          <div class="form-group row">
            <label for="idValidation" class="col-3 col-form-label">Validation threshold</label>
            <div class="col-9">
              <input id="idValidation" name="idValidation" type="text" class="form-control" />
            </div>
          </div>

          <!-- Domain -->
          <div class="form-group row">
            <label class="col-3 col-form-label">Domain</label>
            <div class="col-9">
              <select id="idDomain" name="idDomain" class="custom-select" multiple="multiple">
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
              <input id="idItems" name="idItems" type="text" class="form-control" />
            </div>
          </div>

          <!-- Participants -->
          <div class="form-group row">
            <label for="idParticipants" class="col-3 col-form-label">Participants threshold</label>
            <div class="col-9">
              <input id="idParticipants" name="idParticipants" type="text" class="form-control" />
            </div>
          </div>

          <!-- Submit -->
          <div class="form-group row">
            <div class="offset-3 col-9">
              <button name="submit" type="submit" class="btn btn-primary">Create</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
//import CreateStudy from "@/components/CreateStudy.vue";
//import PendingStudy from "@/components/PendingStudy.vue";
//import CreateStudyForm from "@/components/CreateStudyForm.vue";

export default {
  name: "Home",
  components: {
    //HelloWorld,
    //CreateStudy,
    //PendingStudy,
    //CreateStudyForm,
  },
};
</script>

<style>
zone {
  border-block-color: black;
  color: #2c3e50;
}
</style>
