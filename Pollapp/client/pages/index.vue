<template>
  <div>
    <div v-for="question in questions"
            :key="question.question_text"
          >
          <NuxtLink :to="'/'+question.questionid">{{question.question_text}}</NuxtLink>
        </div>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const questions = await $axios.$get('/polls/questions/')
    return { questions }
  },
}
</script>
