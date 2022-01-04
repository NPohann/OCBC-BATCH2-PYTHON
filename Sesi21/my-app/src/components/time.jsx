import React, {useState, useEffect} from "react";



function Times() {
    const [date, setDate] = useState(new Date())

    function tick() {
        setDate(new Date())
    }
    useEffect(() => {
        setInterval(() => tick(), 1000)
    })
    return (
        <div>
            <h1>Realtime CLOCK</h1>
            <hr />
            <h1>{date.toLocaleTimeString()}</h1>
        </div>
    )
}

export default Times