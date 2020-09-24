<template>
  <div>
    <v-row
      class="signup"
      align="center"
    >
      <div style="margin-top:100px;">
&nbsp;
      </div>
      <div style="width:100%;">
        <v-row
          justify="center"
        >
          <a href="/" class="logo" />
        </v-row>
        <v-row
          justify="center"
        >
          <h1 style="font-size:40px; font-weight:400;">
            <span class="success--text" style="font-weight:700; font-size:40px;">어린이ZIP</span> 회원가입
          </h1>
        </v-row>
        <v-row
          justify="center"
          style="margin-top:20px;"
        >
          <v-badge
            color="transparent"
            bottom
            offset-x="65"
            offset-y="65"
          >
            <template v-slot:badge>
              <v-btn fab depressed color="#e4e4e4" outlined style="background-color:white;">
                <v-icon color="#e4e4e4">
                  mdi-camera
                </v-icon>
              </v-btn>
            </template>
            <v-avatar width="184" height="184">
              <v-img src="/user2.png" />
            </v-avatar>
          </v-badge>
        </v-row>
        <v-row justify="center">
          <v-card
            class="form"
            tile
            hover
            outlined
            style="box-shadow:none;"
            :ripple="false"
          >
            <table width="100%">
              <tr width="100%">
                <th width="100%">
                  아이디
                </th>
              </tr>
              <tr width="100%;">
                <td width="100%">
                  <v-text-field
                    placeholder="아이디를 입력해 주세요."
                    color="grey"
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  비밀번호
                </th>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    placeholder="비밀번호를 입력해 주세요."
                    color="grey"
                    type="password"
                  />
                </td>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    placeholder="비밀번호를 다시 한번 입력해 주세요."
                    color="grey"
                    type="password"
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  닉네임
                </th>
              </tr>
              <tr width="100%">
                <td width="100%">
                  <v-text-field
                    placeholder="닉네임을 입력해 주세요."
                    color="grey"
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  이메일
                </th>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    placeholder="이메일을 입력해 주세요."
                    color="grey"
                  />
                </td>
              </tr>
              <div class="empty" />
              <tr>
                <th>
                  관심 지역
                </th>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    v-model="address"
                    placeholder="관심 지역을 입력해 주세요."
                    color="grey"
                    @click="openDaumZipAddress"
                  />
                </td>
              </tr>
            </table>
          </v-card>
        </v-row>
        <v-row
          justify="center"
          style="margin-top:20px;"
        >
          <v-btn
            color="#0dCA78"
            rounded
            x-large
            depressed
            dark
            style="width:240px;"
          >
            <span style="font-size:16px; font-weight:400">가입완료</span>
          </v-btn>
        </v-row>

        <div style="margin-bottom:100px;" />
      </div>
    </v-row>
  </div>
</template>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script type="text/JavaScript" src="http://dmaps.daum.net/map_js_init/postcode.v2.js"></script>
<script>
export default {
  data () {
    return {
        address: '',
    }
  },
  methods: {
    openDaumZipAddress() {
        var setAddress = this.setAddress;
        new daum.Postcode({
            oncomplete(data) {
                setAddress(data.address)
            }
        }).open();
    },

    setAddress(address) {
        this.address = address
    }
  }
}
</script>

<style scoped>
    @import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);
    * {
        font-family: "Noto Sans KR", sans-serif !important;
        font-size:16px;
    }
    .empty{
        height:15px;
    }
    tr{
        height:40px;
    }
    th{
        font-size:14px;
        font-weight: 700;
        text-align:left;
    }
    .v-badge__badge .v-icon {
        color: inherit;
        font-size: 36px;
        margin: 0 -2px;
    }
    .v-badge__badge{
        border-color: #666666 !important;
    }
    .logo {
      background: url(/Vue.png) center center / cover no-repeat;
      margin-bottom:5px;
      height:50px;
      width:50px;
    }
    .signup {
        background-color: #f9f9f9;
        width:100%;
        margin:0;
    }

    .form {
      margin: 20px 0px;
      width: 600px;
      padding:24px 36px;
    }

    .v-text-field{
        padding:0;
        margin:0;
    }
</style>
