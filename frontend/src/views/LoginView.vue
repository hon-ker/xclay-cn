<template>
  <div class="login-container">
    <n-card class="login-form">
      <n-tabs default-value="signin" size="large" justify-content="space-evenly">
        <n-tab-pane name="signin" tab="登录">
          <n-form>
            <n-form-item-row label="用户名">
              <n-input placeholder="用户名" v-model:value="login.name" />
            </n-form-item-row>
            <n-form-item-row label="密码">
              <n-input v-model:value="login.passwd" type="password" show-password-on="click" placeholder="密码"
                />
            </n-form-item-row>
          </n-form>
          <n-button @click="handleLogin" type="primary" block secondary strong>
            登录
          </n-button>
        </n-tab-pane>
        <!-- 注册 -->
        <n-tab-pane name="signup" tab="注册">
          <n-form>
            <n-form-item-row label="用户名">
              <n-input placeholder="用户名" v-model:value="register.name" />
            </n-form-item-row>
            <n-form-item-row label="密码">
              <n-input v-model:value="register.passwd" type="password" show-password-on="click" placeholder="密码"
                />
            </n-form-item-row>
            <n-form-item-row label="确认密码">
              <n-input v-model:value="register.repasswd" type="password" show-password-on="click" placeholder="确认密码"
                 />
            </n-form-item-row>
            <n-form-item-row label="邮箱">
              <n-auto-complete v-model:value="register.mail" :options="mailComplate" placeholder="邮箱" size="medium" />
            </n-form-item-row>
          </n-form>
          <n-button @click="handleRegister" type="primary" block secondary strong>
            注册
          </n-button>
        </n-tab-pane>
      </n-tabs>
    </n-card>
  </div>
</template>

<script setup>
import { useLoadingBar, useMessage, NAutoComplete, NCard, NTabs, NTabPane, NForm, NFormItemRow, NInput, NButton } from 'naive-ui';
import { ref, computed } from 'vue';

import { MyAxios } from '../assets/clay.utils';

const message = useMessage();

const loadingBar = useLoadingBar();

function handleStart() {
  loadingBar.start();
}

function handleFinish() {
  loadingBar.finish();
}
function handleError() {
  loadingBar.error();
}

const login = ref({
  name: "",
  passwd: ""
})

const register = ref({
  name: "",
  passwd: "",
  repasswd: "",
  mail: "",
})

const mailComplate = computed(() => {
  return ["@qq.com", "@163.com", "@gmail.com", , "@xclay.cn", "@outlook.com"].map((suffix) => {
    const prefix = register.value.mail.split("@")[0];
    return {
      label: prefix + suffix,
      value: prefix + suffix
    };
  });
})


const handleRegister = () => {
  if (register.value.passwd !== register.value.repasswd) {
    message.error("密码不一致!");
  } else if (register.value.passwd.length < 8) {
    message.error("密码至少八位!");
  } else if (register.value.mail === "") {
    message.error("请输入邮箱!");
  } else {
    // 密码校验通过，可以进行提交操作
    // 在这里你可以在提交前删除 repassword
    loadingBar.start();
    delete register.value.repasswd;


    // 进行提交操作，例如发送注册请求
    MyAxios.post('/register', register.value)
      .then(response => {
        loadingBar.finish();
        message.success(response.data.msg);
      })
      .catch(error => {
        loadingBar.error();

        message.error(error.data.detail);
      });
  }
}

const handleLogin = () => {
  if (login.value.name.length < 1 && login.value.passwd.length < 1) {
    message.error("请输入用户名和密码");
  }else if (login.value.name.length < 1) {
    message.error("请输入用户名");
  }
  else if (login.value.passwd.length < 1) {
    message.error("请输入密码");
  }


  loadingBar.start();

  // 进行提交操作，例如发送注册请求
  MyAxios.post('/login', login.value)
    .then(response => {
      // 注册成功，进行相关处理
        loadingBar.finish();
        message.success(response.data.msg);

    })
    .catch(error => {
      // 注册失败，进行错误处理
      loadingBar.error();
      message.error(error.response.data.detail);

    });
}

</script>

<style scoped>
.login-container {
  position: relative;
  height: 100vh;
  /* 设置容器的高度，这里使用视口高度作为示例 */
}

.login-form {
  width: 400px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>