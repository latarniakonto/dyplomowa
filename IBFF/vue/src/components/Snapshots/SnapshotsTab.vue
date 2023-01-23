<template>
  <div class="snapshots-tab">
    <div class="card">
      <div class="table-toolbar">
        <Toolbar class="mb-4">
          <template #start>
            <Button
              label="Take Snapshot"
              icon="pi pi-plus"
              class="p-button-success mr-2"
              @click="takeSnapshot()"
            />
          </template>
        </Toolbar>
      </div>
      <SnapshotsTable :snapshots="snapshots" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SnapshotsTable from "./SnapshotsTable.vue";
import Toolbar from "primevue/toolbar";
import Button from "primevue/button";
import { axios } from "../../common/api.service";
import { Snapshot, SnapshotJSON } from "../../common/models";

export default defineComponent({
  name: "TransactionsTab",

  components: {
    SnapshotsTable,
    Toolbar,
    Button,
  },

  data() {
    return {
      snapshots: [] as Array<Snapshot>,
      portfolioSlug: "" as String,
    };
  },

  methods: {
    async getSnapshots() {
      if (this.$store.state.portfolio.slug === undefined) {
        return;
      }

      let endpoint = `api/v1/portfolios/${this.$store.state.portfolio.slug}/snapshots/`;

      try {
        let response = await axios.get(endpoint);
        let jsons = response.data;
        jsons.forEach((json: any) => {
          this.snapshots.push(new Snapshot(json as SnapshotJSON));
        });
      } catch (e: any) {
        console.error(e.response);
      }
    },

    async takeSnapshot() {
      if (this.$store.state.portfolio.slug === undefined) {
        return;
      }

      let endpoint = `api/v1/portfolios/${this.$store.state.portfolio.slug}/snapshots/get_or_create/`;

      try {
        let response = await axios.get(endpoint);
        let newSnapshot = new Snapshot(response.data as SnapshotJSON);

        if (this.snapshots.length === 0) {
          this.snapshots.push(newSnapshot);
        } else if (
          newSnapshot.date.getFullYear() > this.snapshots[0].date.getFullYear()
        ) {
          this.snapshots.unshift(newSnapshot);
        } else {
          this.snapshots.splice(0, 1, newSnapshot);
        }
      } catch (e: any) {
        console.error(e.response);
      }
    },
  },

  created() {
    this.getSnapshots();
  },
});
</script>

<style>
.snapshots-tab .table-toolbar {
  background-color: #f6f6f6;
  height: 60px;
}

.snapshots-tab .table-toolbar .p-toolbar {
  background-color: #f6f6f6;
  border-color: #a4a4a4;
  padding: 0.3rem 0 0 0.3rem;
}
</style>
