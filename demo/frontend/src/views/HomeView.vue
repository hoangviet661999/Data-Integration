<template>
  <div class="home">
    <div class="box">
      <aside v-if="hasData">
        <!--        <div class="left-box">-->
        <LeftBar @pageFilter="pageFilter" />
        <!--        </div>-->
      </aside>
      <div class="right-box">
        <div v-if="hasData" class="item-list">
          <ItemList :deviceList="deviceList" />
          <Pagination
            :current-page="currentPage"
            :total="total"
            :per-page="numOfDevicePerPage"
            :total-pages="totalPages"
            @pagechanged="onPageChange"
          />
        </div>
        <!--      <div v-else>-->
        <!--        <p>Không tìm thấy dữ liệu phù hợp</p>-->
        <!--      </div>-->
      </div>
    </div>
  </div>
</template>

<script>
import ItemList from "../components/ItemList";
import LeftBar from "../components/LeftBar";
import Pagination from "../components/Pagination";
// import {mapGetters} from 'vuex';
export default {
  components: {
    ItemList,
    LeftBar,
    Pagination,
  },
  props: {
    numOfDevicePerPage: {
      type: Number,
      default: 20,
    },
  },
  data() {
    return {
      currentPage: 1,
      total: 0,
      totalPages: 0,
      deviceList: [],
      firstIndex: 0,
      lastIndex: this.numOfDevicePerPage - 1,
      hasData: true,
      field: {},
    };
  },
  methods: {
    async getData() {
      try {
        this.hasData = false;
        const response1 = await this.$http.post(
          "http://localhost:5000/get-total"
        );
        this.total = response1.data.soLuong;
        const response2 = await this.$http.post(
          "http://localhost:5000/device-list",
          {
            page: this.currentPage,
          }
        );
        console.log(response2.data.devicelist);
        // JSON responses are automatically parsed.
        this.deviceList = response2.data.deviceList;
        // this.total = response.data.soLuong;
        this.totalPages = Math.ceil(this.total / this.numOfDevicePerPage);
        console.log(this.totalPages);
        console.log(this.total);
        console.log(this.deviceList);
        this.hasData = true;
      } catch (error) {
        this.hasData = false;
        console.log(error);
      }
    },
    async searchData(field) {
      try {
        const response = await this.$http.post(
          "http://localhost:5000/device-filter",
          {
            name: field.name,
            minPrice: field.minPrice,
            maxPrice: field.maxPrice,
            brand: field.brand,
            type: field.type,
            loadSize: field.loadSize,
          }
        );
        console.log(response.data.deviceList);
        // JSON responses are automatically parsed.
        this.deviceList = response.data.deviceList;
        this.total = response.data.soLuong;
        this.totalPages = Math.ceil(this.total / this.numOfDevicePerPage);
        console.log(this.totalPages);
        console.log(this.total);
        console.log(this.deviceList);
      } catch (error) {
        console.log(error);
      }
    },
    // getRenderHouse() {
    //   let first = this.firstIndex
    //   let last = this.lastIndex
    //   if (this.deviceList != null) {
    //     return this.deviceList.slice(first, last + 1);
    //   } else {
    //     return []
    //   }
    // },
    onPageChange(page) {
      // console.log(page)
      this.currentPage = page;
      this.getData();
      // this.firstIndex = (page - 1) * this.numOfDevicePerPage;
      // this.lastIndex = Math.min(page * this.numOfDevicePerPage - 1, this.total - 1);
    },
    pageFilter(field) {
      console.log(field);
      this.searchData(field);
    },
  },
  computed: {},
  mounted() {
    this.getData();
  },
};
</script>

<style scoped lang="css">
.home {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  background-color: #dfe7e7;
}
.box {
  background-color: white;
  display: flex;
  margin-left: 5em;
  margin-right: 15em;
  margin-top: 5em;
  border-radius: 10px;
}
.right-box {
  /*padding-right: 2em;*/
  /*width: 100%;*/
  /*height: calc(100% - 70px);*/
  /*box-sizing: border-box;*/
  /*position: relative;*/
  /*height: 350px;*/
  /*flex: 1;*/
  /*display: flex;*/
  -webkit-box-flex: 4;
  -ms-flex: 4;
  flex: 3;
  padding-left: 40px;
}
.left-box {
  /*width: 30%;*/
  /*height: 100%;*/
  /*color: black;*/
  /*flex: 1;*/
  /*!*opacity: 0;*!*/
  /*display: flex;*/
  /*justify-content: center;*/
  /*align-items: center;*/
  /*font-size: 30px;*/
  /*flex-direction: column;*/

  /*-webkit-box-flex: 1;*/
  /*-ms-flex: 1;*/
  /*flex: 2;*/
  /*padding-right: 40px;*/
  /*border-right: 1px solid #eee;*/

  /*padding-right: 7em;*/
  /*padding-left: 1em;*/
  /*border-right: 1px solid #eee;*/
  /*font-size: 15px;*/
}

aside {
}
</style>
