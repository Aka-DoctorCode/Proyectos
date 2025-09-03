import Styles from "./Styles/Button.module.css";
const Button = ({ children, ...rest }) => {
  return (
    <button className={Styles.button} {...rest}>
      {children}
    </button>
  );
};

export default Button;
