<template>
  <div class="login">
    <div class="login-box">
      <a href="/" class="logo" />

      <div class="login-box-wrap">
        <h2 class="login-text">
          대한민국 No.1 어린이집 추천 플랫폼
        </h2>
        <div class="divider" />

        <div class="form">
          <v-text-field outlined color="success" label="아이디" />
          <v-text-field outlined color="#0CC476" label="비밀번호" hide-details />
          <v-list-item style="padding:0;margin-top:30px;">
            <v-list-item-content style="padding:0">
              <v-checkbox label="아이디 저장" color="success" dense style="margin:0px" />
            </v-list-item-content>
            <v-list-item-action style="margin:0;">
              <a href="#" style="margin-bottom:15px;"> 혹시 비밀번호를 잊으셨나요? </a>
            </v-list-item-action>
          </v-list-item>
          <v-row
            align="center"
            justify="center"
          >
            <v-btn color="#0dCA78" rounded x-large dark style="margin-top:10px; width:90%;">
              <span style="font-size:20px">로그인</span>
            </v-btn>
            <div class="add-option">
              <nuxt-link to="/signup">
                회원가입
              </nuxt-link>

              <span class="bar" aria-hidden="true">|</span>
              <a href="#">아이디 찾기</a>
              <span class="bar" aria-hidden="true">|</span>
              <a href="#">비밀번호 찾기</a>
            </div>
          </v-row>
        </div>

        <div class="other-service">
          <div class="add-option">
            <div class="wrap">
              <p>다른 서비스로 로그인</p>
              <a class="_kakao _serviceIcon" title="kakao" href="#" @mouseover="switchButton" />
              <a class="_naver _serviceIcon" title="naver" href="#" @mouseover="switchButton" />
              <a class="_facebook _serviceIcon" title="facebook" href="#" @mouseover="switchButton" />
            </div>
          </div>
        </div>
        </h2>
      </div>
    </div>
    <div class="banner" />
  </div>
</template>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script>
export default {
  methods: {
    switchButton (e) {
      const kakaoIcon = $('._kakao')
      let className = e.target.classList
      for (let i = 0; i < e.target.classList.length; i++) {
        if (e.target.classList[i] != '_serviceIcon') { className = e.target.classList[i] }
      }
      const targetIcon = $(`.${className}`)
      kakaoIcon.attr('class',`${className} _serviceIcon`);
      targetIcon.attr('class',`_kakao _serviceIcon`);

    }
  }
}
</script>

<style scoped>
    a {
      text-decoration: none;
    }

    .login{
        display: flex;
        min-width: 1200px;
    }
    .banner {
        position: relative;
        padding: 48px;
        width: 100%;
        min-height: 100vh;
        max-width: 768px;
        /* background: url(/bg.png) center center / cover no-repeat; */
        background-image: linear-gradient(45deg, rgb(13,202,120), rgb(11,203,156)); min-height:100%;
        display: flex;
    }
    .login-box {
        display: flex;
        flex-direction: column;
        background-color: rgb(255, 255, 255);
        width: calc(100% - 768px);
        min-height: 100vh;
    }
    .login-box-wrap {
        width: 480px;
        margin: auto;
    }
    .logo {
      margin-top:1%;
      margin-left:3%;
      background: url(/Vue.png) center center / cover no-repeat;

      height:50px;
      width:50px;
    }

    .login-text{
      text-align:center;
      color:#0CC476;
      padding-bottom:20px;
    }

    .divider {
      margin:auto;
      margin-bottom:20px;
      border-bottom:1px solid #0CC476;
      width:75px;
      border-width: 5px;
      border-radius: 5px;
    }

    .other-service {
        font-size:14px;
        line-height:14px;
        padding-top:18px;
        text-align:center;
        color:#8e8e8e;
    }
    .bar{
        display: inline-block;
        width:1px;
        height:18px;
        margin: 2px 3px;
        text-indent: -999em;
        background: #e4e4e5;
        vertical-align: bottom;
    }
    .other-service .bar {
        margin: 0 3px;
    }

    ._kakao{
        background-color: #ffcd00;
        background-image: url(https://statics.goorm.io/images/social/logo/kakaoLogo.svg);
    }

    ._naver{
        background-color: #1dc800;
        background-image: url(https://statics.goorm.io/images/social/logo/naverLogo.svg);
    }
    ._facebook{
        background-color: #3d5a98;
        background-image: url("https://statics.goorm.io/images/social/logo/FacebookLogo.svg");
    }

     ._serviceIcon{
        background-repeat: no-repeat;
        background-position: center;
        width: 40px;
        height: 40px;
        border-radius: 3px;
        -webkit-box-shadow: 0 0 1px 0 rgba(0, 0, 0, 0.12), 0 1px 1px 0 rgba(0, 0, 0, 0.24);
        box-shadow: 0 0 1px 0 rgba(0, 0, 0, 0.12), 0 1px 1px 0 rgba(0, 0, 0, 0.24);
        display: -ms-inline-flexbox;
        display: inline-flex;
        -ms-flex-pack: center;
        justify-content: center;
        margin:10px;
     }
    .add-option{
        margin-top: 30px;
    }
    .v-input__slot{
      margin:0 !important;
    }

    .v-ripple__container {
      display:none;
    }

    @media(max-width:768px){
      .banner {
        display: none;
      }
    }
</style>
