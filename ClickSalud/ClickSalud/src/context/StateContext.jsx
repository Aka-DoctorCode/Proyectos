import Context from "./Context";

const StateContext = ({ children }) => {
  // const [descargoVisible, setDescargoVisible] = useState(true);
  // const descargoOcultar = () => {
  // 	setDescargoVisible(false);
  // };
  return (
    <Context.Provider
      value={
        {
          //     descargoVisible,
          //     descargoOcultar,
        }
      }
    >
      {children}
    </Context.Provider>
  );
};

export default StateContext;
