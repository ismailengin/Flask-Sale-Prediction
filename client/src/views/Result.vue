<template>
    <div class="hello">
        <h1>Sales {{ id }}</h1>
        <img :src="`http://localhost:5000/show/${id}`">
        <a style="cursor: pointer; text-decoration: underline" v-on:click="goBack()">Go Back</a>
    </div>

</template>


<script>
import router from '../router'
export default {
    name: 'Result',
    data () {
        return {
            id: 0,
        }
    },
    created() {
        this.id = this.$route.params.id;
    },
    methods: {
        goBack() {
            router.go(-1);
        }
    }
}
</script>

   

    export default {
    
    }
</script>