<template>
  <div class="container">
    <div class="row">
      <div class="col-12 text-primary bg-light border border-primary rounded">
        Creation d'un Study
        <form>
          <!-- name -->
          <div class="form-group row">
            <label for="text" class="col-4 col-form-label">Name</label>
            <div class="col-8">
              <input id="text" name="name" type="text" class="form-control" required="required" />
            </div>
          </div>

          <!-- Validation -->
          <div class="form-group row">
            <label for="text1" class="col-4 col-form-label">Validation threshold</label>
            <div class="col-8">
              <input type="range" class="custom-range" id="customRange1" min="0" max="100" />
            </div>
          </div>

          <!-- Domain -->
          <div class="form-group row">
            <label for="idDomain" class="col-4 col-form-label">Domain</label>
            <div class="col-8">
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
            <label for="text3" class="col-4 col-form-label">Items</label>
            <div class="col-8">
              <input id="text" name="items" type="text" class="form-control" />
            </div>
          </div>

          <!-- Participants -->
          <div class="form-group row">
            <label for="text4" class="col-4 col-form-label">Participants</label>
            <div class="col-8">
              <input id="text" name="participants" type="text" class="form-control" />
            </div>
          </div>

          <!-- Submit -->
          <div class="form-group row">
            <div class="offset-4 col-8">
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
