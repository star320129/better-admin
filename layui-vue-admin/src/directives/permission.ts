import { Directive } from 'vue';
import { useUserStore } from '../store/user';

export const permission: Directive = {
    mounted(el, binding) {
        toolPermission(el, binding);
    },
    updated(el, binding) {
        toolPermission(el, binding);
    }
}

// 自定义指令，检测按钮权限
const toolPermission = (el:any, binding:any) => {
    const { value } = binding;
    const userInfoStore = useUserStore();
    const permissions = userInfoStore.permissions;
    if (value && typeof value === 'object') {

        const exists = permissions.some(permission =>
            Object.keys(value).every(key =>
                Object.keys(permission).includes(key) && permission[key] === value[key]
            )
        );

        if (!exists) {
            el.parentNode && el.parentNode.removeChild(el);
        }
    }
}