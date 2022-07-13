<template>
  <div class="left-box">
    <div class="label-input">
      <h3>Tìm kiếm nâng cao</h3>
      <input
        type="text"
        placeholder="Tên sản phẩm"
        v-model="field.name"
      /><br /><br />
      <input
        type="text"
        placeholder="Hãng"
        v-model="field.brand"
      /><br /><br />
      <input
        type="text"
        placeholder="Khối lượng giặt"
        v-model="field.loadSize"
      /><br /><br />
      <label>Lọc theo giá (triệu VNĐ): </label>
      <input
        type="number"
        placeholder="Nhỏ nhất"
        v-model="field.minPrice"
      /><br /><br />
      <input
        type="number"
        placeholder="Lớn nhất"
        v-model="field.maxPrice"
      /><br /><br />
      <label>Lọc theo hãng: </label>
      <input
        type="text"
        placeholder="Toshiba, Samsung, ..."
        v-model="field.brand"
      /><br /><br />
      <label>Lọc theo khối lượng giặt (kg): </label>
      <input
        type="number"
        placeholder="9, 9.5, ..."
        v-model="field.loadSize"
      /><br /><br />
      <div class="label-input">
        <button class="button" @click="handleFilter">Lọc</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LeftBar",
  props: {},
  data() {
    return {
      field: {
        title: null,
        city: null,
        district: null,
        minPrice: null,
        maxPrice: null,
        brand: null,
        loadSize: null,
      },
      data: null,
    };
  },
  methods: {
    // async searchData() {
    //   try {
    //     console.log(this.field.city)
    //     const response = await this.$http.post(
    //       "http://localhost:5000/house-filter",
    //       {
    //         giaMin: this.field.minPrice,
    //         giaMax: this.field.maxPrice,
    //         tieuDe: this.field.title,
    //         thanhPho: this.field.city,
    //         quan: this.field.district,
    //         dienTichMin: this.field.minSquare,
    //         dienTichMax: this.field.maxSquare
    //       }
    //     );
    //     console.log(response.data.houselist)
    //     // JSON responses are automatically parsed.
    //     this.data = response.data
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    handleFilter() {
      // this.searchData()
      console.log(this.field);
      this.$emit("pageFilter", this.field);
    },
  },
};
</script>

<style lang="scss" scoped>
.left-box {
  font-size: 15px;
  align-items: center;
  //justify-content: center;
  padding-left: 2em;
  padding-right: 13em;
  width: 20%;
  //padding-left: 1em;
  //font-size: 15px;
}
//input {
//  padding: 0.3em;
//  width: 10em;
//  margin-right: 1em;
//}
//label {
//  font-size: 16px;
//}
.button {
  background: darken(#a3b8ca, 10%);
  padding: 10px;
  display: inline-block;
  outline: 0;
  border: 0;
  margin: -1px;
  border-radius: 2px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #f5f5f5;
  cursor: pointer;
  &:hover {
    background: #89c2c2;
    transition: all 0.4s ease-in-out;
  }
  margin-left: 8px;
}
//.label-input {
//  display: flex;
//  align-items: flex-start;
//  width: 10em;
//}
.label-input-2 {
  display: flex;
  align-items: flex-start;
  width: 5em;
}
.label-input {
  margin-bottom: 5px;
  width: 330%;
  input {
    border-radius: 4px;
    height: 40px;
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    width: 120%;
    margin: 0.5em;
    border: 1px solid #b5b5b5;
    padding-left: 10px;
    //&.has-error {
    //  color: red !important;
    //  border: 1px solid red;
    //}
    //&::placeholder,
    //&::-webkit-input-placeholder,
    //&:-ms-input-placeholder {
    //  color: #8F9BB3;
    //  font-size: 15px;
    //  line-height: 20px;
    //  font-weight: 400;
    //  padding-left: 5px;
    //}
    //&:disabled {
    //  background-color: #DDD;
    //}
    //.right-input {
    //  float: right;
    //}
  }
  &.is-one-line {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    label {
      display: block;
      width: 150px;
    }
  }
  //&.flex-column {
  //  display: flex;
  //  flex-direction: column;
  //  label {
  //    color: #3366ff;
  //    font-size: 12px;
  //    font-weight: bold;
  //    line-height: 16px;
  //  }
  //}
  //&.subinformations {
  //  display: flex;
  //  flex-direction: column;
  //  label {
  //    color: #808080;
  //    font-size: 11px;
  //    font-weight: bold;
  //    line-height: 5px;
  //  }
  //  .value {
  //    font-size: 12px;
  //    line-height: 14px;
  //  }
  //}
  //.select {
  //  position: relative;
  //  display: flex;
  //  width: 100%;
  //  height: 40px;
  //  line-height: 3;
  //  background: #F8F9FA;
  //  overflow: hidden;
  //  border: 1px solid #e1e7ec;
  //  border-radius: 24px;
  //  .select-value {
  //    position: absolute;
  //    height: 40px;
  //    line-height: 40px;
  //    padding-left: 20px;
  //    color: #222B45;
  //    font-size: 15px;
  //    font-weight: 600;
  //  }
  //  select {
  //    -webkit-appearance: none;
  //    -moz-appearance: none;
  //    -ms-appearance: none;
  //    appearance: none;
  //    outline: 0;
  //    box-shadow: none;
  //    border: 0 !important;
  //    background: #F8F9FA;
  //    background-image: none;
  //    flex: 1;
  //    padding: 0 .5em;
  //    color: #fff;
  //    cursor: pointer;
  //    width: 100%;
  //    &::-ms-expand {
  //      display: none;
  //    }
  //    option {
  //      color: black
  //    }
  //  }
  //  &::after {
  //    content: '\2304';
  //    position: absolute;
  //    top: 0;
  //    right: 0;
  //    padding: 0 1em;
  //    background: #F8F9FA;
  //    cursor: pointer;
  //    pointer-events: none;
  //    -webkit-transition: .25s all ease;
  //    -o-transition: .25s all ease;
  //    transition: .25s all ease;
  //    line-height: 30px;
  //  }
  //  &:hover::after {
  //    color: #ffe74c;
  //  }
  //}
  //input[type=checkbox] {
  //  display: none;
  //  &:disabled+label {
  //    color: #808080;
  //    cursor: default !important;
  //  }
  //  &:disabled+label:before {
  //    background-color: #e8e8e8;
  //    cursor: default !important;
  //  }
  //  &+label {
  //    display: block;
  //    margin: 0.2em;
  //    cursor: pointer;
  //    padding: 0.2em;
  //    color: #222B45;
  //    font-size: 15px;
  //    line-height: 24px;
  //    font-weight: 600;
  //    &:before {
  //      content: "\2714";
  //      border: 0.1em solid #8992A3;
  //      border-radius: 0.2em;
  //      display: inline-block;
  //      width: 20px;
  //      height: 20px;
  //      margin-right: 10px;
  //      vertical-align: bottom;
  //      color: transparent;
  //      transition: .2s;
  //      line-height: 16px;
  //      text-align: center;
  //    }
  //    &:active:before {
  //      transform: scale(0);
  //    }
  //  }
  //  &:checked+label:before {
  //    background-color: #3366ff;
  //    border-color: #3366ff;
  //    color: white;
  //  }
  //  &:disabled+label:before {
  //    transform: scale(1);
  //    border-color: #aaa;
  //  }
  //  &:checked:disabled+label:before {
  //    transform: scale(1);
  //    background-color: #bfb;
  //    border-color: #bfb;
  //  }
  //}
}
</style>
