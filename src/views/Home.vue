<template>
  <div class="container">
    <div class="row" style="height:200px;">
      <div class="col-6 text-primary bg-light border border-primary rounded">
        <CreateStudy />
      </div>
      <div class="col-6 text-primary bg-light border border-primary rounded">
        <PendingStudy />
      </div>
    </div>
    <div class="row" style="height:200px;">
      <div class="col-12 text-primary bg-light border border-primary rounded">
        <CreateStudyForm />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import CreateStudy from "@/components/CreateStudy.vue";
import PendingStudy from "@/components/PendingStudy.vue";
import CreateStudyForm from "@/components/CreateStudyForm.vue";

export default {
  name: "Home",
  components: {
    //HelloWorld,
    CreateStudy,
    PendingStudy,
    CreateStudyForm,
  },
};
</script>

<style>
zone {
  border-block-color: black;
  color: #2c3e50;
}
</style>
