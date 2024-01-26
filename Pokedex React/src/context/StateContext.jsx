import { counterContext } from './counterContext';

const StateContext = ({ children }) => {
	return (
		<counterContext.Provider value={{}}>{children}</counterContext.Provider>
	);
};

export default StateContext;
