import StateContext from "./context/StateContext";
import Landing from "./view/Landing";

function App() {
  return (
    <StateContext>
      <Landing />
    </StateContext>
  );
}

export default App;
