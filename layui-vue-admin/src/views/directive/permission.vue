<template>
    <div>
        <lay-card>
            <p class="header-title">权限指令</p>
            <p class="header-describe">表单页用于向用户收集或验证信息，基础表单常见于数据项较少的表单场景。表单域标签也可支持响应式.</p>
        </lay-card>
        <lay-container :fluid="true" style="padding: 10px;padding-top: 0px;">
            <lay-card>
                <template #title>我的权限</template>
                {{ permissions }}
            </lay-card>
            <lay-card>
                <template #title>我的按钮</template>
                <lay-button-container>
                    <lay-button v-permission='{"添加用户": "user:action:create"}' type="primary" >新增</lay-button>
                    <lay-button v-permission='{"编辑用户": "user:action:update"}'>修改</lay-button>
                    <lay-button v-permission='{"删除用户": "user:action:destroy"}'>删除</lay-button>
                    <lay-button v-permission='{"用户导入": "user:import"}'>导入</lay-button>
                    <lay-button v-permission='{"用户导出": "user:export"}'>导出</lay-button>
                </lay-button-container>
            </lay-card>
        </lay-container>
    </div>
</template>

<script lang="ts">
import { useUserStore } from "../../store/user";

export default {
    setup() {
        const userInfoStore = useUserStore();
        const permissions = userInfoStore.permissions;
        return {
            permissions
        };
    },
};
</script>

<style scoped>
.header-title {
    font-size: 20px;
    font-weight: 500;
    margin-top: 12px;
    margin-bottom: 20px;
}

.header-describe {
    font-size: 14px;
    margin-bottom: 12px;
}
</style>