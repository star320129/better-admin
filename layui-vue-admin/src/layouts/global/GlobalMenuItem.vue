<template>
    <template v-for="(menu, index) in menus" :key="index">
        <template v-if="menu.children">
            <lay-sub-menu :id="menu.path">
                <template #icon>
                    <lay-icon :type="menu.icon"></lay-icon>
                </template>
                <template #title>{{ menu.name }}</template>
                <GlobalMenuItem :menus="menu.children"></GlobalMenuItem>
            </lay-sub-menu>
        </template>
        <template v-else>
            <lay-menu-item :id="menu.path">
                <template #icon>
                    <lay-icon :type="menu.icon"></lay-icon>
                </template>
                <template #title>{{ menu.name }}</template>
            </lay-menu-item>
        </template>
    </template>
</template>

<script lang="ts">
import GlobalMenuItem from "./GlobalMenuItem.vue"
import { defineComponent } from "vue";

export default defineComponent({
    name:  "GlobalMenuItem",
    props: {
        menus: {
            type: Object
        }
    }
})
</script>