<template>
  <div v-if="visible" class="form-entry flex-column input-item">
    <label>{{ label }}</label>
    <div v-if="isEditing">
      <input
          :type="inputType"
          v-model="input"
          :placeholder="placeholder"
          :class="[valid ? '' : 'has-error']"
      />
    </div>
  </div>
</template>

<script>

export default {
  name: 'InputItem',
  props: {
    isEditing: {
      type: Boolean,
      default: false
    },
    visible: {
      type: Boolean,
      default: true
    },
    label: {
      type: String,
      default: ''
    },
    inputType: {
      type: String,
      default: 'text'
    },
    placeholder: {
      type: String,
      default: ''
    },
    isValid: {
      type: Boolean,
      default: true
    },
    mandatory: {
      type: Boolean,
      default: false
    },
    value: {
      type: [String, Number],
      default: ''
    },
    isOnlyAlpha: {
      type: Boolean,
      default: true
    },
    isOnlyNumeric: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    valid() {
      return this.isValid
    },
    input: {
      get() {
        if (this.isOnlyAlpha) {
          let checkedText = this.value !== null ? this.value.replace(/[a-zA-Z]+/g, '') : this.value
          return checkedText
        } else if (this.isOnlyNumeric) {
          let checkedText = this.value !== null ? this.value.replace(/[0-9]+/g, '') : this.value
          return checkedText
        }
        return this.value
      },
      set(value) {
        this.$emit('input', value)
      }
    }
  },
  methods: {

  }
}
</script>