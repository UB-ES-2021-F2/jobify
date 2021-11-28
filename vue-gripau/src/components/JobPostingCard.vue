<template>
  <b-card
    tag="article"
    style="height: 100%; min-width: 350px; max-width: 500px; font-family: 'Work Sans SemiBold'"
    id="jobOfferCard"
  >
    <b-container style="font-family: 'Work Sans'">
      <b-row align-v="center">
        <b-col align="left">
          <b-card-text id="companyName" >
          <p class="titleJobOfferCard">{{ job_name }}</p>
          <p  v-if="show_company" class="companyNameJobOfferCard">{{ company_name }}</p>
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
        <b-col v-if="show_company"  align-v="center" cols="4">
          <img v-if="company_logo !=null" class="card-img companyAvatar" :src=company_logo alt="">
          <img v-if="company_logo == null" class="card-img companyAvatar" src="../assets/images/company_avatar.png" alt="">
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
    company_logo: { required: false, type: String },
    show_company: { type: Boolean, default: true }
  },
  methods: {
    onJobOffer (id) {
      this.$router.push('/job_posting/' + id)
    }
  },
  created () {
    console.log(this.$props)
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
.companyAvatar{
  max-width:128px;
  max-height:128px;
  border-radius: 128px;
}
</style>
