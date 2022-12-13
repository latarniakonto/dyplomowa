<template>
  <Dialog
    :visible="editDepositDialog"
    :style="{ width: '450px' }"
    :modal="true"
    class="p-fluid"
    @update:visible="cancelDepositEditing()"
  >
    <template #header>
      <h4>Deposit Details</h4>
    </template>
    <div class="deposit-core mb-3">
      <div
        class="deposit-check mb-3"
        :class="{
          'p-invalid': depositEdited && !check.value,
        }"
      >
        <h6 class="mb-2">Deposit Check</h6>
        <InputNumber
          id="check"
          v-model="check.value"
          mode="currency"
          currency="PLN"
          :min="0.01"
          :maxFractionDigits="2"
          autofocus
          required="true"
          :class="{
            'p-invalid': depositEdited && !check.value,
          }"
          @input="updateDepositCheck($event)"
        />
        <small class="p-error" v-if="depositEdited && !check.value"
          >You need to specify a deposit check.</small
        >
      </div>
      <h6 class="mb-2">Deposit Actions</h6>
      <div id="actions" class="deposit-actions">
        <div
          class="d-flex"
          :class="{
            'p-invalid':
              depositEdited &&
              !check.deposit &&
              !check.withdraw &&
              !check.override,
          }"
        >
          <ToggleButton
            id="deposit"
            class="mr-2"
            v-model="check.deposit"
            onLabel="Deposit money"
            offLabel="Deposit money"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            :class="{
              'p-invalid':
                depositEdited &&
                !check.deposit &&
                !check.withdraw &&
                !check.override,
            }"
            @change="check.deposit = setDepositAction()"
          />
          <ToggleButton
            id="withdraw"
            class="mr-2"
            v-model="check.withdraw"
            onLabel="Withdraw money"
            offLabel="Withdraw money"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            :class="{
              'p-invalid':
                depositEdited &&
                !check.deposit &&
                !check.withdraw &&
                !check.override,
            }"
            @change="check.withdraw = setDepositAction()"
          />
          <ToggleButton
            id="override"
            v-model="check.override"
            onLabel="Override money"
            offLabel="Override money"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            :class="{
              'p-invalid':
                depositEdited &&
                !check.deposit &&
                !check.withdraw &&
                !check.override,
            }"
            @change="check.override = setDepositAction()"
          />
        </div>
        <small
          class="p-error"
          v-if="
            depositEdited &&
            !check.deposit &&
            !check.withdraw &&
            !check.override
          "
          >You need to specify a deposit action.</small
        >
      </div>
    </div>
    <h6 class="mb-2">Deposit Overview</h6>
    <div id="overview" class="deposit-overview">
      <div class="arithmetic-operation">
        <div class="mb-1">
          <span class="text-muted variable">Initital deposit value</span>
          <span class="font-medium variable-value">{{
            portfolio.deposit
          }}</span>
        </div>
        <div class="mb-1">
          <span class="text-muted variable">Deposit modifier</span>
          <span
            v-if="check.value"
            class="font-medium variable-value"
            >{{ check.value }}</span
          >
        </div>
        <div class="operation-line mb-1 text-2xl">
          <span v-if="check.deposit" class="mdi mdi-plus"></span>
          <span v-if="check.withdraw" class="mdi mdi-minus"></span>
          <span v-if="check.override" class="mdi mdi-equal"></span>
        </div>
        <div>
          <span class="text-muted variable">New deposit value</span>
          <span
            v-if="
              check.value &&
              (check.deposit ||
                check.withdraw ||
                check.override)
            "
            class="font-medium variable-value"
          >
            {{ calculateDepositValue() }}
          </span>
        </div>
      </div>
    </div>
    <template #footer>
      <Button
        label="Cancel"
        icon="pi pi-times"
        class="p-button-text"
        @click="cancelDepositEditing()"
      />
      <Button
        label="Save"
        icon="pi pi-check"
        class="p-button-text"
        @click="editDeposit()"
      />
    </template>
  </Dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Dialog from "primevue/dialog";
import InputNumber from "primevue/inputnumber";
import ToggleButton from "primevue/togglebutton";
import { Portfolio, Check } from "../../common/models";

export default defineComponent({
  name: "EditDepositDialog",

  components: {
    Button,
    InputText,
    Dialog,
    InputNumber,
    ToggleButton,
  },

  props: {
    portfolio: {
      type: Object as () => Portfolio,
      required: true,
      default: {},
    },
    editDepositDialog: {
      type: Boolean,
      required: true,
      default: false,
    },
  },

  emits: {
    depositEdited: (check: Check) => true,
    depositEditingCanceled: () => true,
  },

  data() {
    return {
      depositEdited: false as Boolean,
      check: new Check(),
    };
  },

  methods: {
    cancelDepositEditing() {
      this.check = new Check();
      this.depositEdited = false;
      this.$emit("depositEditingCanceled");
    },

    editDeposit() {
      this.depositEdited = true;
      if (
        this.check.value &&
        (this.check.deposit ||
          this.check.withdraw ||
          this.check.override)
      ) {
        this.$emit("depositEdited", this.check);

        this.check = new Check();
        this.depositEdited = false;
      }
    },

    setDepositAction(): Boolean {
      this.check.deposit = false;
      this.check.withdraw = false;
      this.check.override = false;

      return true;
    },

    updateDepositCheck(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.check.value = e.value;
    },

    calculateDepositValue(): String {
      if (!this.check.value) {
        return "CalculateDepositValue error: this.check.value seems to be missing.";
      }

      if (this.check.deposit) {
        return String(
          Number(this.portfolio.deposit) + Number(this.check.value)
        );
      } else if (this.check.withdraw) {
        return String(
          Number(this.portfolio.deposit) - Number(this.check.value)
        );
      }
      return String(Number(this.check.value));
    },
  },
});
</script>

<style>
#deposit.p-togglebutton.p-button.p-highlight {
  background: green;
}

#withdraw.p-togglebutton.p-button.p-highlight {
  background: red;
}

#override.p-togglebutton.p-button.p-highlight {
  background: yellow;
}

.p-togglebutton.p-button.p-invalid {
  border-color: #b00020;
}

.arithmetic-operation {
  display: flex;
  flex-direction: column;
}

.operation-line {
  border-bottom: solid 2px #a4a4a4;
}

.variable {
  float: left;
}

.variable-value {
  float: right;
}
</style>
