import { useEffect, useState } from "react";

function Counter () {
    const [ counter, setCounter ] = useState(0)

    useEffect(() => {
        console.log('Efek berjalan/di-trigger');
    })

    return (
        <div>
            <h2>Lets Count!</h2>
            <h3>{ counter }</h3>

            <button
                onClick={() => setCounter(counter+1)}
                style={{fontSize: '2em'}}
            >
            Hit me! 
            </button>
        </div>
    )
}

export default Counter