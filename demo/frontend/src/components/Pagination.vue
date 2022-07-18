<template>
  <div class="pagination-card">
    <ul class="pagination">
      <li class="pagination-item">
        <button
            class="button2"
            type="button"
            @click="onClickFirstPage"
            :disabled="isInFirstPage"
        >
          <i class="fa-solid fa-angles-left"></i>
        </button>
      </li>

      <li class="pagination-item">
        <button
            class="button2"
            type="button"
            @click="onClickPreviousPage"
            :disabled="isInFirstPage"
        >
          <i class="fa-solid fa-chevron-left"></i>
        </button>
      </li>
      <li
          v-for="page in pages"
          :key="page.name"
          class="pagination-item"
      >
        <button
            class="button1"
            type="button"
            @click="onClickPage(page.name)"
            :disabled="page.isDisabled"
            :class="{ active: isPageActive(page.name) }"
        >
          {{ page.name }}
        </button>
      </li>

      <li class="pagination-item">
        <button
            class="button2"
            type="button"
            @click="onClickNextPage"
            :disabled="isInLastPage"
        >
          <i class="fa-solid fa-angle-right"></i>
        </button>
      </li>

      <li class="pagination-item">
        <button
            class="button2"
            type="button"
            @click="onClickLastPage"
            :disabled="isInLastPage"
        >
          <i class="fa-solid fa-angles-right"></i>
        </button>
      </li>
    </ul>
  </div>
</template>


<script>
export default {
  name: 'PaginationComponent',
  props: {
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 3
    },
    totalPages: {
      type: Number,
      required: true
    },
    total: {
      type: Number,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    }
  },
  computed: {
    startPage() {
      if (this.currentPage === 1) {
        return 1;
      }

      if (this.currentPage === this.totalPages) {
        return (this.totalPages - this.maxVisibleButtons + 1 > 0 ? this.totalPages - this.maxVisibleButtons + 1 : 1);
      }

      return this.currentPage - 1;

    },
    endPage() {

      return Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages);

    },
    leftPage() {
      return this.currentPage - 1;
    },
    rightPage() {
      return this.currentPage + 1;
    },
    pages() {
      const range = [];

      // if (this.currentPage <= 3) {
      //
      // }
      for (let i = this.startPage; i <= this.endPage; i+= 1 ) {
        range.push({
          name: i,
          isDisabled: i === this.currentPage
        });
      }

      return range;
    },
    isInFirstPage() {
      return this.currentPage === 1;
    },
    isInLastPage() {
      return this.currentPage === this.totalPages;
    },
  },
  methods: {
    onClickFirstPage() {
      this.$emit('pagechanged', 1);
    },
    onClickPreviousPage() {
      this.$emit('pagechanged', this.currentPage - 1);
    },
    onClickPage(page) {
      this.$emit('pagechanged', page);
    },
    onClickNextPage() {
      this.$emit('pagechanged', this.currentPage + 1);
    },
    onClickLastPage() {
      this.$emit('pagechanged', this.totalPages);
    },
    isPageActive(page) {
      return this.currentPage === page;
    },
  }
}
</script>


<style lang="scss">
@import url('../assets/fontawesome-free-6.1.1/css/all.min.css');
.pagination-card {
  display: flex;
  justify-content: center;
  margin-top: 2em;
  margin-right: 2em;
  margin-bottom: 2em;
}
.pagination {
  list-style-type: none;
}

.pagination-item {
  display: inline-block;
  padding: 10px;
}

.active {
  background-color: lightblue;
  color: #ffffff;
}
.button1 {
  background: darken(#899EAF, 10%);
  padding: 10px;
  display: inline-block;
  outline: 0;
  border: 0;
  margin: -1px;
  border-radius: 2px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #F5F5F5;
  cursor: pointer;
  &:hover {
    background: #89C2C2;
    transition: all .4s ease-in-out;
  }
}
.button2 {
  background: darken(#FFFFFF, 10%);
  padding: 10px;
  display: inline-block;
  outline: 0;
  border: 0;
  margin: -1px;
  border-radius: 2px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #54697A;
  cursor: pointer;
  &:hover {
    background: #89C2C2;
    transition: all .4s ease-in-out;
  }
}
</style>