<template>
  <div>
    <div v-for="choice in choices" :key="choice.question"><NuxtLink :to="'/result/'+choice.question"><button @click="submitdata(choice)">{{choice.choice_text}}</button></NuxtLink></div>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios,params }) {
    const choices = await $axios.$get(`/polls/Choice/${params.id}/`)
    return { choices }
  },
  methods:{
    async submitdata(choice){
      await this.$axios.post('polls/updatevote/',{
        choice
      })
      this.$nuxt.refresh()
    }
  }
}
</script>
