<template>
  <div class="resources position-relative">
    <h6>Deposit</h6>
    <div
      v-if="!addPressed && !substractPressed && !editPressed"
      class="form-floating input-group mb-2"
    >
      <input
        v-model="text"
        :disabled="true"
        type="number"
        class="form-control bg-main-color"
      />
      <button class="btn btn-outline-secondary btn-icon" @click="toggleAdd()">
        <i class="bi bi-plus-square"></i>
      </button>
      <button
        class="btn btn-outline-secondary btn-icon"
        @click="toggleSubstract()"
      >
        <i class="bi bi-dash-square"></i>
      </button>
      <button class="btn btn-outline-secondary btn-icon" @click="toggleEdit()">
        <i class="bi bi-pencil-square"></i>
      </button>
    </div>
    <div v-else class="form-floating input-group mb-2">
      <input
        v-model="currentText"
        :disabled="false"
        id="input-deposit"
        type="number"
        class="form-control bg-main-color"
      />
      <label for="input-deposit">{{ text }}</label>
      <button
        class="btn btn-outline-secondary"
        :class="{
          'btn-icon': !addPressed,
          'btn-icon-pressed': addPressed,
        }"
        @click="toggleAdd()"
      >
        <i class="bi bi-plus-square"></i>
      </button>
      <button
        class="btn btn-outline-secondary"
        :class="{
          'btn-icon': !substractPressed,
          'btn-icon-pressed': substractPressed,
        }"
        @click="toggleSubstract()"
      >
        <i class="bi bi-dash-square"></i>
      </button>
      <button
        class="btn btn-outline-secondary"
        :class="{
          'btn-icon': !editPressed,
          'btn-icon-pressed': editPressed,
        }"
        @click="toggleEdit()"
      >
        <i class="bi bi-pencil-square"></i>
      </button>
    </div>
    <h6>Cash on hand</h6>
    <div class="input-group mb-2">
      <input
        :disabled="true"
        type="number"
        class="form-control bg-main-color"
        value="2000"
      />
    </div>
    <h6>No. of transaction</h6>
    <div class="input-group mb-2">
      <input
        :disabled="true"
        type="number"
        class="form-control bg-main-color"
        value="9"
      />
    </div>
    <h6>Transaction cost</h6>
    <div class="input-group mb-2">
      <input
        :disabled="true"
        type="number"
        class="form-control bg-main-color"
        value="120"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "PortfolioDashboard",

  data() {
    return {
      addPressed: false as Boolean,
      substractPressed: false as Boolean,
      editPressed: false as Boolean,
      text: "30000" as String,
      currentText: "" as String,
    };
  },

  methods: {
    toggleAdd: function () {
      this.substractPressed = this.editPressed = false;
      if (!this.addPressed) {
        this.currentText = "";
      } else {
        this.text = String(Number(this.text) + Number(this.currentText));
      }
      this.addPressed = !this.addPressed;
    },

    toggleSubstract: function () {
      this.addPressed = this.editPressed = false;
      if (!this.substractPressed) {
        this.currentText = "";
      } else {
        this.text = String(Number(this.text) - Number(this.currentText));
      }
      this.substractPressed = !this.substractPressed;
    },

    toggleEdit: function () {
      this.substractPressed = this.addPressed = false;
      if (!this.editPressed) {
        this.currentText = "";
      } else {
        this.text = this.currentText === "" ? this.text : this.currentText;
      }
      this.editPressed = !this.editPressed;
    },
  },
});
</script>

<style>
button.btn-icon {
  background-color: #f6f6f6;
  color: rgba(0, 0, 0, 0.87);
  border-color: #a4a4a4;
  z-index: 3;
}

button.btn-icon:hover {
  background-color: #ededed;
  color: rgba(0, 0, 0, 0.87);
  border-color: #393939;
  z-index: 3;
}

button.btn-icon:active:focus {
  background-color: #ededed;
  color: rgba(0, 0, 0, 0.87);
  border-color: #393939;
  z-index: 3;
}

button.btn-icon-pressed:hover {
  background-color: #ededed;
  color: rgba(0, 0, 0, 0.87);
  border-color: #393939;
  z-index: 3;
}

button.btn-icon-pressed {
  background-color: #ededed;
  color: rgba(0, 0, 0, 0.87);
  border-color: #393939;
}

.input-group > button.btn-icon-pressed {
  z-index: 3;
}

button.btn-icon-pressed:active:focus {
  background-color: #ededed;
  color: rgba(0, 0, 0, 0.87);
  border-color: #393939;
  z-index: 3;
}

input[type="number"]:disabled {
  background-color: #f6f6f6;
  color: rgba(0, 0, 0, 0.87);
  letter-spacing: 0.15px;
  line-height: 24px;
  border-color: #a4a4a4;
  -moz-appearance: textfield;
}

input[type="number"]:enabled {
  background-color: #f6f6f6;
  color: rgba(0, 0, 0, 0.87);
  letter-spacing: 0.15px;
  line-height: 24px;
  border-color: #a4a4a4;
  -moz-appearance: textfield;
}

/* input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
} */

.form-floating > label {
  z-index: 5;
  margin: -8px;
}

.resources .form-floating .form-control:not(:placeholder-shown):disabled {
  height: 38px;
  padding-top: 0.375rem;
  padding-right: 0.75rem;
  padding-bottom: 0.375rem;
  padding-left: 0.75rem;
  font-size: 1rem;
  font-weight: 400;
}

.resources .form-floating .form-control:not(:placeholder-shown):enabled {
  height: 38px;
  padding-top: 1.25rem;
  padding-right: 0.75rem;
  padding-bottom: 0.375rem;
  padding-left: 0.75rem;
  font-size: 1rem;
  font-weight: 400;
}
</style>
