<template>
  <div class="app">
    <header>
      <img class="logo" src="https://1000marcas.net/wp-content/uploads/2021/04/Planet-Express-logo.png" alt="Logo de la Empresa" />
      <h1>Tienda en Línea</h1>
      <div class="cart">
        <span>Carrito: {{ carrito.length }}</span>
        <span>Total: ${{ totalVenta.toFixed(2) }}</span>
      </div>
      <div v-if="usuario">
        <span>Bienvenido, {{ usuario }}     </span>
        <button @click="cerrarSesion">Cerrar Sesión</button>
      </div>
      <div v-else>
        <button @click="mostrarLogin">Iniciar Sesión</button>
      </div>
    </header>
    <main>
      <section class="productos">
        <div v-for="(producto, index) in productos" :key="index" class="producto">
          <img :src="producto.imagen" :alt="producto.nombre" />
          <h2>{{ producto.nombre }}</h2>
          <p>{{ producto.descripcion }}</p>
          <p>Precio: ${{ producto.precio.toFixed(2) }}</p>
          <button @click="agregarAlCarrito(producto)">Agregar al Carrito</button>
        </div>
      </section>
    </main>
    <aside class="carrito">
      <h2>Carrito de Compras</h2>
      <ul>
        <li v-for="(item, index) in carrito" :key="index">
          {{ item.nombre }} - ${{ item.precio.toFixed(2) }}
          <button @click="eliminarDelCarrito(index)">Eliminar</button>
        </li>
      </ul>
      <button @click="realizarVenta">Realizar Venta</button>
    </aside>
    <div v-if="mostrarFormularioLogin" class="login-form">
      <h2>Iniciar Sesión</h2>
      <input v-model="nombreUsuario" placeholder="Nombre de Usuario" />
      <input v-model="contrasena" type="password" placeholder="Contraseña" />
      <button @click="iniciarSesion">Iniciar Sesión</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      productos: [
      {
          nombre: 'Salchicha de Pavo',
          descripcion: 'Salchicha de Pavo Lala 100 de 500g',
          precio: 65.99,
          imagen: 'https://http2.mlstatic.com/D_NQ_NP_985811-MLU70711473394_072023-O.webp',
        },
        {
          nombre: 'Carne de res para hamburguesa',
          descripcion: 'Carne De Res Sukarne Hamburguesa 720g',
          precio: 92.99,
          imagen: 'https://http2.mlstatic.com/D_NQ_NP_712189-MLM49360907592_032022-O.webp',
        },
        {
          nombre: 'Cebolla En Trozos',
          descripcion: 'Cebolla En Trozos 470g Mccormick',
          precio: 239.99,
          imagen: 'https://http2.mlstatic.com/D_NQ_NP_632029-MLM49838380926_052022-V.webp',
        },
        {
          nombre: 'Pimiento Rojo Triturado',
          descripcion: 'Pimiento Rojo Triturado 368g Mccormick Gourmet Sazonador',
          precio: 169.99,
          imagen: 'https://http2.mlstatic.com/D_NQ_NP_919425-MLM53790177419_022023-V.webp',
        },
        {
          nombre: 'Sopa Maruchan Ramen',
          descripcion: 'Sopa Maruchan Ramen Sabor Camaron, Limón Y Habanero 85 Gr',
          precio: 6.99,
          imagen: 'https://http2.mlstatic.com/D_NQ_NP_805125-MLM47161873231_082021-V.webp',
        },
      ],
      carrito: [],
      mostrarFormularioLogin: false,
      nombreUsuario: '',
      usuario: null,
    };
  },
  computed: {
    totalVenta() {
      return this.carrito.reduce((total, item) => total + item.precio, 0);
    },
  },
  methods: {
    getUsuario() {
      const path = 'https://localhost:5000/api/login'
      axios.get(path).them((respuesta)=> {
        this.usuario = respuesta.data
      })
      .catch((error)=>{
        console.error(error);
      })
    },
    created(){
      this.getUsuario
    },
    agregarAlCarrito(producto) {
      this.carrito.push(producto);
    },
    eliminarDelCarrito(index) {
      this.carrito.splice(index, 1);
    },
    realizarVenta() {
      alert(`Venta realizada con éxito. Total: $${this.totalVenta.toFixed(2)}`);
      this.carrito = [];
    },
    mostrarLogin() {
      this.mostrarFormularioLogin = true;
    },
    iniciarSesion() {

      this.usuario = this.nombreUsuario;
      this.mostrarFormularioLogin = false;
    },
    cerrarSesion() {
      this.usuario = null;
    },
  },
};
</script>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  font-family: Arial, sans-serif;
}

header {
  background-color: #333;
  color: white;
  padding: 20px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.logo {
  max-height: 50px;
}

.cart {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  font-size: 18px;
}

main {
  padding: 20px;
}

.productos {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.producto {
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.carrito {
  margin-top: 20px;
  background-color: #f0f0f0;
  padding: 20px;
  width: 100%;
  max-width: 400px;
  text-align: left;
}

.carrito h2 {
  font-size: 20px;
  margin-bottom: 10px;
}

.carrito ul {
  list-style: none;
  padding: 0;
}

.carrito li {
  margin-bottom: 10px;
}

.carrito button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  margin-top: 10px;
}

.carrito button:hover {
  background-color: #45a049;
}

.login-form {
  margin-top: 20px;
  border: 1px solid #ddd;
  padding: 20px;
  max-width: 400px;
}

.login-form h2 {
  font-size: 20px;
  margin-bottom: 10px;
}

.login-form input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
}

.login-form button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

.login-form button:hover {
  background-color: #0056b3;
}
</style>