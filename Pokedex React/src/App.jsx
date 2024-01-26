import { useState } from 'react';
import './Styles/App.css';

const App = () => {
	const [pantalla, setPantalla] = useState('pantalla');
	function activar() {
		setPantalla('pantalla2');
	}
	return (
		<div id='fondo'>
			<div className='esquinero' id='SI' />
			<div className='esquinero' id='II' />
			<div className='esquinero' id='SD' />
			<div className='esquinero' id='ID' />
			<div id={pantalla} />
			<div id='contenedor'>
				<div id='circulo' onClick={activar}>
					<div id='barra' />
					<div id='centro' />
					<span>PokeDEX</span>
				</div>
			</div>
		</div>
	);
};

export default App;
