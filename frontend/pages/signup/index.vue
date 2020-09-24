<template>
  <div>
    <v-row
      class="select-signup"
      align="center"
    >
      <div style="width:100%;">
        <v-row
          justify="center"
        >
          <a href="/" class="logo" />
        </v-row>
        <v-row
          justify="center"
        >
          <h1 style="font-size:40px;">
            <span class="success--text" style="font-weight:800;">어린이ZIP</span> 회원가입
          </h1>
        </v-row>
        <v-row
          justify="center"
        >
          <h3 style="font-size:20px;margin:10px 0 40px 0; color:#666666;">
            본인이 해당하시는 가입 유형을 아래에서 선택해주세요.
          </h3>
        </v-row>
        <v-row>
          <v-col v-for="(type,i) in types" :key="`${i}_type`" :cols="6">
            <v-row
              :justify="type.justify"
            >
              <v-card
                class="select-card"
                tile
                hover
                style="box-shadow:none;"
                :ripple="false"
                :to="`/signup/${type.id}`"
              >
                <v-row justify="center">
                  <div class="card-img" :style="{'width': type.width}">
                    <v-img :src="type.src" />
                  </div>
                </v-row>
                <v-row justify="center">
                  <h3 v-text="type.title" />
                </v-row>
                <v-row justify="start">
                  <div style="font-size:14px; margin-top:10px;" v-html="type.contents" />
                </v-row>
                <v-row justify="center">
                  <v-btn
                    color="#0dCA78"
                    rounded
                    x-large
                    depressed
                    dark
                    style="margin-top:30px; width:60%;"
                  >
                    <span style="font-size:16px"><b>선택하기</b></span>
                  </v-btn>
                </v-row>
              </v-card>
            </v-row>
          </v-col>
        </v-row>
        <v-row
          justify="center"
          style="margin-top:20px;"
        >
          이미 계정이 있으신가요?
          <nuxt-link to="/login" style="margin-left:5px;">
            로그인
          </nuxt-link>
        </v-row>
      </div>
    </v-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      types: [
        {
          id: 'parents',
          justify: 'end',
          width: '113px',
          src: 'https://d1ta1myjmiqbpz.cloudfront.net/static/images/join_login/img_parents01.png',
          title: '학부모',
          contents: '맞춤형 어린이집 추천과 함께 우리 아이의 어린이집 리뷰를 보실 수 있습니다.'

        },
        {
          id: 'kindergarden',
          justify: 'start',
          width: '86px',
          src: 'https://d1ta1myjmiqbpz.cloudfront.net/static/images/join_login/img_academy01.png',
          title: '어린이집',
          contents: '원격으로 학부모님들에게 어린이집에 대해 상담해드릴 수 있습니다. '
        }
      ]
    }
  }
}
</script>

<style scoped>
    .logo {
      background: url(/Vue.png) center center / cover no-repeat;
      margin-bottom:5px;
      height:50px;
      width:50px;
    }
    .select-card:hover {
      box-shadow: 0 4px 4px 0 rgba(0,0,0,0.2) !important;
    }
    .select-signup {
        background-color: #f9f9f9;
        height:100vh;
        width:100%;
        margin:0;
    }

    .select-card {
      margin: 0px 20px;
      width: 282px;
      padding:36px;
    }

    .card-img{
      margin: 24px 0 42px 0;
      vertical-align: top;
    }
</style>
