<template>
  <b-col>
    <b-row>
      <b-col class="mb-4" align="center" align-self="stretch" v-for="(job_offer) in job_offers.slice((current_page-1)*per_page, current_page*per_page)" :key="job_offer.id">
        <job-offer-card
          v-bind:id = "job_offer.id"
          v-bind:job_name = "job_offer.job_name"
          v-bind:company_name = "job_offer.company_name"
          v-bind:contract_type = "job_offer.contract_type"
          v-bind:publication_date = "job_offer.publication_date"
          v-bind:location =  "job_offer.location"
          v-bind:company_logo =  "companies_logos[job_offer.company]"
        ></job-offer-card>
      </b-col>
    </b-row>
    <b-row class="mt-4" align-h="center">
      <b-col align-self="center" cols="10">
        <b-pagination
          align="center"
          v-model = "current_page"
          :total-rows = "job_offers.length"
          :per-page = "per_page"
        >
        </b-pagination>
      </b-col>
    </b-row>
    <b-col align="center">
      Items per page:
    </b-col>
    <b-col class="pb-4" align-h="center">
      <b-form-select style="width:10%; min-width: 60px" v-model="per_page" :options="options" size="sm">Items per page:</b-form-select>
    </b-col>
  </b-col>
</template>

<script>
export default{
  props: {
    job_offers: { required: true, type: Array },
    companies_logos: { required: false, type: Object },
    per_page: {type: Number, default: 25}
  },
  data () {
    return {
      current_page: 1,
      options: [5, 10, 25, 50]
    }
  }
}
</script>

<style>

.page-item.active .page-link {
  background-color: #ffc107 !important;
  border-color: #ffc107 !important;
}
.page-link {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  color: #ffc107;
}
</style>
