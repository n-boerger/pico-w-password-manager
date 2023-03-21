<template>
  <div class="h-full flex flex-col max-w-7xl mx-auto p-3">
    <h1 class="text-2xl mb-6">Pico Password Manager</h1>

    <div class="grow overflow-y-auto divide-y px-3">
      <div
        v-for="(credentials, index) in credentialsList"
        :key="index"
      >
        <a
            href="#"
            class="block px-3 py-2 rounded-md outline-none hover:bg-gray-100 text-start -mx-3"
            @click="editCredentials = {...credentials}"
          >
            <span class="block">{{ credentials.title }}</span>
        </a>
      </div>
    </div>

    <button class="px-3 py-2 rounded-md outline-none text-indigo-500 hover:bg-gray-100 w-full text-center mt-2" @click="addItem">
      Add credentials
    </button>
  </div>
  <div v-if="editCredentials" class="fixed inset-0 bg-transparent-200 p-3">
    <div class="bg-gray-50 rounded-lg shadow-md max-w-5xl mx-auto px-3 py-2">
      <h2 class="text-xl mb-6">Edit credentials</h2>

      <div class="space-y-6 mb-8">
        <div>
          <label for="title" class="text-gray-500 font-light text-sm block mb-2">Title</label>
          <input id="title" type="text" v-model="editCredentials.title" placeholder="Credentials title" class="block w-full px-3 py-2 rounded-md bg-white ring-1 ring-gray-200 focus:ring-2 focus:ring-indigo-500 outline-none">
        </div>
        
        <div>
          <label for="username" class="text-gray-500 font-light text-sm block mb-2">Username</label>
          <input id="username" type="text" v-model="editCredentials.username" placeholder="Credentials username" class="block w-full px-3 py-2 rounded-md bg-white ring-1 ring-gray-200 focus:ring-2 focus:ring-indigo-500 outline-none">
        </div>

        <div>
          <label for="password" class="text-gray-500 font-light text-sm block mb-2">Password</label>
          <input id="password" type="password" v-model="editCredentials.password" placeholder="Credentials password" class="block w-full px-3 py-2 rounded-md bg-white ring-1 ring-gray-200 focus:ring-2 focus:ring-indigo-500 outline-none">
        </div>
      </div>

      <div class="flex space-x-3 justify-between">
        <button class="px-3 py-2 rounded-md outline-none bg-red-400 hover:bg-red-500 text-white" @click="deleteItem(editCredentials)">
          Delete
        </button>

        <div class="flex space-x-3">
          <button class="px-3 py-2 rounded-md outline-none bg-gray-100 hover:bg-gray-200" @click="editCredentials = null">
            Cancel
          </button>
          
          <button class="px-3 py-2 rounded-md outline-none bg-indigo-400 hover:bg-indigo-500 text-white" @click="saveItem(editCredentials)">
            Save
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        credentialsList: [],
        editCredentials: null,
      };
    },
    methods: {
      addItem() {
        const newIndex = this.credentialsList.length

        this.editCredentials = {
              index: newIndex,
              title: '',
              username: '',
              password: '',
        };
      },
      async deleteItem(credentials) {
        this.credentialsList = this.credentialsList.filter((_credentials, index) => index !== credentials.index);

        await this.updateAll();
      },
      async saveItem(credentials) {
        this.credentialsList[credentials.index] = credentials;

        await this.updateAll();
      },
      async updateAll() {
        this.editCredentials = null;

        await fetch('/update/before');

        for(let credentials of this.credentialsList) {
          const formData = new FormData();

          formData.append('title', credentials.title);
          formData.append('username', credentials.username);
          formData.append('password', credentials.password);

          await fetch('/update/append', {
            method: 'POST',
            body: formData,
          });
        }

        await this.loadList();
      },
      async loadList() {
        const credentialsListResponse = await (await fetch('/passwords')).text();

        this.credentialsList = credentialsListResponse.split(/\n/g)
          .filter(credentialsText => {
            return credentialsText.trim() !== '';
          })
          .map((credentialsText, index) => {
            const credentials = credentialsText.replace(/\n$/, '').split(/\t/g);

            return {
              index: index,
              title: credentials[0],
              username: credentials[1],
              password: credentials[2],
            };
          });
      },
    },
    async mounted() {
      await this.loadList();
    },
  }
</script>