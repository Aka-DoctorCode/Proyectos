import Styles from "./Styles/NavBar.module.css";
import Logo from "../asset/Logo-Click-Salud simple.svg";
import Boton from "./Button";

const NavBar = () => {
  return (
    <nav>
      <div id={Styles.navbar}>
        <a id={Styles.logobox}>
          <img href="null" id={Styles.logo} src={Logo} alt="Logo Completo" />
          <div id={Styles.name}>
            <span className={Styles.clicksalud} id={Styles.click}>
              click
            </span>
            <span className={Styles.clicksalud} id={Styles.salud}>
              salud
            </span>
          </div>
        </a>
        <div id={Styles.rutas}>
          <a className={Styles.navegacion} href="null">
            Inicio
          </a>
          <a className={Styles.navegacion} href="null">
            Quienes Somos
          </a>
          <a className={Styles.navegacion} href="null">
            Servicios
          </a>
          <a className={Styles.navegacion} href="null">
            Planes y Precios
          </a>
          <a className={Styles.navegacion} href="null">
            Contactanos
          </a>
        </div>
        <div id={Styles.menuUsuario}>
          <a href="null" id={Styles.sesion}>
            Iniciar Sesión
          </a>
          <Boton
            href="null"
            // onClick={() => alert("hola")}
          >
            Registrarse
          </Boton>
        </div>
      </div>
      <div id={Styles.decoracion}></div>
    </nav>
  );
};

export default NavBar;
