<template>
  <b-card
    tag="article"
    style="height: 100%; min-width: 350px; max-width: 500px; font-family: 'Work Sans SemiBold'"
    id="jobOfferCard"
  >
    <b-container style="font-family: 'Work Sans'">
      <b-row align-v="center">
        <b-col cols="8">
          <b-card-text id="companyName" >
          <p class="titleJobOfferCard">{{ job_name }}</p>
          <p class="companyNameJobOfferCard">{{ company_name }}</p>
          </b-card-text>
          <b-col lg v-if="contract_type !== null && contract_type !== ''">
          <b-icon id="contractTypeIcon" icon="briefcase"></b-icon> {{ contract_type }}
          </b-col>
          <b-col lg>
          <b-icon id="publicationDateIcon" icon="calendar3-event"></b-icon> {{ publication_date }}
          </b-col>
          <b-col lg>
          <b-icon id="locationIcon" icon="geo-alt-fill"></b-icon> {{ location }}
          </b-col>
        </b-col>
        <b-col align-v="center">
          <img v-if="company_logo !=null" class="card-img" :src=company_logo alt=""
            style="max-width:128px; max-height:128px">
          <img v-if="company_logo == null" class="card-img" src="../assets/images/company_avatar.png" alt=""
            style="max-width:128px; max-height:128px">
        </b-col>
      </b-row>
    </b-container>
    <b-button id="jobOfferButton" class="btn btn-outline-light active" @click="onJobOffer(id)" style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
  </b-card>
</template>

<script>
export default{
  props: {
    id: { required: true, type: Number },
    job_name: { required: true, type: String },
    company_name: { required: true, type: String },
    contract_type: { required: true, type: String },
    publication_date: { required: true, type: String },
    location: { required: true, type: String },
    company_logo: { required: false, type: String }
  },
  methods: {
    onJobOffer (id) {
      this.$router.push('/job_posting/' + id)
    }
  }
}
</script>

<style>
.companyNameJobOfferCard{
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 18px;
  margin-bottom: 0.3rem;
}
.titleJobOfferCard{
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-weight: bold;
  font-size: 24px;
  margin-bottom: 0;
}
</style>
