import BasicLayout from '../../layouts/BasicLayout.vue';
import Login from '../../views/login/index.vue';


export default [
  {
    path: '/',
    redirect: '/workSpace'
  },
  {
    path: '/login',
    component: Login,
    meta: { name: '登录页面' },
  },
  {
    path: '/workspace',
    redirect: '/workspace/workbench',
    component: BasicLayout,
    meta: { name: '工作空间' },
    children: [
      {
        path: '/workspace/workbench',
        name: 'Workbench',
        component: () => import('../../views/workSpace/workbench/index.vue'),
        meta: { name: '工作台', requireAuth: true, affix: true, closable: false },
      },
      {
        path: '/workspace/console',
        component: () => import('../../views/workSpace/console/index.vue'),
        meta: { name: '控制台', requireAuth: true },
      },
      {
        path: '/workspace/analysis',
        component: () => import('../../views/workSpace/analysis/index.vue'),
        meta: { name: '分析页', requireAuth: true },
      },
      {
        path: '/workspace/monitor',
        component: () => import('../../views/workSpace/monitor/index.vue'),
        meta: { name: '监控页', requireAuth: true },
      }
    ]
  }, {
    path: '/error',
    component: BasicLayout,
    meta: { name: '错误页面' },
    children: [
      {
        path: '/error/401',
        component: () => import('../../views/error/401.vue'),
        meta: { name: '401' },
      },
      {
        path: '/error/403',
        component: () => import('../../views/error/403.vue'),
        meta: { name: '403' },
      },
      {
        path: '/error/404',
        component: () => import('../../views/error/404.vue'),
        meta: { name: '404' },
      },
      {
        path: '/error/500',
        component: () => import('../../views/error/500.vue'),
        meta: { name: '500' },
      }
    ]
  }, {
    path: '/system',
    component: BasicLayout,
    meta: { name: '系统管理' },
    children: [
      {
        path: '/system/user',
        component: () => import('../../views/system/user/index.vue'),
        meta: { name: '用户管理', requireAuth: true },
      },
      {
        path: '/system/role',
        component: () => import('../../views/system/role/index.vue'),
        meta: { name: '角色管理', requireAuth: true },
      },
      {
        path: '/system/menu',
        component: () => import('../../views/system/menu/index.vue'),
        meta: { name: '菜单管理', requireAuth: true },
      },
      {
        path: '/system/organization',
        component: () => import('../../views/system/organization/index.vue'),
        meta: { name: '机构管理', requireAuth: true },
      },
      {
        path: '/system/dictionary',
        component: () => import('../../views/system/dictionary/index.vue'),
        meta: { name: '字典管理', requireAuth: true },
      },
      {
        path: '/system/file',
        component: () => import('../../views/system/file/index.vue'),
        meta: { name: '文件管理', requireAuth: true },
      },
      {
        path: '/system/login',
        component: () => import('../../views/system/login/index.vue'),
        meta: { name: '登录日志', requireAuth: true },
      },
      {
        path: '/system/option',
        component: () => import('../../views/system/option/index.vue'),
        meta: { name: '操作日志', requireAuth: true },
      },
    ]
  }, {
    path: '/result',
    component: BasicLayout,
    meta: { name: '错误页面' },
    children: [
      {
        path: '/result/success',
        component: () => import('../../views/result/success.vue'),
        meta: { name: '成功页面', requireAuth: true },
      },
      {
        path: '/result/failure',
        component: () => import('../../views/result/failure.vue'),
        meta: { name: '失败页面', requireAuth: true },
      },
    ]
  }, {
    path: '/list',
    component: BasicLayout,
    meta: { name: '列表页面' },
    children: [
      {
        path: '/table/base',
        component: () => import('../../views/table/base.vue'),
        meta: { name: '查询列表', requireAuth: true },
      },
      {
        path: '/table/card',
        component: () => import('../../views/table/card.vue'),
        meta: { name: '卡片列表', requireAuth: true },
      },
      {
        path: '/table/project',
        component: () => import('../../views/table/project.vue'),
        meta: { name: '项目列表', requireAuth: true },
      },
      {
        path: '/table/article',
        component: () => import('../../views/table/article.vue'),
        meta: { name: '文章列表', requireAuth: true },
      }
    ]
  }, {
    path: '/form',
    component: BasicLayout,
    meta: { name: '表单页面' },
    children: [
      {
        path: '/form/base',
        component: () => import('../../views/form/base.vue'),
        meta: { name: '基础表单', requireAuth: true },
      },
      {
        path: '/form/step',
        component: () => import('../../views/form/step.vue'),
        meta: { name: '分步表单', requireAuth: true },
      },
      {
        path: '/form/intricate',
        name: 'Intricate',
        component: () => import('../../views/form/intricate.vue'),
        meta: { name: '复杂表单', requireAuth: true },
      },
      {
        path: '/form/step',
        name: 'Step',
        component: () => import('../../views/form/step.vue'),
        meta: { name: '分步表单', requireAuth: true },
      },
    ]
  }, {
    path: '/directive',
    component: BasicLayout,
    meta: { name: '内置指令' },
    children: [
      {
        path: '/directive/permission',
        component: () => import('../../views/directive/permission.vue'),
        meta: { name: '权限指令', requireAuth: true },
      },
    ]
  }, {
    path: '/component',
    component: BasicLayout,
    meta: { name: '常用组件' },
    children: [
      {
        path: '/component/qrcode',
        component: () => import('../../views/component/qrcode.vue'),
        meta: { name: '二维码', requireAuth: true },
      },
      {
        path: '/component/barcode',
        component: () => import('../../views/component/barcode.vue'),
        meta: { name: '条形码', requireAuth: true },
      },
      {
        path: '/component/treeSelect',
        component: () => import('../../views/component/treeSelect.vue'),
        meta: { name: '下拉树', requireAuth: true },
      },
    ]
  }, {
    path: '/enrollee',
    component: BasicLayout,
    meta: { name: '个人中心' },
    children: [
      {
        path: '/enrollee/profile',
        component: () => import('../../views/enrollee/profile/index.vue'),
        meta: { name: '我的资料', requireAuth: true },
      },
      {
        path: '/enrollee/message',
        component: () => import('../../views/enrollee/message/index.vue'),
        meta: { name: '我的消息', requireAuth: true },
      },

    ]
  },


]
