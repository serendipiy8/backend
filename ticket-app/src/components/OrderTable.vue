<!-- OrderTable.vue -->
<template>
  <div>
    <h2>Order Data Table</h2>
    <table>
      <thead>
        <tr>
          <th v-for="header in tableHeaders" :key="header">{{ header }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order[uniqueKey]">
          <td v-for="field in tableFields" :key="field">{{ order[field] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    responseData: {
      type: Object,
      default: () => ({
        code: "2000",
        data: [],
        message: "successfully!",
      }),
    },
    tableHeaders: {
      type: Array,
      default: () => [],
    },
    tableFields: {
      type: Array,
      default: () => [],
    },
    uniqueKey: {
      type: String,
      default: "OrderID",
    },
  },
  computed: {
    orders() {
      return this.responseData.data || [];
    },
  },
};
</script>

<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}</style>
