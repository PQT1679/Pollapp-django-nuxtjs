<template>
  <div>
    <table>
    <td>
      <tr v-for="choice in result.choices" :key="choice.choice_text">{{choice.choice_text}}</tr>
    <!-- <th v-for="choice in result.choices" :key="choice.choice_text">{{choice.choice_text}}</th> -->
  </td>
    <td>
    <tr v-for="choice in result.choices" :key="choice.choice_text">{{choice.votes}}</tr>
  </td>
    </table>

    <button><NuxtLink to="/">Bỏ Phiếu Lại</NuxtLink></button>
  </div>

</template>

<style>
table, th, td {
  border:1px solid black;
  padding: 10px;
  text-align: center;
}
</style>

<script>
export default {
  async asyncData({ $axios,params }) {
    const result = await $axios.$get(`/polls/questions/${params.id}/`)
    return { result }
  },
}
</script>