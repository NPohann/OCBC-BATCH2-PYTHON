import cardStyles from './styles/card.module.css'

function Card (props) {
    return(
        <div className={cardStyles.card}>
            <div>
                <h3>{props.title}</h3>
                 by {props.userId}
            </div>
            <div>
                {props.completed ? 'Completed' : 'Pending'}
            </div>
            <button className='btn btn-primary'>Click Me!</button>
        </div>
    )
}

export default Card