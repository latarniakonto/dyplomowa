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
          'p-invalid': depositEdited && !editingDeposit.check,
        }"
      >
        <h6 class="mb-2">Deposit Check</h6>
        <InputNumber
          id="check"
          v-model="editingDeposit.check"
          mode="currency"
          currency="PLN"
          :min="0.01"
          :maxFractionDigits="2"
          autofocus
          required="true"
          :class="{
            'p-invalid': depositEdited && !editingDeposit.check,
          }"
          @input="updateDepositCheck($event)"
        />
        <small class="p-error" v-if="depositEdited && !editingDeposit.check"
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
              !editingDeposit.deposit &&
              !editingDeposit.withdraw &&
              !editingDeposit.override,
          }"
        >
          <ToggleButton
            id="deposit"
            class="mr-2"
            v-model="editingDeposit.deposit"
            onLabel="Deposit money"
            offLabel="Deposit money"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            :class="{
              'p-invalid':
                depositEdited &&
                !editingDeposit.deposit &&
                !editingDeposit.withdraw &&
                !editingDeposit.override,
            }"
            @change="editingDeposit.deposit = setDepositAction()"
          />
          <ToggleButton
            id="withdraw"
            class="mr-2"
            v-model="editingDeposit.withdraw"
            onLabel="Withdraw money"
            offLabel="Withdraw money"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            :class="{
              'p-invalid':
                depositEdited &&
                !editingDeposit.deposit &&
                !editingDeposit.withdraw &&
                !editingDeposit.override,
            }"
            @change="editingDeposit.withdraw = setDepositAction()"
          />
          <ToggleButton
            id="override"
            v-model="editingDeposit.override"
            onLabel="Override money"
            offLabel="Override money"
            onIcon="pi pi-check"
            offIcon="pi pi-times"
            :class="{
              'p-invalid':
                depositEdited &&
                !editingDeposit.deposit &&
                !editingDeposit.withdraw &&
                !editingDeposit.override,
            }"
            @change="editingDeposit.override = setDepositAction()"
          />
        </div>
        <small
          class="p-error"
          v-if="
            depositEdited &&
            !editingDeposit.deposit &&
            !editingDeposit.withdraw &&
            !editingDeposit.override
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
            v-if="editingDeposit.check"
            class="font-medium variable-value"
            >{{ editingDeposit.check }}</span
          >
        </div>
        <div class="operation-line mb-1 text-2xl">
          <span v-if="editingDeposit.deposit" class="mdi mdi-plus"></span>
          <span v-if="editingDeposit.withdraw" class="mdi mdi-minus"></span>
          <span v-if="editingDeposit.override" class="mdi mdi-equal"></span>
        </div>
        <div>
          <span class="text-muted variable">New deposit value</span>
          <span
            v-if="
              editingDeposit.check &&
              (editingDeposit.deposit ||
                editingDeposit.withdraw ||
                editingDeposit.override)
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
      type: Object,
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
    depositEdited: (deposit: any) => true,
    depositEditingCanceled: () => true,
  },

  data() {
    return {
      depositEdited: false as Boolean,
      editingDeposit: {} as any,
    };
  },

  methods: {
    cancelDepositEditing() {
      this.editingDeposit = {};
      this.depositEdited = false;
      this.$emit("depositEditingCanceled");
    },

    editDeposit() {
      this.depositEdited = true;
      if (
        this.editingDeposit.check &&
        (this.editingDeposit.deposit ||
          this.editingDeposit.withdraw ||
          this.editingDeposit.override)
      ) {
        this.$emit("depositEdited", this.editingDeposit);

        this.editingDeposit = {};
        this.depositEdited = false;
      }
    },

    setDepositAction(): Boolean {
      this.editingDeposit.deposit = false;
      this.editingDeposit.withdraw = false;
      this.editingDeposit.override = false;

      return true;
    },

    updateDepositCheck(e: any) {
      // Component InputNumber doesn't support v-model to this extent.
      // So here is a workaround.
      this.editingDeposit.check = e.value;
    },

    calculateDepositValue(): String {
      if (!this.portfolio.deposit || !this.editingDeposit.check) {
        return "CalculateDepositValue error: this.portfolio.deposit and this.editingDeposit.check seems to be missing.";
      }

      if (this.editingDeposit.deposit) {
        return String(
          Number(this.portfolio.deposit) + Number(this.editingDeposit.check)
        );
      } else if (this.editingDeposit.withdraw) {
        return String(
          Number(this.portfolio.deposit) - Number(this.editingDeposit.check)
        );
      }
      return String(Number(this.editingDeposit.check));
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
