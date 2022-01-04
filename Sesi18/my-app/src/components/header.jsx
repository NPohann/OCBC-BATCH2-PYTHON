import React, { Component } from "react";


class Header extends Component {
    constructor(props) {
        super(props)
        this.state = {
            name: "FSD OCBC Batch ke-2!"
        }
    }

    changeName = () => {
        console.log(this.props);
        this.setState({
            name: this.state.name + 'FSD OCBC Materi React!!!'
        })
    }

    render() {
        return (
            <div>
                <h1>{this.props.batch}</h1>
                <img src={this.props.logo} alt="logo" />
                <h3>
                    Halo kelas { this.state.name }
                </h3>
                <button onClick={this.changeName}>Ganti nama, gan!</button>
            </div>
            
        )
    }
}

export default Header