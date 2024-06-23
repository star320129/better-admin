<template>
    <lay-breadcrumb>
        <lay-breadcrumb-item v-for="(breadcrumb, index) in breadcrumbs" :key="index">
            {{ breadcrumb.name }}
        </lay-breadcrumb-item>
    </lay-breadcrumb>
</template>

<script lang="ts">
export default {
    name: "GlobalBreadcrumb"
}
</script>


<script lang="ts" setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import { getParents } from "../../library/treeUtil";
import { useUserStore } from "../../store/user";

const userStore = useUserStore();
const route = useRoute();
// console.log(route.path)
const breadcrumbs = computed(() => getParents(userStore.menus, route.path)?.reverse());
</script>
